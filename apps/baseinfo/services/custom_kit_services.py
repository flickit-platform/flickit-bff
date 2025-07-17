import requests

from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider
from assessmentplatform.settings import ASSESSMENT_URL


def create_custom_kit(request, kit_id):
    data = dict(request.data)
    data['kitId'] = kit_id
    response = requests.post(
        ASSESSMENT_URL + 'assessment-core/api/kit-customs',
        json=data,
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_custom_kit(request, custom_kit_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/kit-customs/{custom_kit_id}',
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def update_custom_kit(request, custom_kit_id):
    response = requests.put(
        ASSESSMENT_URL + f'assessment-core/api/kit-customs/{custom_kit_id}',
        json=request.data,
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}
