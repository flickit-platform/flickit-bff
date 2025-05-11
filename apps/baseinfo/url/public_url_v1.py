from django.urls import path

from assessment.views import assessment_report_views
from baseinfo.views import assessment_kit_views

urlpatterns = [
    path("graphical-report/<uuid:link_hash>/", assessment_report_views.PublicGraphicalReportApi.as_view()),
    path("assessment-kits/<str:assessment_kit_id>", assessment_kit_views.PublicAssessmentKitApi.as_view()),
]