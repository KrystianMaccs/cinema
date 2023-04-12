from ninja import NinjaAPI
from typing import List
from apps.movies.models import Movie
from apps.movies.schema import MovieIn

api = NinjaAPI()

@api.get("/movies", response=List[MovieIn])
def tracks(request):
    return Movies.objects.all()

@api.get("/movie/{movie_id}", response={200: MovieIn,})
def movie(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        return 200, movie
    except Movie.DoesNotExist as e:
        return 404, {"message": "Could not find movie"}