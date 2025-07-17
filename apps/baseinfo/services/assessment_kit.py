import requests

from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider
from assessmentplatform.settings import ASSESSMENT_URL
from rest_framework import status


def create_assessment_by_dsl(data, request):
    response = requests.post(ASSESSMENT_URL + f'assessment-core/api/assessment-kits/create-by-dsl', json=data,
                             headers=AuthHeaderProvider(request).get_headers())
    return {"Success": False, "body": response.json(), "status_code": response.status_code}
