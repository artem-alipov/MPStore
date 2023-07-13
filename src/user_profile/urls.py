from django.urls import path
from django.contrib.auth import views
from django.urls import path, include
from . import views


app_name = 'profile'

urlpatterns = [
    path("view/", views.get_profile, name='profile_view'),
    path("edit/", views.profile, name='profile_edit'),
]