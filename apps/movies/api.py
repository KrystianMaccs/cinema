from ninja import NinjaAPI
from typing import List
from apps.movies.models import Movie
from apps.movies.schema import MovieIn
from apps.movies.tasks import sync_movie_to_mongodb

api = NinjaAPI()

@api.get("/movies", response=List[MovieIn])
def movies(request):
    return Movie.objects.all()

@api.get("/movie/{movie_id}", response={200: MovieIn,})
def movie(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        return 200, movie
    except Movie.DoesNotExist as e:
        return 404, {"message": "Could not find movie"}


@api.post("/movies/")
def add_movie(request, movie: MovieIn):
    movie_obj = Movie(**movie.dict())
    movie_obj.save()
    sync_movie_to_mongodb.delay(movie_obj.id)  # Call the Celery task asynchronously
    return {"message": "Movie added successfully"}

@api.put("/movies/{movie_id}")
def update_movie(request, movie_id: int, movie: MovieIn):
    movie_obj = Movie.objects.filter(id=movie_id).update(**movie.dict())
    sync_movie_to_mongodb.delay(movie_id)  # Call the Celery task asynchronously
    return {"message": "Movie updated successfully"}

@api.delete("/movies/{movie_id}")
def delete_movie(request, movie_id: int):
    try:
        movie_obj = Movie.objects.get(id=movie_id)
        movie_obj.delete()
        sync_movie_to_mongodb.delay(movie_id)  # Call the Celery task asynchronously
        return {"message": "Movie deleted successfully"}
    except Movie.DoesNotExist:
        return {"message": "Movie does not exist"}, status.HTTP_404_NOT_FOUND
