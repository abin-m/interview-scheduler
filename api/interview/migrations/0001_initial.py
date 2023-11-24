# Generated by Django 4.2.7 on 2023-11-24 07:56

import api.interview.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('interview_date', models.CharField(max_length=20)),
                ('interview_time_slot', models.CharField(default='NULL', max_length=20)),
                ('role', models.CharField(max_length=100)),
                ('interview_code', models.CharField(default=api.interview.models.generate_unique_random_id, max_length=5, primary_key=True, serialize=False)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.candidatedetails')),
                ('interviewer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.interviewerdetails')),
            ],
        ),
    ]
