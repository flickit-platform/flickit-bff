from django.urls import path

from assessment.views import assessment_report_views

urlpatterns = [
    path("graphical-report/<uuid:link_hash>/", assessment_report_views.PublicGraphicalReportApi.as_view()),
]