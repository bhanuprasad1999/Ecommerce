from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from users.serializers import *
from .models import *
import json

# Registering the new users differentiated two type of users seller and buyer.


@api_view(['POST'])
def user_register(request):
    if request.method == 'POST':
        if not User.objects.filter(username=request.data['username']).exists():
            user = User.objects.create(
                username=request.data['username'],
            )
            user.set_password(request.data['password'])
            user.save()
            profile = UserProfile.objects.create(
                user=User.objects.get(username=request.data['username']),
                user_type=request.data['user_type'],
                address=request.data['address'],
                phone_no=request.data['phone_no']
            )
            profile.save()

    return JsonResponse({'message': 'created'})


@swagger_auto_schema(method='post', request_body=UserSerializer)
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.data['username'], password=request.data['password'])
        if user is not None:
            Token.objects.create(user=User.objects.get(username=request.data['username'])).save()
            token = Token.objects.get(user_id=User.objects.get(username=request.data['username']))
            return JsonResponse({'data': json.loads(json.dumps(token, default=str)), 'message': 'successfully logged in!'})
        else:
            JsonResponse({'message': 'Please check the credentials!'})


def token_authentication(auth1):
    def auth(*args, **kwargs):
        request = args[0]
        print(request.META)
        print(request.META['HTTP_AUTHORIZATION'].split(' ')[1])
        authorized = Token.objects.filter(
            key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).exists()
        if authorized:
            return auth1(*args, **kwargs)
        else:
            return HttpResponse("<h1>Token not existed!</h1>")
    return auth


@api_view(['POST'])
@token_authentication
def logout(request):
    if request.method == 'POST':

        token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        Token.objects.get(key=token).delete()
    return JsonResponse({'message': 'logged out'})
