import requests

from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider
from assessmentplatform.settings import ASSESSMENT_URL


def load_advice_item_priority_levels(request):
    response = requests.get(ASSESSMENT_URL + 'assessment-core/api/advice-item-priority-levels',
                            headers=AuthHeaderProvider(request).get_headers())
    return {"Success": True, "body": response.json(), "status_code": response.status_code}
