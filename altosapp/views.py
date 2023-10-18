from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.



def index(request):
    
    return render(request, 'index.html')

def base(request):
    
    return render(request, 'base.html')
def home(request):
    
    return render(request, 'home.html')



def aha(request):
    
    return render(request, 'aha.html')

def adminhome(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render(request, 'adminhome.html')

def adminlog(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('adminhome')
            else:
                login(request, user)
                messages.info(request, f'Welcome {username}')
                return redirect('userhome')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('/')
    return render(request, 'index.html')

# def update_theme(request):
#     user_id = request.POST['user_id']
#     theme = request.POST['theme']

#     user_profile, created = UserProfile.objects.get_or_create(user_id=user_id)
#     user_profile.selected_theme = theme
#     user_profile.save()

#     return redirect('home')

def update_theme(request):
    if request.method == 'POST':
        theme = request.POST.get('theme', 'default')
        request.session['selected_theme'] = theme
        return redirect('index')  # Redirect to the home page after theme selection


