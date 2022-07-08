from django.urls import path

from .short_view import ShortView
from .views import ListUsersView


urlpatterns = [
    path('users/', ListUsersView.as_view()),
    path('short/get/', ShortView.as_view()),

]