from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from .models import *


class UserCreateCustomSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email', 'first_name', 'last_name', 'password')

class ShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ("long_url", "short_url", "user_id")
