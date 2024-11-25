from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from baseinfo.services import custom_kit_services


class KitCustomApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, custom_kit_id):
        result = custom_kit_services.get_custom_kit(request, custom_kit_id)
        return Response(data=result["body"], status=result["status_code"])
