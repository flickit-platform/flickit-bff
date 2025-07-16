class AuthHeaderProvider:
    """
    Utility class to extract and validate required headers from an incoming request.
    """

    def __init__(self, request):
        self.request = request

    def get_headers(self):
        """
        Return a dictionary with 'Authorization' and 'Accept-Language' headers.
        Raises ValueError if any required header is missing.
        """
        return {
            'Authorization': self._get_header('Authorization'),
            'Accept-Language': self._get_header('Accept-Language')
        }

    def _get_header(self, name):
        """
        Helper method to safely retrieve a header or raise an error if missing.
        """
        if name not in self.request.headers:
            raise ValueError(f"Missing required header: {name}")
        return self.request.headers[name]
