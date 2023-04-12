from ninja import Router
from .models import Movie
from .schemas import MovieIn

movies_router = Router()

@movies_router.post("/")
def add_movie(request, movie: MovieIn):
    movie_obj = Movie(**movie.dict())
    movie_obj.save()
    return {"message": "Movie added successfully"}

