# Generated by Django 3.1.1 on 2020-09-28 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traveller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travelling_area', models.CharField(max_length=1000)),
                ('User_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserManagement.profile')),
            ],
        ),
    ]
