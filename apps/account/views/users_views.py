from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from account.services import users_services
from account.services.users_services import get_user_id_by_email
from assessmentplatform.auth.authentication_provider import authenticate


class UserInfoApi(APIView):
    authenticate()

    def get(self, request):
        result = users_services.user_info(request)
        return Response(data=result["body"], status=result["status_code"])


class UserProfileApi(APIView):
    authenticate()

    def get(self, request):
        result = users_services.load_user_profile(request)
        return Response(data=result["body"], status=result["status_code"])

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request):
        result = users_services.edit_user_profile(request)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class LoadUserByEmailApi(APIView):
    authenticate()

    def get(self, request, email):
        result = get_user_id_by_email(email)
        return Response(data=result["body"], status=result["status_code"])


class UserProfilePictureApi(APIView):
    authenticate()
    parser_classes = [MultiPartParser, FormParser]

    picture_param = openapi.Parameter('pictureFile', openapi.IN_FORM, description="picture file",
                                      type=openapi.TYPE_FILE, required=True)

    @swagger_auto_schema(manual_parameters=[picture_param])
    def put(self, request):
        result = users_services.update_user_profile_picture(request)
        return Response(data=result["body"], status=result["status_code"])
