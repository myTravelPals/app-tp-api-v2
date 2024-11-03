# third party
from ninja import NinjaAPI
# local
from api_auth.api import APIKeyAuth
from landing_page.api import router as landing_page_router


api = NinjaAPI(auth=APIKeyAuth())

api.add_router("/landing_page/", landing_page_router)