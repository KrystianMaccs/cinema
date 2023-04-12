from ninja import Router
from .views import add_movie

movies_router = Router()
movies_router.add_router("POST", add_movie)

api_router = Router()
api_router.add_router("/movies", movies_router)
