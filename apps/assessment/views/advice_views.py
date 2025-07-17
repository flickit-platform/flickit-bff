from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response

from assessment.services import advice_services
from assessmentplatform.auth.authentication_provider import authenticate


class AdviceView(APIView):
    authenticate()

    def post(self, request, assessment_id):
        result = advice_services.get_advice(request, assessment_id)
        return Response(result["body"], result["status_code"])


class AdviceNarrationView(APIView):
    authenticate()

    def get(self, request, assessment_id):
        result = advice_services.get_advice_narration(request, assessment_id)
        return Response(result["body"], result["status_code"])

    @swagger_auto_schema(
        operation_description="create advice narration for assessor.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['assessment_id']
        ),
        responses={
            201: ""}
    )
    def post(self, request, assessment_id):
        result = advice_services.create_advice_narration(request, assessment_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])


class AdviceNarrationAiView(APIView):
    authenticate()

    @swagger_auto_schema(
        operation_description="Get advice narration for a specific assessment.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['assessment_id']
        ),
        responses={
            201: openapi.Response(
                description="Advice narration retrieved successfully.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'content': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='A message indicating that AI is disabled.',
                            example='Ai Is Disabled'
                        )
                    }
                )
            ),
            400: openapi.Response(description="Bad Request - Invalid input."),
            500: openapi.Response(description="Internal Server Error - An error occurred while retrieving narration."),
        }
    )
    def post(self, request, assessment_id):
        result = advice_services.create_advice_narration_ai(request, assessment_id)
        return Response(result["body"], result["status_code"])


class AdviceItemsApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={201: ""})
    def post(self, request):
        result = advice_services.create_advice_items(request)
        return Response(result["body"], result["status_code"])

    assessment_id = openapi.Parameter('assessmentId', openapi.IN_QUERY, description="assessmentId param",
                                      type=openapi.TYPE_STRING, required=True)
    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(manual_parameters=[size_param, page_param, assessment_id])
    def get(self, request):
        result = advice_services.get_advice_items(request)
        return Response(result["body"], result["status_code"])


class AdviceItemApi(APIView):
    authenticate()

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT), responses={200: ""})
    def put(self, request, advice_item_id):
        result = advice_services.update_advice_item(request, advice_item_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])

    def delete(self, request, advice_item_id):
        result = advice_services.delete_advice_item(request, advice_item_id)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])
