from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from assessment.services import attribute_measure_services


class AssessmentAttributeMeasuresApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, assessment_id, attribute_id):
        result = attribute_measure_services.get_list_measures(request, assessment_id, attribute_id)
        return Response(result["body"], result["status_code"])
