from ninja import NinjaAPI
from landing_page.api import router as landing_page_router
api = NinjaAPI()

api.add_router("/landing_page/", landing_page_router)