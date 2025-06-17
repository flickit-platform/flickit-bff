from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from concurrent.futures import ThreadPoolExecutor, as_completed
import datetime
from assessment.services import assessment_report_services, assessment_permission_services, assessment_services, \
    advice_services, maturity_level_services


class AssessmentReportApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, assessment_id):
        permissions_result = assessment_permission_services.get_assessment_permissions_list(request, assessment_id)
        result = assessment_report_services.get_assessment_report(request, assessment_id)
        if result["status_code"] == 200 and permissions_result["status_code"] == 200:
            result["body"]["permissions"] = permissions_result["body"]["permissions"]
            return Response(data=result["body"], status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class AssessmentSubjectReportApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, assessment_id, subject_id):
        permissions_result = assessment_permission_services.get_assessment_permissions_list(request, assessment_id)
        result = assessment_report_services.get_assessment_subject_report(request, assessment_id, subject_id)
        if result["status_code"] == 200 and permissions_result["status_code"] == 200:
            result["body"]["permissions"] = permissions_result["body"]["permissions"]
            return Response(data=result["body"], status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class AssessmentProgressApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, assessment_id):
        result = assessment_report_services.get_assessment_progress(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])


class GraphicalReportApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, assessment_id):
        assessment = assessment_services.load_assessment(request, assessment_id)
        if assessment["status_code"] == 200:
            data = assessment["body"]
            mode = data.get("mode")
            if mode['code'] == "QUICK":
                # Calculate maturity level first
                data = maturity_level_services.calculate_maturity_level(request, assessment_id)
                calculate_result = data["body"]

                # Then run both services concurrently
                with ThreadPoolExecutor(max_workers=2) as executor:
                    # Define wrapper functions to track execution time
                    def prepare_with_logging():
                        print(f"[{datetime.datetime.now()}] Starting prepare_assessment_report")
                        result = assessment_report_services.prepare_assessment_report(request, assessment_id)
                        print(f"[{datetime.datetime.now()}] Finished prepare_assessment_report")
                        return result

                    def refresh_with_logging():
                        print(f"[{datetime.datetime.now()}] Starting refresh_advice")
                        result = advice_services.refresh_advice(
                            request,
                            assessment_id,
                            calculate_result["resultAffected"]
                        )
                        print(f"[{datetime.datetime.now()}] Finished refresh_advice")
                        return result

                    # Submit both tasks to the executor
                    prepare_future = executor.submit(prepare_with_logging)
                    refresh_future = executor.submit(refresh_with_logging)

                    # Wait for both tasks to complete
                    for future in as_completed([prepare_future, refresh_future]):
                        try:
                            future.result()  # Get the result to catch any exceptions
                        except Exception as e:
                            # Handle exceptions if needed
                            print(f"Service call failed: {e}")

        result = assessment_report_services.get_graphical_report(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])


class ReportPublishStatus(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, assessment_id):
        result = assessment_report_services.report_publish_status(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class ReportVisibilityStatus(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, assessment_id):
        result = assessment_report_services.report_visibility_status(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])


class PublicGraphicalReportApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, link_hash):
        result = assessment_report_services.get_public_graphical_report(request, link_hash)
        return Response(data=result["body"], status=result["status_code"])
