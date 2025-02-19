from django.urls import path

from baseinfo.views import space_types_views

urlpatterns = [
    path("", space_types_views.SpaceTypesView.as_view())
]
