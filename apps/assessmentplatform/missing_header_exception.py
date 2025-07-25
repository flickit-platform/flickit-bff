from rest_framework.exceptions import APIException
from rest_framework import status

class MissingHeaderException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Required header is missing.'
    default_code = 'missing_header'