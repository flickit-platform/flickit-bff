from http import HTTPStatus

import requests

from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider
from assessmentplatform.settings import ASSESSMENT_URL


def get_list_comments(request):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/comments',
        params=request.query_params,
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}

def resolve_assessment_comments(request, assessment_id):
    response = requests.put(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/resolve-comments',
        params=request.query_params,
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code != HTTPStatus.OK:
        return {"Success": False, "body": response.json(), "status_code": response.status_code}
    return {"Success": True, "body": None, "status_code": response.status_code}