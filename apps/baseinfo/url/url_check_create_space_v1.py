from django.urls import path

from baseinfo.views import check_create_space_views

urlpatterns = [
    path("", check_create_space_views.Checkcreatespaceview.as_view())
]
