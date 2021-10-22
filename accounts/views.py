from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def returnLogin(request):
    return HttpResponse('Login Page')


def returnSignup(request):
    return HttpResponse('Signup Page')