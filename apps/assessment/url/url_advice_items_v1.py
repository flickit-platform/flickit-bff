from django.urls import path
from assessment.views import advice_views

urlpatterns = [
    path("", advice_views.AdviceItemsApi.as_view()),
]