from django import forms
from .models import Appointment

class SubmitForm(forms.ModelForm):
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField()
    # date = forms.DateField()
    # time = forms.TimeField()
    # message = forms.CharField()

    class Meta:
        exclude = [
            'date_booked',
            'user']
        model = Appointment
        fields = '__all__'
