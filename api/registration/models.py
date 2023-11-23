from django.db import models
from datetime import date
import random
from django.db.models.signals import pre_save
from django.dispatch import receiver


def generate_unique_random_id(queryset, field_name):
    while True:
        random_id = random.randint(10000, 99999)
        if not queryset.filter(**{field_name: random_id}).exists():
            return random_id

class CandidateDetails(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=13)
    candidate_id = models.IntegerField(primary_key=True)
    
    def __str__(self):
        return self.full_name

@receiver(pre_save, sender=CandidateDetails)
def assign_candidate_id(sender, instance, **kwargs):
    if not instance.candidate_id:
        queryset = sender.objects
        field_name = 'candidate_id'
        instance.candidate_id = generate_unique_random_id(queryset, field_name)


class InterviewerDetails(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=13)
    interviewer_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.full_name

@receiver(pre_save, sender=InterviewerDetails)
def assign_interviewer_id(sender, instance, **kwargs):
    if not instance.interviewer_id:
        queryset = sender.objects
        field_name = 'interviewer_id'
        instance.interviewer_id = generate_unique_random_id(queryset, field_name)


