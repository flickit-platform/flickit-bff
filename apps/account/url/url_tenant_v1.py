from django.urls import path

from account.views.tenant_views import TenantInfoApi, TenantLogoApi, TenantApi

urlpatterns = [
    path("info/", TenantInfoApi.as_view()),
    path("logo/", TenantLogoApi.as_view()),
    path("", TenantApi.as_view()),
]
