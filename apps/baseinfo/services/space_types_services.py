import requests

from assessmentplatform.settings import ASSESSMENT_URL


def load_space_types(request):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/space-types',
        headers={'Accept-Language': request.headers['Accept-Language']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}
