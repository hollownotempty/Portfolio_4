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
            # subject = 'Thank you for your booking.'
            # message = 'Thank you for booking in, I look forward to getting started on your project together./n I will be in touch soon regarding your booking.'
            # from_email = settings.EMAIL_HOST_USER
            # to_list = [BookingForm.email, settings.EMAIL_HOST_USER]
            # send_mail(subject, message, from_email, to_list, fail_silently=True)
            messages.success(request, 'Contact request submitted successfully.')
            return redirect('booking')

    form = BookingForm()
    return render(request, 'booking.html', {'form': form})
