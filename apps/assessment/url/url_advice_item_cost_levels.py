from django.urls import path
from assessment.views import advice_item_cost_levels_views

urlpatterns = [
    path("", advice_item_cost_levels_views.AdviceItemCostLevelsApi.as_view()),
]
