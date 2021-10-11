from django import forms


class BookingForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    date = forms.DateField()
    time = forms.TimeField()
    message = forms.CharField(widget=forms.Textarea)
