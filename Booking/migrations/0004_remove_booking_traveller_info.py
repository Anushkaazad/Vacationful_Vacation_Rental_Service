# Generated by Django 3.1.1 on 2020-09-30 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0003_auto_20200929_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='traveller_Info',
        ),
    ]
