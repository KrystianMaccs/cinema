from datetime import datetime, timedelta
from celery import Celery, shared_task
from .models import Movie
from .schema import MovieIn
from cinema.utils import get_db_handle, get_collection_handle

app = Celery("movies")


@shared_task
def sync_movie_to_mongodb(movie_id):
    # Define MongoDB connection details
    host = 'mongodb_host'
    port = 27017
    username = 'mongodb_username'
    password = 'mongodb_password'
    db_name = 'cinema'

    # Connect to MongoDB
    db_handle, client = get_db_handle(db_name, host, port, username, password)
    movie_collection = get_collection_handle(db_handle, 'movies')

    # Get the movie object by id
    movie = Movie.objects.get(id=movie_id)

    # Create a MongoDB document from the movie object
    movie_document = {
        'id': movie.id,
        'name': movie.name,
        'protagonists': movie.protagonists,
        'poster': movie.poster,
        'start_date': movie.release_date.isoformat(),
        'ranking': movie.ranking
    }

    # Upsert the movie document in the movies collection
    movie_collection.update_one({'id': movie.id}, {'$set': movie_document}, upsert=True)

    # Close the MongoDB connection
    client.close()

    return "Movie synced to MongoDB successfully"



@shared_task
def update_movie_rank():
    # Get all the upcoming movies
    upcoming_movies = Movie.objects.filter(status='upcoming')

    # Check if any of the upcoming movies have a release date less than or equal to the current time
    for movie in upcoming_movies:
        start_time = datetime.combine(movie.start_date, datetime.min.time())
        if start_time <= datetime.now():
            # Update the movie status and rank
            movie.status = 'running'
            movie.ranking += 10
            movie.save()

    return "Movie ranks updated successfully"


movie = Movie.objects.first()
# app.conf.beat_schedule = {
#    'sync-movies-to-mongodb-every-5-minutes': {
#       'task': 'movies.tasks.sync_movie_to_mongodb',
#       'schedule': 300.0,
#       'args': [MovieIn.from_orm(movie).dict(), 'update'] # pass a dictionary representing the movie object here
#   },
# }
