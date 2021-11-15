from django.db import models
import datetime as dt

# Create your models here.


class Appointment(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    file_link = models.CharField(max_length=200)
    message = models.TextField(max_length=500)
    date_booked = models.DateField(default=dt.date.today)

    def __str__(self):
        return str(self.last_name + ' ' + str(self.appointment_date))
