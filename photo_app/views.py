from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import PhotoModel
from user_app.models import UserModel
from django.views.decorators.csrf import csrf_exempt

from faker import Faker

# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        return redirect('login')
    else:
        posts = PhotoModel.objects.order_by('-timestamp')
        return render(request, 'photo_app/index.html', {'posts':posts} )

def profile(request, username):
    user = UserModel.objects.filter(username=username).first()

    if user is None:
        return render(request, 'photo_app/404.html')
        
    posts = PhotoModel.objects.filter(uploaded_by = user).order_by('-timestamp')
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'photo_app/profile.html', context)

@csrf_exempt
def likephoto(request):
    print('server side ajax function called')
    return JsonResponse({'success': 'true'})

def faker(request):
    fake = Faker()
    for i in range(5):
        name = fake.name()
        username = fake.user_name()
        password = fake.password()
        email = fake.email()
        website = fake.url()
        profile_pic = 'profile.jpg'
        bio = fake.sentence()

        user = UserModel(display_name=name, username=username, 
                    password=password, email=email,
                    website=website, profile_pic=profile_pic,
                    bio=bio)
        user.save(force_insert=True)

        for j in range(5):
            photo = 'feedPhoto.jpg'
            likes = fake.random_digit()
            location = fake.city()
            post = PhotoModel(likes = likes,
                            location=location,
                            photo=photo,
                            uploaded_by=user)
            post.save(force_insert=True)

    return HttpResponse('Fake Data created successfully')
