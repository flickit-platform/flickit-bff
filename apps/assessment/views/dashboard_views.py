from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from assessment.services import dashboar_services


class AssessmentDashboardApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, assessment_id):
        result = dashboar_services.load_assessment_dashboard(request, assessment_id)
        return Response(data=result["body"], status=result["status_code"])
