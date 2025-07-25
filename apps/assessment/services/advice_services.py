import requests

from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider
from assessmentplatform.settings import ASSESSMENT_URL


def get_advice(request, assessment_id):
    result = dict()
    response = requests.post(ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/advice',
                             json=request.data,
                             headers=AuthHeaderProvider(request).get_headers())
    result["Success"] = False
    result["body"] = response.json()
    result["status_code"] = response.status_code
    return result


def get_advice_narration(request, assessment_id):
    response = requests.get(ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/advice-narration',
                            headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def create_advice_narration_ai(request, assessment_id):
    response = requests.post(ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/advice-narration-ai',
                             json=request.data,
                             headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def create_advice_narration(request, assessment_id):
    response = requests.post(ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/advice-narration',
                             json=request.data,
                             headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 201:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def create_advice_items(request):
    response = requests.post(ASSESSMENT_URL + 'assessment-core/api/advice-items',
                             json=request.data,
                             headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_advice_items(request):
    response = requests.get(ASSESSMENT_URL + 'assessment-core/api/advice-items',
                            params=request.query_params,
                            headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def update_advice_item(request, advice_item_id):
    response = requests.put(ASSESSMENT_URL + f'assessment-core/api/advice-items/{advice_item_id}',
                            json=request.data,
                            headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def delete_advice_item(request, advice_item_id):
    response = requests.delete(ASSESSMENT_URL + f'assessment-core/api/advice-items/{advice_item_id}',
                               headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 204:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def refresh_advice(request, assessment_id, result_affected):
    data = dict(request.data)
    data['forceRegenerate'] = result_affected
    response = requests.post(ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/refresh-advice',
                             json=data,
                             headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}