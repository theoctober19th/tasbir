from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import PhotoModel, CommentModel
from user_app.models import UserModel
from django.views.decorators.csrf import csrf_exempt

from faker import Faker

# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        return redirect('login')

    userid = request.session.get('user_id', None)
    user = UserModel.objects.filter(id=userid).first()
    posts = PhotoModel.objects.filter(uploaded_by__in = user.followings.all()).order_by('-timestamp')
    return render(request, 'photo_app/index.html', {'posts':posts, 'user':user})

def profile(request, username):
    user = UserModel.objects.filter(username=username).first()

    if user is None:
        return render(request, 'photo_app/404.html')
        
    posts = PhotoModel.objects.filter(uploaded_by = user).order_by('-timestamp')[:10]
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'photo_app/profile.html', context)

@csrf_exempt
def ajaxlike(request):
    if 'user_id' not in request.session:
        return redirect('login')

    userid = request.session.get('user_id', None)
    postid = request.POST.get('postid', None)

    if postid and userid:
        post = PhotoModel.objects.filter(id=postid).first()
        user = UserModel.objects.filter(id=userid).first()
        if post and user:
            if post.liked_by.filter(id=userid):
                post.liked_by.remove(user)
                print('Now Disliked')
                return JsonResponse({'success': 'true', 'action':'disliked'})
            else:
                post.liked_by.add(user)
                print('Now Liked')
                return JsonResponse({'success': 'true', 'action':'liked'})
    #print('server side ajax function called', postid)
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
            location = fake.city()
            post = PhotoModel(
                            location=location,
                            photo=photo,
                            uploaded_by=user)
            post.save(force_insert=True)

            for k in range(3):
                text = fake.sentence()
                comment = CommentModel(commented_by=user, text=text, parent_post=post)
                comment.save(force_insert=True)
    return HttpResponse('Fake Data created successfully')

@csrf_exempt
def ajaxcomment(request):
    if 'user_id' not in request.session:
        return redirect('login')

    userid = request.session.get('user_id', None)

    if request.method == 'POST':
        postid = request.POST.get('postid', None)
        comment_text = request.POST.get('text', None)
        
        if userid and postid and comment_text:
            post = PhotoModel.objects.filter(id=postid).first()
            user = UserModel.objects.filter(id=userid).first()
            comment = CommentModel(commented_by=user, text=comment_text, parent_post=post)
            print(post, user, comment)
            comment.save()
            return JsonResponse({'success': 'true', 'status':'comment added'})
    return JsonResponse({'success':'false'})


def search(request):
    if 'user_id' not in request.session:
        return redirect('login')

    userid = request.session.get('user_id', None)
    
    if request.method == 'GET':
        query = request.GET.get('q', None)
        if query:
            d = {
                'profiles': UserModel.objects.filter(username__icontains=query).exclude(id=userid),
                'query': query
            }
            return render(request, 'photo_app/search_results.html', d)
        else:
            return redirect('index')    
    else:
        return redirect('index')


def explore(request):
    if 'user_id' not in request.session:
        return redirect('login')

    userid = request.session.get('user_id', None)
    user = UserModel.objects.filter(id=userid).first()
    recommendations = UserModel.objects.exclude(id__in=user.followings.all()).exclude(id=userid)
    context = {
        'profiles': recommendations
    }
    return render(request, 'photo_app/explore.html', context)


def followers(request, username):
    user = UserModel.objects.filter(username=username).first()
    if user:
        followers_list = user.followers.all()
        context = {'profiles': followers_list, 'username': username}
        return render(request, 'photo_app/followers.html', context)
    else:
        return render(request, 'photo_app/404.html')


def followings(request, username):
    user = UserModel.objects.filter(username=username).first()
    if user:
        followings_list = user.followings.all()
        context = {'profiles': followings_list, 'username': username}
        return render(request, 'photo_app/followings.html', context)
    else:
        return render(request, 'photo_app/404.html')

def detail(request, postid):
    photo = PhotoModel.objects.filter(id=postid).first()
    if photo:
        context = {
            'post': photo
        }
        return render(request, 'photo_app/post_detail.html', context)
    else:
        return render(request, 'photo_app/404.html')