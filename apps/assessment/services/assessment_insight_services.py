import requests

from assessmentplatform.settings import ASSESSMENT_URL


def create_assessment_insights(request, assessment_id):
    response = requests.post(ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/overall-insight',
                             json=request.data,
                             headers={'Authorization': request.headers['Authorization'],
                                      'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 201:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def init_assessment_insights(request, assessment_id):
    response = requests.post(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/init-insight',
        json=request.data,
        headers={'Authorization': request.headers.get('Authorization')}
    )
    if response.status_code == 201:
        return {
            "Success": True,
            "body": None,
            "status_code": response.status_code
        }
    return {
        "Success": False,
        "body": response.json(),
        "status_code": response.status_code
    }


def get_assessment_overall_insights(request, assessment_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/overall-insight',
        headers={'Authorization': request.headers.get('Authorization')}
    )
    if response.status_code != 200:
        return {
            "Success": False,
            "body": response.json(),
            "status_code": response.status_code
        }
    return {
        "Success": True,
        "body": response.json(),
        "status_code": response.status_code
    }


def get_assessment_insights(request, assessment_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/insights',
        headers={'Authorization': request.headers.get('Authorization')}
    )
    if response.status_code != 200:
        return {
            "Success": False,
            "body": response.json(),
            "status_code": response.status_code
        }
    return {
        "Success": True,
        "body": response.json(),
        "status_code": response.status_code
    }


def get_assessment_subject_insights(request, assessment_id, subject_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/subjects/{subject_id}/insight',
        headers={'Authorization': request.headers.get('Authorization')}
    )
    if response.status_code != 200:
        return {
            "Success": False,
            "body": response.json(),
            "status_code": response.status_code
        }
    return {
        "Success": True,
        "body": response.json(),
        "status_code": response.status_code
    }


def create_assessment_subject_insight(request, assessment_id, subject_id):
    response = requests.post(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/subjects/{subject_id}/insight',
        json=request.data,
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 201:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def approve_attribute_insight(request, assessment_id, attribute_id):
    response = requests.put(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/attributes/{attribute_id}/approve-insight',
        json=request.data,
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def approve_subject_insight(request, assessment_id, subject_id):
    response = requests.put(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/subjects/{subject_id}/approve-insight',
        json=request.data,
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def approve_assessment_insight(request, assessment_id):
    response = requests.put(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/approve-overall-insight',
        json=request.data,
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def create_attributes_insight(request, assessment_id, attribute_id):
    response = requests.post(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/attributes/{attribute_id}/insight',
        json=request.data,
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 201:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def create_attributes_ai_insight(request, assessment_id, attribute_id):
    response = requests.post(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/attributes/{attribute_id}/ai-insight',
        json=request.data,
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}


def get_assessment_attribute_insight(request, assessment_id, attribute_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/attributes/{attribute_id}/insight',
        headers={'Authorization': request.headers.get('Authorization')}
    )

    if response.status_code != 200:
        return {
            "Success": False,
            "body": response.json(),
            "status_code": response.status_code
        }
    return {
        "Success": True,
        "body": response.json(),
        "status_code": response.status_code
    }


def init_subject_insight(request, assessment_id, subject_id):
    response = requests.post(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/subjects/{subject_id}/init-insight',
        json=request.data,
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 201:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def init_assessment_insight(request, assessment_id):
    response = requests.post(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/init-overall-insight',
        json=request.data,
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 201:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def approve_all_assessment_insights(request, assessment_id):
    response = requests.put(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/approve-insights',
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def generate_all_assessment_insights(request, assessment_id):
    response = requests.put(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/generate-insights',
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def regenerate_expired_assessment_insights(request, assessment_id):
    response = requests.put(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/regenerate-expired-insights',
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}


def approve_expired_assessment_insights(request, assessment_id):
    response = requests.put(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/approve-expired-insights',
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 200:
        return {"Success": True, "body": None, "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}

