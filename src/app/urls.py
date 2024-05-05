from django.urls import path
from django.contrib.auth.views import logout_then_login
from .views import index, register, add_user, login_user, listings_view

urlpatterns = [
    path('', index, name='login'),
    path('register', register, name='register'),
    path('add_user', add_user, name='add_user'),
    path('login_user', login_user, name='login_user'),
    path('listings', listings_view, name='listings'),
    path('logout', logout_then_login, name='logout'),
]
