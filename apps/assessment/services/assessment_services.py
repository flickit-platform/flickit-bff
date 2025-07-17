from http import HTTPStatus

import requests

from assessment.services import assessment_permission_services
from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider
from assessmentplatform.settings import ASSESSMENT_URL


def get_questionnaires_with_assessment_id(request, assessment_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/questionnaires',
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def assessment_delete(request, assessment_id):
    response = requests.delete(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}',
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 204:
        return {"Success": False, "body": None, "status_code": response.status_code}
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def edit_assessment(request, assessment_id):
    response = requests.put(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}',
        json=request.data,
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def create_assessment(request):
    response = requests.post(
        ASSESSMENT_URL + f'assessment-core/api/assessments',
        json=request.data,
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def load_assessment(request, assessment_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}',
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def list_assessments(request):
    response = requests.get(
        ASSESSMENT_URL + 'assessment-core/api/assessments',
        params=request.query_params,
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def assessments_comparable_list(request):
    response = requests.get(
        ASSESSMENT_URL + 'assessment-core/api/comparable-assessments',
        params=request.query_params,
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def assessments_invite_user(request, assessment_id):
    response = requests.post(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/invite',
        json=request.data,
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def assessment_invitees(request, assessment_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/invitees',
        params=request.query_params,
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def assessment_invite_delete(request, invite_id):
    response = requests.delete(
        ASSESSMENT_URL + f'assessment-core/api/assessment-invites/{invite_id}',
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 204:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def assessment_invite_edit(request, invite_id):
    response = requests.put(
        ASSESSMENT_URL + f'assessment-core/api/assessment-invites/{invite_id}',
        json=request.data,
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def assessment_migrate_kit_version(request, assessment_id):
    response = requests.post(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/migrate-kit-version',
        json=request.data,
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def assign_custom_kit(request, assessment_id, custom_kit_id):
    data = request.data
    data["kitCustomId"] = custom_kit_id
    response = requests.put(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/assign-kit-custom',
        json=data,
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def access_assessment_report_grant(request, assessment_id):
    response = requests.post(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/grant-report-access',
        json=request.data,
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 201:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def get_report_users_access(request, assessment_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/users-with-report-access',
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_report_metadata(request, assessment_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/report-metadata',
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def update_report_metadata(request, assessment_id):
    response = requests.patch(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/report-metadata',
        json=request.data,
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 201:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def get_question_issues(request, assessment_id, question_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/questions/{question_id}/issues',
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}

def get_pre_advice_info(request, assessment_id):
    permissions_result = assessment_permission_services.get_assessment_permissions_list(request, assessment_id)
    if permissions_result.get("createAdvice", False):
        return {"Success": False, "body": "Not allowed to perform this action", "status_code": HTTPStatus.FORBIDDEN}

    attributes_response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/attributes',
        headers=AuthHeaderProvider(request).get_headers())
    maturity_levels_response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/maturity-levels',
        headers=AuthHeaderProvider(request).get_headers())

    merged_response = {}
    if attributes_response.status_code == 200 and maturity_levels_response.status_code == 200:
        attributes_data = attributes_response.json().get("attributes", [])
        processed_attributes = [
            {
                "id": attr["id"],
                "title": attr["title"],
                "maturityLevel": {"id": attr["maturityLevel"]["id"]},
                "subject": {
                    "id": attr["subject"]["id"],
                    "title": attr["subject"]["title"],
                },
            }
            for attr in attributes_data
        ]
        merged_response["attributes"] = processed_attributes

        maturity_levels_data = maturity_levels_response.json().get("maturityLevels", [])
        processed_maturity_levels = [
            {
                "id": lvl["id"],
                "title": lvl["title"],
                "index": lvl["index"],
                "value": lvl["value"],
            }
            for lvl in maturity_levels_data
        ]
        merged_response["maturityLevels"] = processed_maturity_levels
        return {"Success": True, "body": merged_response, "status_code": HTTPStatus.OK}

    merged_response.update(attributes_response.json())
    merged_response.update(maturity_levels_response.json())
    return {"Success": False, "body": merged_response, "status_code": HTTPStatus.BAD_REQUEST}


def approve_answer(request, assessment_id):
    response = requests.put(
    ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/approve-answer',
    json = request.data,
    headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def approve_assessment_answers(request, assessment_id):
    response = requests.put(
    ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/approve-answers',
    headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def update_assessment_mode(request, assessment_id):
    response = requests.put(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/mode',
        json=request.data,
        headers=AuthHeaderProvider(request).get_headers())
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def next_questionnaire(request, assessment_id, questionnaire_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/questionnaires/{questionnaire_id}/next',
        json=request.data,
        headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}