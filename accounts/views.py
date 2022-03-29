from email import message
import re
import django
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.success(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        # Get entered form values form UI
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Validating Password
        if password != password2:
            messages.error(request, "Password doesn't match")
            return redirect('register')        
        # Validating Username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please enter a new username")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "email already exists")
            return redirect('register')
        user = User.objects.create_user(username= username, password=password, email= email,
        first_name=first_name, last_name=last_name)
        user.save()
        messages.success(request, "Registered Successfully. You can login")
        return redirect('login')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "Logged out succesfully")
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')