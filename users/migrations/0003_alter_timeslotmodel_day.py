# Generated by Django 3.2.5 on 2021-08-01 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210801_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslotmodel',
            name='Day',
            field=models.CharField(blank=True, choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=255, null=True),
        ),
    ]
