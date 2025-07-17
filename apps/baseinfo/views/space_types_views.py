from rest_framework.views import APIView
from rest_framework.response import Response

from assessmentplatform.auth.authentication_provider import authenticate
from baseinfo.services import space_types_services


class SpaceTypesView(APIView):
    authenticate()

    def get(self, request):
        result = space_types_services.load_space_types(request)
        return Response(data=result["body"], status=result["status_code"])
