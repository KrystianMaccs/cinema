from ninja import NinjaAPI
from apps.movies.api import router as movies_router

api = NinjaAPI()
api.add_router("/movies/", movies_router)