# Generated by Django 3.1.1 on 2020-10-06 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PropertyManagement', '0003_auto_20201005_1630'),
        ('Traveller', '0003_auto_20201005_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveller',
            name='Property_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='PropertyManagement.property'),
        ),
    ]
