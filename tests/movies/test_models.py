import pytest
from django.utils import timezone
from mixer.backend.django import mixer
from apps.movies.models import Movie


@pytest.fixture
def movie():
    return mixer.blend(
        Movie,
        name='The Dark Knight',
        protagonists='Batman, Joker',
        poster='/path/to/poster',
        start_date=timezone.now(),
        status='ST',
        ranking=5,
    )


@pytest.mark.django_db
def test_movie_str_method(movie):
    assert str(movie) == 'The Dark Knight'


@pytest.mark.django_db
def test_movie_model_fields(movie):
    assert movie.name == 'The Dark Knight'
    assert movie.protagonists == 'Batman, Joker'
    assert movie.poster == '/path/to/poster'
    assert isinstance(movie.start_date, timezone.datetime)
    assert movie.status == 'ST'
    assert movie.ranking == 5
