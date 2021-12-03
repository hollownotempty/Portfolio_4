from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .forms import SubmitForm
from .models import Appointment


# Create your views here.

# Templates for the confirmation email to be sent in the submit_page view.
plaintext_message = get_template('email_template.txt')
html_message = get_template('email_template.html')


def returnHome(request):
    return render(request, 'home.html')


def submit_page(request):

    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid:
            instance = form.save()
            instance.user = request.user
            instance.save()
            # The following code sends an email upon form completion to the 
            # email corresponding with the currently logged in user.
            email = instance.user.email
            subject, from_email, recipient_list = 'Your Submission', settings.EMAIL_HOST_USER, [email, ]
            text_content = plaintext_message.render()
            html_content = html_message.render()
            msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, 'Contact request submitted successfully.')
            return redirect('submit')

    form = SubmitForm()
    return render(request, 'submit.html', {'form': form})


def returnAboutPage(request):
    return render(request, 'about.html')


def return_appointments(request):
    # Allows the display of all objects in the Appointment model on the 
    # appointments page.
    return render(request, 'appointments.html', {
        'appointments': Appointment.objects.all(),
        })
