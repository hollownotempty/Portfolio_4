# Generated by Django 3.2.7 on 2021-11-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_auto_20211126_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='email',
        ),
        migrations.AddField(
            model_name='appointment',
            name='reference_mix',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]