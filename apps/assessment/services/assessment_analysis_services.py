import requests
from django.conf import settings

from assessmentplatform.auth.auth_header_provider import AuthHeaderProvider


def upload_analysis_file(request, assessment_id):
    file = request.data.get('inputFile')
    data = request.data.copy()
    data.pop('inputFile')

    url = f"{settings.ASSESSMENT_URL}assessment-core/api/assessments/{assessment_id}/analysis-input"
    response = requests.post(
        url,
        data=data,
        files={'inputFile': (file.name, file, file.content_type)},
        headers=AuthHeaderProvider(request).get_headers()
    )
    return {"Success": True, "body": response.json(), "status_code": response.status_code}
