from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.



def index(request):
    selected_theme = request.session.get('selected_theme', 'default')

    # Render the corresponding theme template
    if selected_theme == "christmas":
        return render(request, "christmas.html")
    elif selected_theme == "onam":
        return render(request, "onam_theme.html")
    else:
        # Fallback to a default theme if no theme is selected
       
    
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
#     if request.method == 'POST':
#         theme = request.POST.get('theme', 'default')
#         request.session['selected_theme'] = theme
#         return redirect('index')  # Redirect to the home page after theme selection

def update_theme(request):
    if request.method == 'POST':
        theme = request.POST.get('theme', 'default')
        request.session['selected_theme'] = theme

        # Assuming 'index' is the view for rendering the main page
        # You may need to replace this with the actual view name you use for your home page
        return redirect('index')  # Redirect to the home page after theme selection



def christmas(request):
    
    return render(request, 'christmas.html')