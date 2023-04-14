import pytest
from datetime import datetime, timedelta
from unittest import mock
from pymongo import MongoClient
from bson import ObjectId

from movies.models import Movie
from movies.schema import MovieSchema
from movies.tasks import (
    get_trending_movies,
    sync_movie_to_mongodb,
    update_movie_rank,
)

# Mock movie data
movie_data = {
    'id': ObjectId(),
    'name': 'Test Movie',
    'protagonists': ['Test Protagonist'],
    'poster': 'https://test.com/test.jpg',
    'start_date': datetime.now(),
    'ranking': 0,
}

# Set up test database
@pytest.fixture(scope='session')
def mongo():
    mongo_client = MongoClient()
    db = mongo_client['test_db']
    yield db
    mongo_client.drop_database('test_db')

# Test get_trending_movies task
def test_get_trending_movies(mongo):
    # Insert test data into MongoDB
    movie_collection = mongo['movies']
    movie_collection.insert_many([
        {'id': ObjectId(), 'name': 'Test Movie 1', 'status': 'running', 'ranking': 10},
        {'id': ObjectId(), 'name': 'Test Movie 2', 'status': 'running', 'ranking': 20},
        {'id': ObjectId(), 'name': 'Test Movie 3', 'status': 'running', 'ranking': 30},
        {'id': ObjectId(), 'name': 'Test Movie 4', 'status': 'upcoming', 'ranking': 40},
    ])

    # Execute task
    trending_movies = get_trending_movies()

    # Check if returned list contains 10 movies
    assert len(trending_movies) == 3

    # Check if returned movies are sorted by ranking in descending order
    assert trending_movies[0]['name'] == 'Test Movie 3'
    assert trending_movies[1]['name'] == 'Test Movie 2'
    assert trending_movies[2]['name'] == 'Test Movie 1'

# Test sync_movie_to_mongodb task
def test_sync_movie_to_mongodb(mongo):
    # Create mock Movie object
    movie = Movie(**movie_data)
    movie.save()

    # Execute task
    sync_movie_to_mongodb(str(movie.id))

    # Check if movie was synced to MongoDB
    movie_document = mongo['movies'].find_one({'id': str(movie.id)})
    assert movie_document is not None
    assert movie_document['name'] == movie_data['name']
    assert movie_document['protagonists'] == movie_data['protagonists']
    assert movie_document['poster'] == movie_data['poster']
    assert movie_document['start_date'] == movie_data['start_date'].isoformat()
    assert movie_document['ranking'] == movie_data['ranking']

# Test update_movie_rank task
def test_update_movie_rank(mongo):
    # Create mock Movie objects
    upcoming_movies = [
        Movie(**{**movie_data, 'status': 'upcoming', 'ranking': 0}),
        Movie(**{**movie_data, 'status': 'upcoming', 'ranking': 0}),
        Movie(**{**movie_data, 'status': 'upcoming', 'ranking': 0}),
    ]
    for movie in upcoming_movies:
        movie.save()

    # Mock current datetime to be 5 minutes after start_date of the first movie
    with mock.patch('movies.tasks.datetime') as mock_datetime:
        mock_datetime.now.return_value = datetime.combine(upcoming_movies[0].start_date, datetime.min.time()) + timedelta(minutes=5)

        # Execute task
       
