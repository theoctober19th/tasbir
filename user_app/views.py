from django.shortcuts import render, redirect
from .models import UserModel
from .forms import RegisterForm, EditProfileForm

# Create your views here.
def login(request):
    if 'user_id' in request.session:
        return redirect('index')
    
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
            form = EditProfileForm(request.POST, files=request.FILES, instance=user)
            print(form.errors)
            form.save()
            
            request.session['username'] = user.username
            return redirect('profile', user.username)

        else:
            form = EditProfileForm(instance=user)
            d = {
                'user' : user,
                'form': form
            }
            return render(request, 'user_app/edit_profile.html', d)
    else:
        return render(request, 'photo_app/404.html')
        
def register(request):
    if 'user_id' in request.session:
        return redirect('index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
            return render(request, 'user_app/register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'user_app/register.html', {'form': form})