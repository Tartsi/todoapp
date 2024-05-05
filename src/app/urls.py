from django.urls import path
from django.contrib.auth.views import logout_then_login
from .views import login, register_view, add_user, login_view, listings_view

urlpatterns = [
    path('', login, name='login'),
    path('register_view', register_view, name='register_view'),
    path('add_user', add_user, name='add_user'),
    path('login_view', login_view, name='login_view'),
    path('listings_view', listings_view, name='listings_view'),
    path('logout', logout_then_login, name='logout'),
]
