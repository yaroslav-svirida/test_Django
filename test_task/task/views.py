from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from .models import User
from .serializers import UserCreateCustomSerializer


class ListUsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateCustomSerializer
