import requests
from assessmentplatform.settings import ASSESSMENT_URL


def get_tenant(request):
    response = requests.get(
        ASSESSMENT_URL + 'assessment-core/api/tenant',
        headers={'Accept-Language': request.headers['Accept-Language']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}
