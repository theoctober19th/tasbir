
from django.contrib import admin
from django.urls import path, include

from photo_app.views import index, profile


urlpatterns = [
    path('', index, name='index'),
    path('<str:username>', profile, name='profile')
]
