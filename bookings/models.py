from django.db import models
from django.conf import settings
import datetime

# Create your models here.


class Appointment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        on_delete=models.CASCADE)
    reference_mix = models.CharField(max_length=200)
    file_link = models.CharField(max_length=200)
    message = models.TextField(max_length=500)
    date_booked = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.user)
