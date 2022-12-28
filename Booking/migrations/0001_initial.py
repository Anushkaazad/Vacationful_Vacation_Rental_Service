# Generated by Django 3.1.1 on 2020-09-29 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Traveller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Checkin_Date', models.CharField(max_length=100)),
                ('Checkin_Time', models.CharField(max_length=100)),
                ('Checkout_Date', models.CharField(max_length=100)),
                ('Checkout_time', models.CharField(max_length=100)),
                ('No_of_Guests', models.IntegerField(max_length=10)),
                ('traveller_Info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Traveller.traveller')),
            ],
        ),
    ]
