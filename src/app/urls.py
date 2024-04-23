from django.urls import path
from .views import index, register, add_user

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('add_user/', add_user, name='add_user'),
]
