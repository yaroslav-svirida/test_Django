from djoser.serializers import UserCreateSerializer

from .models import User


class UserCreateCustomSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email', 'first_name', 'last_name', 'password')
