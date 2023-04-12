from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': config('POSTGRES_HOST'),
        'NAME': config('POSTGRES_NAME'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'PORT': config('POSTGRES_PORT'),

    },
    "nonrel": {
        "ENGINE": "djongo",
        "NAME": config('MONGO_DB_NAME'),
        "CLIENT": {
            "host": config('MONGO_DB_HOST'),
            "port": int(config('MONGO_DB_PORT')),
            "username": config('MONGO_DB_USERNAME'),
            "password": config('MONGO_DB_PASSWORD'),
        },
        'TEST': {
            'MIRROR': 'default',
        },
    }
}