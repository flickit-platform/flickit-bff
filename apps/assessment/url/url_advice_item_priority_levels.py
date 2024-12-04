from django.urls import path
from assessment.views import advice_item_priority_levels_views

urlpatterns = [
    path("", advice_item_priority_levels_views.AdviceItemPriorityLevelsApi.as_view()),
]
