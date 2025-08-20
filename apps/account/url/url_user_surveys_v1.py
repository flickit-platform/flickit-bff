from django.urls import path

from account.views.user_survey_views import UserSurveysApi

urlpatterns = [
    path("dont-show-again/", UserSurveysApi.as_view())
]
