from django.urls import path
from assessment.views import advice_views

urlpatterns = [
    path("", advice_views.AdviceItemsApi.as_view()),
    path("<uuid:advice_item_id>/", advice_views.AdviceItemApi.as_view()),
]