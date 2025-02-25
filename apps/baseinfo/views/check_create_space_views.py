from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from baseinfo.services import check_create_space_services


class Checkcreatespaceview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = check_create_space_services.check_allowance(request)
        return Response(data=result["body"], status=result["status_code"])
