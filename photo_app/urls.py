
from django.contrib import admin
from django.urls import path, include

from photo_app import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('faker/', faker),
    path('search/', views.search, name='search'),
    path('explore/', views.explore, name='explore'),
    path('posts/<int:postid>', views.detail, name='detail'),
    path('delete/<int:postid>', views.delete_photo, name='delete'),
    path('<str:username>/followers', views.followers, name='followers'),
    path('<str:username>/followings', views.followings, name='followings'),
    path('ajax/likephoto/', views.ajaxlike, name='ajax.likephoto'),
    path('ajax/comment/', views.ajaxcomment, name='ajax.comment'),
    path('add/', views.addphoto, name='add-photo'),
    path('ajax/follow/', views.ajaxfollow, name='ajax.follow'),
    path('<str:username>/', views.profile, name='profile'),
]
