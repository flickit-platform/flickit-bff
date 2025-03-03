from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from assessment.services import comments_services


class CommentsApi(APIView):
    permission_classes = [IsAuthenticated]
    size_param = openapi.Parameter('size', openapi.IN_QUERY, description="size param",
                                   type=openapi.TYPE_INTEGER)
    page_param = openapi.Parameter('page', openapi.IN_QUERY, description="page param",
                                   type=openapi.TYPE_INTEGER)
    questionId_param = openapi.Parameter('questionId', openapi.IN_QUERY, description="questionId param",
                                   type=openapi.TYPE_INTEGER)
    assessmentId_param = openapi.Parameter('assessmentId', openapi.IN_QUERY, description="assessmentId param",
                                   type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[size_param, page_param, questionId_param, assessmentId_param])
    def get(self, request):
        result = comments_services.get_list_comments(request)
        if result["Success"]:
            return Response(status=result["status_code"])
        return Response(data=result["body"], status=result["status_code"])
