import requests

from assessmentplatform.settings import ASSESSMENT_URL


def get_assessment_report(request, assessment_id):
    response = requests.get(ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/report',
                            headers={'Authorization': request.headers['Authorization']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_assessment_subject_report(request, assessment_id, subject_id):
    response = requests.get(ASSESSMENT_URL +
                            f'assessment-core/api/assessments/{assessment_id}/report/subjects/{subject_id}',
                            headers={'Authorization': request.headers['Authorization']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_assessment_progress(request, assessment_id):
    response = requests.get(ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/progress',
                            headers={'Authorization': request.headers['Authorization']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_assessment_attributes_report_ai(request, assessment_id, attribute_id):
    response = requests.post(ASSESSMENT_URL +
                             f'assessment-core/api/assessments/{assessment_id}/ai-report/attributes/{attribute_id}',
                             headers={'Authorization': request.headers['Authorization']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def assessment_attributes_report_ai_edit(request, assessment_id, attribute_id):
    response = requests.put(ASSESSMENT_URL +
                            f'assessment-core/api/assessments/{assessment_id}/ai-report/attributes/{attribute_id}',
                            json=request.data,
                            headers={'Authorization': request.headers['Authorization']})
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def load_assessment_attributes_report_ai(request, assessment_id, attribute_id):
    response = requests.get(ASSESSMENT_URL +
                             f'assessment-core/api/assessments/{assessment_id}/ai-report/attributes/{attribute_id}',
                             headers={'Authorization': request.headers['Authorization']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}
