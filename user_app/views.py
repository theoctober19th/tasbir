from django.shortcuts import render

# Create your views here.
def display(request):
    return render(request, 'user_app/display.html')

def index(request):
    return render(request, 'user_app/index.html')