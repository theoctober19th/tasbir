from django.shortcuts import render
from django.http import HttpResponse
from .models import PhotoModel
from user_app.models import UserModel

# Create your views here.
def index(request):
    posts = PhotoModel.objects.order_by('-timestamp')
    return render(request, 'photo_app/index.html', {'posts':posts} )

def profile(request, username):
    user = UserModel.objects.filter(username=username).first()
    posts = PhotoModel.objects.filter(uploaded_by = user).order_by('-timestamp')
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'photo_app/profile.html', context)
