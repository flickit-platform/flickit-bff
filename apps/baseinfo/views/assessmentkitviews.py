from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

from assessmentplatform.auth.authentication_provider import authenticate
from baseinfo.services import assessment_kit_service, dsl_services


class EditAssessmentKitInfoApi(APIView):

    def get(self, request, assessment_kit_id):
        result = assessment_kit_service.get_assessment_kit_publish(request, assessment_kit_id)
        return Response(data=result["body"], status=result["status_code"])


class LoadAssessmentKitFileApi(APIView):
    authenticate()

    def get(self, request, assessment_kit_id):
        result = dsl_services.download_dsl_assessment(assessment_kit_id=assessment_kit_id, request=request)
        return Response(data=result["body"], status=result["status_code"])
