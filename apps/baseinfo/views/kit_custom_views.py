from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from assessmentplatform.auth.authentication_provider import authenticate
from baseinfo.services import custom_kit_services


class KitCustomApi(APIView):
    authenticate()

    def get(self, request, custom_kit_id):
        result = custom_kit_services.get_custom_kit(request, custom_kit_id)
        return Response(data=result["body"], status=result["status_code"])

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, custom_kit_id):
        result = custom_kit_services.update_custom_kit(request, custom_kit_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])
