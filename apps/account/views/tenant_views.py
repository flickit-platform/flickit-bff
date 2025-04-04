from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from account.services import tenant_services


class TenantApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        result = tenant_services.get_tenant(request)
        return Response(data=result["body"], status=result["status_code"])
