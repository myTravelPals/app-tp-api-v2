# third party
from ninja.security import HttpBearer
# local
from .models import APIKey

class APIKeyAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            api_key = APIKey.objects.get(key=token)
            request.api_key = api_key
            return api_key
        except APIKey.DoesNotExist:
            return None