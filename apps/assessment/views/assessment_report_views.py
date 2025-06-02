from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
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
                assessment_report_services.prepare_assessment_report(request, assessment_id)
                data = maturity_level_services.calculate_maturity_level(request, assessment_id)
                calculate_result = data["body"]
                advice_services.refresh_advice(request, assessment_id, calculate_result["resultAffected"])

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
