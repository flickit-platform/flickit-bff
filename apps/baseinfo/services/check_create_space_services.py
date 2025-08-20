import requests

from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider
from assessmentplatform.settings import ASSESSMENT_URL


def check_allowance(request):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/check-create-space',
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": response.json(), "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}
