# Generated by Django 3.2.7 on 2021-12-03 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_auto_20211126_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date_booked',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
