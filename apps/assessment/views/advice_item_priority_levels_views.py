from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from assessment.services import advice_item_priority_levels_services


class AdviceItemPriorityLevelsApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = advice_item_priority_levels_services.load_advice_item_priority_levels(request)
        return Response(result["body"], result["status_code"])
