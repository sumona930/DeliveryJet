# Generated by Django 3.2.5 on 2021-08-01 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabilitymodel',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.addressphonemodel'),
        ),
        migrations.AlterField(
            model_name='availabilitymodel',
            name='slot_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.timeslotmodel'),
        ),
        migrations.AlterField(
            model_name='timeslotmodel',
            name='Day',
            field=models.CharField(blank=True, choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='timeslotmodel',
            name='time',
            field=models.CharField(blank=True, choices=[('9am-3pm', '9am-3pm'), ('3pm-9pm', '3pm-9pm')], max_length=255, null=True),
        ),
    ]
