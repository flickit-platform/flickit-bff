from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from assessment.services import assessment_insight_services
from assessmentplatform.auth.authentication_provider import authenticate


class AssessmentInsightApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request, assessment_id):
        result = assessment_insight_services.create_assessment_insights(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

    def get(self, request, assessment_id):
        result = assessment_insight_services.get_assessment_overall_insights(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])

class AssessmentInsightsApi(APIView):
    authenticate()

    def get(self, request, assessment_id):
        result = assessment_insight_services.get_assessment_insights(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])


class SubjectInitInsightApi(APIView):
    authenticate()

    def post(self, request, assessment_id, subject_id):
        result = assessment_insight_services.init_subject_insight(request,
                                                                  assessment_id,
                                                                  subject_id)
        return Response(result["body"], result["status_code"])


class AssessmentSubjectLoadInsightApi(APIView):
    authenticate()

    def get(self, request, assessment_id, subject_id):
        result = assessment_insight_services.get_assessment_subject_insights(request, assessment_id, subject_id)
        return Response(data=result["body"], status=result["status_code"])

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request, assessment_id, subject_id):
        result = assessment_insight_services.create_assessment_subject_insight(request, assessment_id, subject_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class ApproveAttributeInsightApi(APIView):
    authenticate()

    def put(self, request, assessment_id, attribute_id):
        result = assessment_insight_services.approve_attribute_insight(request, assessment_id, attribute_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class ApproveSubjectInsightApi(APIView):
    authenticate()

    def put(self, request, assessment_id, subject_id):
        result = assessment_insight_services.approve_subject_insight(request, assessment_id, subject_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class InitAssessmentInsightApi(APIView):
    authenticate()

    def post(self, request, assessment_id):
        result = assessment_insight_services.init_assessment_insight(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

class ApproveAssessmentInsightApi(APIView):
    authenticate()

    def put(self, request, assessment_id):
        result = assessment_insight_services.approve_assessment_insight(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class AssessmentAttributeInsightApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def post(self, request, assessment_id, attribute_id):
        result = assessment_insight_services.create_attributes_insight(request, assessment_id, attribute_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

    def get(self, request, assessment_id, attribute_id):
        result = assessment_insight_services.get_assessment_attribute_insight(request, assessment_id, attribute_id)
        return Response(data=result["body"], status=result["status_code"])


class AssessmentAttributeAiInsightApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def post(self, request, assessment_id, attribute_id):
        result = assessment_insight_services.create_attributes_ai_insight(request, assessment_id, attribute_id)
        return Response(data=result["body"], status=result["status_code"])


class ApproveAllAssessmentInsightsApi(APIView):
    authenticate()

    def put(self, request, assessment_id):
        result = assessment_insight_services.approve_all_assessment_insights(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class GenerateAllAssessmentInsightsApi(APIView):
    authenticate()

    def put(self, request, assessment_id):
        result = assessment_insight_services.generate_all_assessment_insights(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class RegenerateExpiredAssessmentInsightsApi(APIView):
    authenticate()

    def put(self, request, assessment_id):
        result = assessment_insight_services.regenerate_expired_assessment_insights(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class ApproveExpiredAssessmentInsightsApi(APIView):
    authenticate()

    def put(self, request, assessment_id):
        result = assessment_insight_services.approve_expired_assessment_insights(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class GetAssessmentInsightsIssuesApi(APIView):
    authenticate()

    def get(self, request, assessment_id):
        result = assessment_insight_services.get_assessment_insights_issues(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])