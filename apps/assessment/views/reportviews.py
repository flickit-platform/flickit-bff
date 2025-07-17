from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from assessment.services import assessment_core
from assessmentplatform.auth.authentication_provider import authenticate


class SubjectProgressApi(APIView):
    authenticate()

    def get(self, request, assessment_id, subject_id):
        result = assessment_core.get_subject_progress(request,
                                                      assessment_id,
                                                      subject_id)
        return Response(result["body"], result["status_code"])


class AssessmentAttributesReportApi(APIView):
    authenticate()

    maturity_level_id_param = openapi.Parameter('maturityLevelId', openapi.IN_QUERY,
                                                description="maturity level id param",
                                                type=openapi.TYPE_INTEGER, required=True)

    @swagger_auto_schema(manual_parameters=[maturity_level_id_param])
    def get(self, request, assessment_id, attribute_id):
        result = assessment_core.get_assessment_attribute_report(request, assessment_id, attribute_id)
        return Response(result["body"], result["status_code"])

class AttributeScoreStatsAPIView(APIView):
    authenticate()

    maturity_level_id_param = openapi.Parameter('maturityLevelId', openapi.IN_QUERY,
                                                description="maturity level id param",
                                                type=openapi.TYPE_INTEGER, required=True)

    @swagger_auto_schema(manual_parameters=[maturity_level_id_param])
    def get(self, request, assessment_id, attribute_id):
        result = assessment_core.get_attribute_stats_report(request, assessment_id, attribute_id)
        return Response(result["body"], result["status_code"])
