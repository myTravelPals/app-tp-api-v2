# system
import secrets

def create_api_token(length=32):
    """Generate a secure API token."""
    return secrets.token_hex(length)