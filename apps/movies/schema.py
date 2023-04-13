from datetime import datetime
from django.http import Http404
from ninja import ModelSchema
from .models import Movie


class MovieSchema(ModelSchema):
    class Config:
        model = Movie
        model_fields = ['id', 'name', 'protagonists', 'poster', 'start_date', 'status', 'ranking']
    
   
