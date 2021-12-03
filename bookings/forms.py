from django import forms
from .models import Appointment

class SubmitForm(forms.ModelForm):
    
    class Meta:
        exclude = [
            'date_booked',
            'user']
        model = Appointment
        fields = '__all__'
