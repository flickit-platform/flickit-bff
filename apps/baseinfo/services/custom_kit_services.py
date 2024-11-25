import requests
from assessmentplatform.settings import ASSESSMENT_URL


def create_custom_kit(request, kit_id):
    data = dict(request.data)
    data['kitId'] = kit_id
    response = requests.post(
        ASSESSMENT_URL + 'assessment-core/api/kit-customs',
        json=data,
        headers={'Authorization': request.headers['Authorization']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}
