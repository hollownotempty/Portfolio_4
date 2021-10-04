from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def returnHome(request):
    return render(request, 'home.html')


def returnBookingPage(request):
    return render(request, 'booking.html')
