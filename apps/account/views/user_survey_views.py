from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response

from account.services import user_survey_services
from assessmentplatform.auth.authentication_provider import authenticate


class UserSurveysApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def post(self, request):
        result = user_survey_services.set_dont_show_again(request)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])