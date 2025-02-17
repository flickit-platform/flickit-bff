import requests

from assessmentplatform.settings import ASSESSMENT_URL


def load_kit_languages(request):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/kit-languages',
        headers={'Accept-Language': request.headers['Accept-Language']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}
