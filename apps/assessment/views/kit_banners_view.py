from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from assessment.services import kit_banners_services


class AssessmentKitBannersApi(APIView):
    permission_classes = [AllowAny]

    lang_param = openapi.Parameter('lang', openapi.IN_QUERY, description="lang",
                                   type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[lang_param])
    def get(self, request):
        result = kit_banners_services.get_list_slider_banners(request)
        return Response(data=result["body"], status=result["status_code"])