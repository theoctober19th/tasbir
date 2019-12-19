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