from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from .forms import BookingForm
# from django.http import HttpResponse

# Create your views here.


def returnHome(request):
    return render(request, 'home.html')


def returnBookingPage(request):

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Contact request submitted successfully.')
            return redirect('booking')

    form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def returnAboutPage(request):
    return render(request, 'about.html')