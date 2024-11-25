from django.urls import path

from baseinfo.views import kit_custom_views

urlpatterns = [
    path("<str:custom_kit_id>/", kit_custom_views.KitCustomApi.as_view())
    ]