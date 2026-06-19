from asyncio.log import logger

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def register(request):
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return HttpResponse("Passwords do not match.")
        
        User.objects.create_user(username=username,
                                 email=email,
                                 password=password,
                                 )
        
        print("User created successfully.")
        return redirect('login')
    

        
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if len(password) < 8:
            return HttpResponse("Password must be at least 8 characters long.") 
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse("Login successful.") and redirect('home')
        return redirect('register')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')

def home(request):
    return render(request, 'accounts/home.html')

def features(request):
    return render(request, 'accounts/features.html')

def about(request):
    return render(request, 'accounts/about.html')

def contact(request):
    return render(request, 'accounts/contact.html')
