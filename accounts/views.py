from django.shortcuts import render
from . import views

# Create your views here.


def returnLogin(request):
    return render(request, 'login.html')


def returnSignup(request):
    return render(request, 'signup.html')
