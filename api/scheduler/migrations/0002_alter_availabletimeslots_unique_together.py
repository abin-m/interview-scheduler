# Generated by Django 4.2.7 on 2023-11-24 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='availabletimeslots',
            unique_together={('interview_code', 'available_slots')},
        ),
    ]
