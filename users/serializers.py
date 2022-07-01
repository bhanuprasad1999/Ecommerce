from rest_framework import serializers
from django.contrib.auth.models import User

from users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = UserProfile
        fields = ['user', 'user_type', 'address', 'phone_no']
