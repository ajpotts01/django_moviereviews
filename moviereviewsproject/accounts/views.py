from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.shortcuts import redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

def signup(request: HttpResponse):
    if (request.method == 'GET'):        
        return render(request, 'signup.html', {
            'form': CustomUserCreationForm
        })
    else:
        if (request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': CustomUserCreationForm,
                    'error': 'User name already exists. Please choose another name.'
                })
        else:
            return render(request, 'signup.html', {
                'form': CustomUserCreationForm,
                'error': 'Passwords do not match'
            })

def logout_user(request: HttpResponse):
    logout(request)
    return redirect('home')

def login_user(request: HttpResponse):
    if (request.method == 'GET'):
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request,
            username = request.POST['username'],
            password = request.POST['password'])
        
        if (user is None):
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Username and password do not match'
            })
        else:
            login(request, user)
            return redirect('home')
