
from rest_framework.views import APIView
from rest_framework.response import Response

from assessmentplatform.auth.authentication_provider import authenticate
from baseinfo.services import assessment_kit_tags_services


class AssessmentKitTagsApi(APIView):
    authenticate()

    def get(self, request):
        result = assessment_kit_tags_services.get_assessment_kit_tags(request)
        return Response(data=result["body"], status=result["status_code"])
