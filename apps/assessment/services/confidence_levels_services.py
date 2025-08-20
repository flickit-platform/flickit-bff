import requests

from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider
from assessmentplatform.settings import ASSESSMENT_URL


def get_confidence_levels_in_assessment_core(request):
    response = requests.get(ASSESSMENT_URL + 'assessment-core/api/confidence-levels',
                            headers=AuthHeaderProvider(request).get_headers())

    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_confidence_levels_calculate_in_assessment_core(request, assessment_id):
    response = requests.post(ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/calculate-confidence',
                             headers=AuthHeaderProvider(request).get_headers())

    return {"Success": True, "body": response.json(), "status_code": response.status_code}
