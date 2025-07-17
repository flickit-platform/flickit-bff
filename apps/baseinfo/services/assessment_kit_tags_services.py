import requests

from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider
from assessmentplatform.settings import ASSESSMENT_URL


def get_assessment_kit_tags(request):
    response = requests.get(
        ASSESSMENT_URL + 'assessment-core/api/assessment-kit-tags',
        params=request.query_params,
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}
