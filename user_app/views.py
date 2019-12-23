from django.shortcuts import render, redirect
from .models import UserModel

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)

        user = UserModel.objects.filter(username=username, password=password).first()
        print(user)

        if not user:
            return redirect('login')
        else:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['display_name'] = user.display_name
            return redirect('index')
    else:
        return render(request, 'user_app/login.html')

def logout(request):
    request.session.flush()
    return redirect('login')

def edit_profile(request):
    if 'user_id' not in request.session:
        return redirect('login')
    userid = request.session.get('user_id')
    user = UserModel.objects.filter(id=userid).first()
    if user:
        if request.method == 'POST':
            user.display_name = request.POST.get('display_name')
            user.username = request.POST.get('username')
            user.website = request.POST.get('website')
            user.bio = request.POST.get('bio')
            user.email = request.POST.get('email')
            user.save()
            request.session['username'] = user.username
            return redirect('profile', user.username)

        else:
            d = {
                'user' : user
            }
            return render(request, 'user_app/edit_profile.html', d)
    else:
        return render(request, 'photo_app/404.html')
        