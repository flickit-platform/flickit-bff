import requests

from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider
from assessmentplatform.settings import ASSESSMENT_URL


def get_assessment_permissions_list(request, assessment_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/permissions',
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}
