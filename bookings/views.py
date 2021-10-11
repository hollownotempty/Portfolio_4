from django.shortcuts import render, redirect
from django.contrib import messages
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
