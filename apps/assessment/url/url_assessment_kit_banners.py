from django.urls import path
from assessment.views.kit_banners_view import AssessmentKitBannersApi

urlpatterns = [
    path("", AssessmentKitBannersApi.as_view()),
]
