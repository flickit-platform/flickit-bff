from django.urls import path
from assessment.views import comments_views

urlpatterns = [
    path("", comments_views.CommentsApi.as_view())
]
