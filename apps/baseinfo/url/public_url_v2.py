from django.urls import path
from baseinfo.views import assessment_kit_views

urlpatterns = [
    path("assessment-kits/", assessment_kit_views.PublicAssessmentKitsApi.as_view()),
]