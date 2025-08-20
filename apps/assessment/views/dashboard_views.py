from rest_framework.views import APIView
from rest_framework.response import Response

from assessment.services import dashboar_services
from assessmentplatform.auth.authentication_provider import authenticate


class AssessmentDashboardApi(APIView):
    authenticate()

    def get(self, request, assessment_id):
        result = dashboar_services.load_assessment_dashboard(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])
