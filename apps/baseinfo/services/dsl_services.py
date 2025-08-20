import requests

from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider
from assessmentplatform.settings import ASSESSMENT_URL


def upload_dsl_assessment(request):
    file = request.data.get('dslFile')
    data = request.data
    data.pop('dslFile')
    response = requests.post(ASSESSMENT_URL + f'assessment-core/api/assessment-kits/upload-dsl',
                             data=data,
                             files={'dslFile': (file.name, file, file.content_type)},
                             headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def download_dsl_assessment(assessment_kit_id, request):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessment-kits/{assessment_kit_id}/dsl-download-link',
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def get_dsl_json(request, assessment_kit_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessment-kits/{assessment_kit_id}/dsl',
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": False, "body": response.json(), "status_code": response.status_code}
