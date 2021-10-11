from django.shortcuts import render
from .forms import BookingForm
# from django.http import HttpResponse

# Create your views here.


def returnHome(request):
    return render(request, 'home.html')


def returnBookingPage(request):
    form = BookingForm()
    return render(request, 'booking.html', {'form': form})
