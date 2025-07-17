from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response

from assessmentplatform.auth.authentication_provider import authenticate
from baseinfo.services import dsl_services, assessment_kit


class ImportDslFileView(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request):
        result = dsl_services.upload_dsl_assessment(request=request)
        return Response(data=result["body"], status=result["status_code"])


class CreateAssessmentKitByDsl(APIView):
    authenticate()

    def post(self, request):
        result = assessment_kit.create_assessment_by_dsl(data=request.data,
                                                         request=request)
        return Response(data=result["body"], status=result["status_code"])
