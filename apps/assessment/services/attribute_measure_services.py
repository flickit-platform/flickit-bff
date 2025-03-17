import requests

from assessmentplatform.settings import ASSESSMENT_URL


def get_list_measures(request, assessment_id, attribute_d):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/attributes/{attribute_d}/measures',
        params=request.query_params,
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}
