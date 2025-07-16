from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import AnonymousUser, User

class DevMockAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Return a dummy user without checking any headers or tokens
        user = User(username="devuser")
        user.pk = 1
        user.is_staff = True
        user.is_superuser = True
        # Note: is_authenticated is a property, no need to set it manually
        return (user, None)
