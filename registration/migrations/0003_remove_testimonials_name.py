# Generated by Django 3.0.5 on 2020-07-12 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20200711_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonials',
            name='name',
        ),
    ]
