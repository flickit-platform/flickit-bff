from django.urls import path

from baseinfo.views import assessmentkitviews

urlpatterns = [
        path("<str:assessment_kit_id>/info/",assessmentkitviews.LoadAssessmentKitInfoEditableApi.as_view())
            
            ,]