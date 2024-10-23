# system
import os
# django
from django.core.exceptions import ImproperlyConfigured
# third party
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ENVS = ["local", "prod"]
env = os.environ.get("ENV")

if env not in ENVS:
    error_message = f"The current 'ENV' is {env} but must be one of {ENVS}"
    raise ImproperlyConfigured(error_message)

if env == "prod":
    from .prod import *
elif env == "local":
    from .local import *