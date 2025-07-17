from rest_framework.views import APIView
from rest_framework.response import Response

from assessment.services import advice_item_cost_levels_services
from assessmentplatform.auth.authentication_provider import authenticate


class AdviceItemCostLevelsApi(APIView):
    authenticate()

    def get(self, request):
        result = advice_item_cost_levels_services.load_advice_item_cost_levels(request)
        return Response(result["body"], result["status_code"])
