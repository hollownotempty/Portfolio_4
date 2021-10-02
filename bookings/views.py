from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def returnHome(request):
    return HttpResponse('Home Page')


def returnBookingPage(request):
    return HttpResponse('Booking page')
