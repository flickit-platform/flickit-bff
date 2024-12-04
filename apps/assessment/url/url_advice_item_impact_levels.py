from django.urls import path
from assessment.views import advice_item_impact_levels_views

urlpatterns = [
    path("", advice_item_impact_levels_views.AdviceItemImpactLevelsApi.as_view()),
]
