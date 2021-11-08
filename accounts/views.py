from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, 'Successfully logged in!')
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error logging in, try again..."))
            return redirect('login.html')

    else:
        return render(request, 'registration/login.html', {})


def signup_user(request):
    return HttpResponse('Signup')


def logout_user(request):
    logout(request)
    messages.success(request, ("Successfully logged out!"))
    return redirect('home')
