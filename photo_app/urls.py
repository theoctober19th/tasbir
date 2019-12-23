
from django.contrib import admin
from django.urls import path, include

from photo_app.views import index, profile, faker, ajaxcomment, ajaxlike, explore, search, followers, followings, detail


urlpatterns = [
    path('', index, name='index'),
    # path('faker/', faker),
    path('search/', search, name='search'),
    path('explore/', explore, name='explore'),
    path('posts/<int:postid>', detail, name='detail'),
    path('<str:username>/followers', followers, name='followers'),
    path('<str:username>/followings', followings, name='followings'),
    path('ajax/likephoto/', ajaxlike, name='ajax.likephoto'),
    path('ajax/comment/', ajaxcomment, name='ajax.comment'),

    path('<str:username>/', profile, name='profile'),
]
