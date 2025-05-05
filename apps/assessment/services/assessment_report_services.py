import requests

from assessmentplatform.settings import ASSESSMENT_URL


def get_assessment_report(request, assessment_id):
    response = requests.get(ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/report',
                            headers={'Authorization': request.headers['Authorization'],
                                     'Accept-Language': request.headers['Accept-Language']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_assessment_subject_report(request, assessment_id, subject_id):
    response = requests.get(ASSESSMENT_URL +
                            f'assessment-core/api/assessments/{assessment_id}/report/subjects/{subject_id}',
                            headers={'Authorization': request.headers['Authorization'],
                                     'Accept-Language': request.headers['Accept-Language']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_assessment_progress(request, assessment_id):
    response = requests.get(ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/progress',
                            headers={'Authorization': request.headers['Authorization'],
                                     'Accept-Language': request.headers['Accept-Language']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_graphical_report(request, assessment_id):
    response = requests.get(ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/graphical-report',
                            headers={'Authorization': request.headers['Authorization'],
                                     'Accept-Language': request.headers['Accept-Language']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def report_publish_status(request, assessment_id):
    response = requests.put(ASSESSMENT_URL +
                            f'assessment-core/api/assessments/{assessment_id}/report-publish-status',
                            json=request.data,
                            headers={'Authorization': request.headers['Authorization'],
                                     'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def report_visibility_status(request, assessment_id):
    response = requests.put(ASSESSMENT_URL +
                            f'assessment-core/api/assessments/{assessment_id}/report-visibility-status',
                            json=request.data,
                            headers={'Authorization': request.headers['Authorization'],
                                     'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 200:
        return {"Success": True, "body": response.json(), "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}
