import requests
from assessmentplatform.settings import ASSESSMENT_URL


def load_advice_item_cost_levels(request):
    response = requests.get(ASSESSMENT_URL + 'assessment-core/api/advice-item-cost-levels',
                            headers={'Authorization': request.headers['Authorization']})
    return {"Success": True, "body": response.json(), "status_code": response.status_code}
