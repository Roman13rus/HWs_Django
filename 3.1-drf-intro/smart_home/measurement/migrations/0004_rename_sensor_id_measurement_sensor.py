# Generated by Django 4.2.4 on 2023-08-12 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_measurement_temperature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor_id',
            new_name='sensor',
        ),
    ]
