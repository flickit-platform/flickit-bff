import requests

from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider
from assessmentplatform.settings import ASSESSMENT_URL


def calculate_maturity_level(request, assessment_id):
    response = requests.post(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/calculate',
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}
