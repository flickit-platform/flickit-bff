from django.urls import path

from baseinfo.views import kit_language_views

urlpatterns = [
    path("", kit_language_views.KitLanguageViews.as_view())
]
