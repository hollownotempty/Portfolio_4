from django import forms
from .models import Appointment


class BookingForm(forms.ModelForm):
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField()
    # date = forms.DateField()
    # time = forms.TimeField()
    # message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Appointment
        fields = ('first_name', 'last_name', 'email', 'appointment_date', 'appointment_time', 'message')
