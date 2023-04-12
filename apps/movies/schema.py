from datetime import datetime
from django.http import Http404
from ninja import Schema
from .models import Movie

class MovieIn(Schema):
    name: str
    protagonists: str
    poster: str
    start_date: datetime
    status: str
    ranking: int
