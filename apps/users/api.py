from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from ninja import NinjaAPI, Schema
from ninja.errors import HttpError
from ninja.security import django_auth
from .schema import UserSchema


api = NinjaAPI(auth=django_auth)


@api.post('/login', auth=None)
@csrf_exempt
def login(request, payload: UserSchema):
    user = auth.authenticate(request, username=payload.username, password=payload.password)
    if not user:
        raise HttpError(400, 'invalid username or password')
    auth.login(request, user)
    return {'success': True}


@api.post('/register', auth=None)
def register(request, payload: UserSchema):
    user = auth.models.User.objects.create_user(
        email=payload.email,
        username=payload.username,
        first_name=payload.first_name,
        last_name=payload.last_name,
        password=payload.password
    )
    auth.login(request, user)
    return {'success': True}


@api.post('/logout')
def logout(request):
    auth.logout(request)
    return {'success': True}
