from django.urls import path
from .views import index, register, add_user, login_user

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('add_user', add_user, name='add_user'),
    path('login_user', login_user, name='login_user'),
]
