from rest_framework.views import APIView
from rest_framework.response import Response

from assessmentplatform.auth.authentication_provider import authenticate
from baseinfo.services import kit_language_services


class KitLanguageViews(APIView):
    authenticate()

    def get(self, request):
        result = kit_language_services.load_kit_languages(request)
        return Response(data=result["body"], status=result["status_code"])
