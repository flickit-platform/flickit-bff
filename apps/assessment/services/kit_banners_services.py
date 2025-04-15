import requests

from assessmentplatform.settings import ASSESSMENT_URL

def get_list_slider_banners(request):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/assessment-kits-banners',
        params=request.query_params,
        headers={'Accept-Language': request.headers['Accept-Language']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}
