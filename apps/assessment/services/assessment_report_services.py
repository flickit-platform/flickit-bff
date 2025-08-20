import requests

from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider
from assessmentplatform.settings import ASSESSMENT_URL


def get_assessment_report(request, assessment_id):
    response = requests.get(ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/report',
                            headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_assessment_subject_report(request, assessment_id, subject_id):
    response = requests.get(ASSESSMENT_URL +
                            f'assessment-core/api/assessments/{assessment_id}/report/subjects/{subject_id}',
                            headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_assessment_progress(request, assessment_id):
    response = requests.get(ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/progress',
                            headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_graphical_report(request, assessment_id):
    response = requests.get(ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/graphical-report',
                            headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_public_graphical_report(request, link_hash):
    response = requests.get(ASSESSMENT_URL + f'assessment-core/api/public/assessments/graphical-report/{link_hash}',
                            headers=AuthHeaderProvider(request).get_accept_language_header())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def report_publish_status(request, assessment_id):
    response = requests.put(ASSESSMENT_URL +
                            f'assessment-core/api/assessments/{assessment_id}/report-publish-status',
                            json=request.data,
                            headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def report_visibility_status(request, assessment_id):
    response = requests.put(ASSESSMENT_URL +
                            f'assessment-core/api/assessments/{assessment_id}/report-visibility-status',
                            json=request.data,
                            headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": response.json(), "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def prepare_assessment_report(request, assessment_id):
    response = requests.post(ASSESSMENT_URL +
                            f'assessment-core/api/assessments/{assessment_id}/prepare-report',
                            json=request.data,
                            headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}
