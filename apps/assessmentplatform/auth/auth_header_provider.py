from rest_framework.exceptions import AuthenticationFailed, PermissionDenied

from assessmentplatform.missing_header_exception import MissingHeaderException


class AuthHeaderProvider:

    def __init__(self, request):
        self.request = request

    def get_headers(self):
        return {
            'Authorization': self._get_header('Authorization'),
            'Accept-Language': self._get_header('Accept-Language')
        }

    def _get_header(self, name):
        if name not in self.request.headers:
            raise MissingHeaderException(f"Missing required header: {name}")
        return self.request.headers[name]
