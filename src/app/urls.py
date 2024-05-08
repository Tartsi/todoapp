from django.urls import path
from django.contrib.auth.views import logout_then_login
from .views import delete_task, login, register_view, add_user, login_view, listings_view, add_task, clear_listed_task, clear_completed_task

urlpatterns = [
    path('', login, name='login'),
    path('register_view', register_view, name='register_view'),
    path('add_user', add_user, name='add_user'),
    path('login_view', login_view, name='login_view'),
    path('listings_view', listings_view, name='listings_view'),
    path('logout', logout_then_login, name='logout'),
    path('add_task', add_task, name='add_task'),
    path('clear_listed_task', clear_listed_task, name='clear_listed_tasks'),
    path('delete_task', delete_task, name='delete_task'),
    path('clear_completed_task', clear_completed_task,
         name='clear_completed_tasks'),
]
