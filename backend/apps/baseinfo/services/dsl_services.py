import requests
from assessmentplatform.settings import DSL_PARSER_URL_SERVICE, ASSESSMENT_URL
from baseinfo.models.assessmentkitmodels import ExpertGroup
from rest_framework import status


def upload_dsl_assessment(request):
    file = request.data.get('dslFile')
    data = request.data
    data.pop('dslFile')
    response = requests.post(ASSESSMENT_URL + f'assessment-core/api/assessment-kits/upload-dsl',
                             data=data,
                             files={'dslFile': (file.name, file, file.content_type)},
                             headers={'Authorization': request.headers['Authorization']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def download_dsl_assessment(assessment_kit_id, request):
    response = requests.get(ASSESSMENT_URL + f'assessment-core/api/assessment-kits/{assessment_kit_id}/dsl-download-link',
                            headers={'Authorization': request.headers['Authorization']})
    return {"Success": False, "body": response.json(), "status_code": response.status_code}
