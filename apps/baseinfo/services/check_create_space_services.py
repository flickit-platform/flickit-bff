import requests
from assessmentplatform.settings import ASSESSMENT_URL


def check_allowance(request):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/check-create-space',
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    if response.status_code == 200:
        return {"Success": True, "body": response.json(), "status_code": response.status_code}
    return {"Success": False, "body": response.json(), "status_code": response.status_code}
