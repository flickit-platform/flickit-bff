import requests

from assessmentplatform.settings import ASSESSMENT_URL


def load_assessment_dashboard(request, assessment_id):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessments/{assessment_id}/dashboard',
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}
