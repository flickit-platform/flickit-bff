import requests

from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider
from assessmentplatform.settings import ASSESSMENT_URL


def set_dont_show_again(request):
    response = requests.post(
        ASSESSMENT_URL + f'assessment-core/api/user-surveys/dont-show-again',
        json=request.data,
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}

def init_survey(request):
    response = requests.post(
        ASSESSMENT_URL + f'assessment-core/api/init-survey',
        json=request.data,
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 201:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}