from django.urls import path

from account.views.tenant_views import TenantApi

urlpatterns = [
    path("", TenantApi.as_view()),
]
