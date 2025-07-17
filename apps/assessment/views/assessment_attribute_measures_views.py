from rest_framework.response import Response
from rest_framework.views import APIView

from assessment.services import attribute_measure_services
from assessmentplatform.auth.authentication_provider import authenticate


class AssessmentAttributeMeasuresApi(APIView):
    authenticate()

    def get(self, request, assessment_id, attribute_id):
        result = attribute_measure_services.get_list_measures(request, assessment_id, attribute_id)
        return Response(result["body"], result["status_code"])
