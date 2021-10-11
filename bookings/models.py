from django.db import models
import datetime as dt

# Create your models here.


class Appointment(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    appointment_date = models.DateField(null=False)
    appointment_time = models.TimeField(default=dt.time(00, 00))
    message = models.TextField(max_length=500)

    def __str__(self):
        return str(self.last_name + ' ' + str(self.appointment_date))
