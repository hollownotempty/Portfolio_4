from django.shortcuts import render, redirect
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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['appointment_date']
            time = form.cleaned_data['appointment_time']
            message = form.cleaned_data['message']
            return redirect('home')

    form = BookingForm()
    return render(request, 'booking.html', {'form': form})
