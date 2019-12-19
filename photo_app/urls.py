
from django.contrib import admin
from django.urls import path, include

from photo_app.views import index, profile, faker, likephoto


urlpatterns = [
    path('', index, name='index'),
    # path('faker/', faker),
    path('<str:username>', profile, name='profile'),
    path('ajax/likephoto', likephoto, name='ajax.likephoto')
]
