from rest_framework.views import APIView
from rest_framework.response import Response

from account.services import notify_settings_services
from assessmentplatform.auth.authentication_provider import authenticate


class NotificationSettingsApi(APIView):
    authenticate()

    def get(self, request):
        result = notify_settings_services.get_notify_settings(request)
        return Response(data=result["body"], status=result["status_code"])

