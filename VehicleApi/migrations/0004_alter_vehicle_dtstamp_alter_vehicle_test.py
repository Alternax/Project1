# Generated by Django 5.2 on 2025-04-13 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VehicleApi', '0003_alter_vehicle_v_make_alter_vehicle_v_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='dtstamp',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='test',
            field=models.TextField(blank=True, null=True),
        ),
    ]
