from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.



def home(request):
    
    return render(request, 'home.html')

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
    return render(request, 'home.html')