# Generated by Django 3.1.2 on 2020-10-07 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Traveller', '0004_traveller_property_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traveller',
            name='Property_name',
        ),
    ]
