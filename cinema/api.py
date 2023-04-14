from ninja import NinjaAPI
from apps.movies.api import router as movies_router
from apps.users.api import api as users_api

api = NinjaAPI()
api.add_router("/movies/", movies_router)
# users_api.add_router("/users/", users_api)