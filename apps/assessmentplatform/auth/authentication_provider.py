import os
from django.conf import settings
from rest_framework.permissions import AllowAny, IsAuthenticated

def authenticate():
    env_value = os.getenv("DJANGO_DEV_AUTH")
    if env_value is not None:
        use_dev_auth = env_value.lower() == "true"
    else:
        use_dev_auth = getattr(settings, "DJANGO_DEV_AUTH", False)

    return [AllowAny()] if use_dev_auth else [IsAuthenticated()]
