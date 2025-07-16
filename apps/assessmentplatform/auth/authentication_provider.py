import os
from rest_framework.permissions import AllowAny, IsAuthenticated

def get_env_based_permissions():
    use_dev_auth = os.getenv("DJANGO_DEV_AUTH", "false").lower() == "true"
    print("authentication provider ***", use_dev_auth)
    if use_dev_auth:
        return [AllowAny()]
    return [IsAuthenticated()]