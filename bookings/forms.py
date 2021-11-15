from django import forms
from .models import Appointment
import datetime as dt
HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(10, 19)]


class SubmitForm(forms.ModelForm):
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField()
    # date = forms.DateField()
    # time = forms.TimeField()
    # message = forms.CharField()

    class Meta:
        exclude = ['date_booked']
        model = Appointment
        fields = '__all__'
        widgets = {'appointment_time': forms.Select(choices=HOUR_CHOICES)}
