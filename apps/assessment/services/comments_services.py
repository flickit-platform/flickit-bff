import requests

from assessmentplatform.settings import ASSESSMENT_URL


def get_list_comments(request):
    response = requests.get(
        ASSESSMENT_URL + f'assessment-core/api/comments',
        params=request.query_params,
        headers={'Authorization': request.headers['Authorization'],
                 'Accept-Language': request.headers['Accept-Language']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}