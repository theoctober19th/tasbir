
from django.contrib import admin
from django.urls import path, include

from .views import login, logout, edit_profile, register

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile')
]
