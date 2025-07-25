import requests

from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider
from assessmentplatform.settings import ASSESSMENT_URL


def add_evidences(request):
    response = requests.post(
        ASSESSMENT_URL + f'assessment-core/api/evidences',
        json=request.data,
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_list_evidences(request):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/evidences',
        params=request.query_params,
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def edit_evidence(request, evidence_id):
    response = requests.put(
        ASSESSMENT_URL + f'assessment-core/api/evidences/{evidence_id}',
        json=request.data,
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def delete_evidence(request, evidence_id):
    response = requests.delete(
        ASSESSMENT_URL + f'assessment-core/api/evidences/{evidence_id}',
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 204:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response}


def evidence_add_attachments(request, evidence_id):
    file = request.data.get('attachment')
    data = request.data
    data.pop('attachment')
    response = requests.post(
        ASSESSMENT_URL + f'assessment-core/api/evidences/{evidence_id}/attachments',
        files={'attachment': (file.name, file, file.content_type)},
        data=request.data,
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def evidence_list_attachments(request, evidence_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/evidences/{evidence_id}/attachments',
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def evidence_delete_attachment(request, evidence_id, attachment_id):
    response = requests.delete(
        ASSESSMENT_URL + f'assessment-core/api/evidences/{evidence_id}/attachments/{attachment_id}',
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 204:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def evidence_get_by_id(request, evidence_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/evidences/{evidence_id}',
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def evidence_resolve_comment(request, evidence_id):
    response = requests.put(
        ASSESSMENT_URL + f'assessment-core/api/evidences/{evidence_id}/resolve',
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}
