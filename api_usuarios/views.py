from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')

def en_costruccion(request):
    return render(request, 'en_costruccion.html')

def login_page(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Usuario o clave incorrecto')
    return render(request, 'login.html')

def logout_page(request):
    logout(request)    
    return redirect('/login_page')