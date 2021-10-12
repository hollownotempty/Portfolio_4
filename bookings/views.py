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
            email = request.POST.get('email', '')
            form.save()
            subject = 'Your booking.'
            message = 'Thank you for booking your call, I look forward to working together./n I will be in contact shortly regarding the call. '
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'Contact request submitted successfully.')
            return redirect('booking')

    form = BookingForm()
    return render(request, 'booking.html', {'form': form})


def returnAboutPage(request):
    return render(request, 'about.html')
