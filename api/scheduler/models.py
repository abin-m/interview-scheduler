from django.db import models
from api.interview.models import Interview

class AvailableTimeSlots(models.Model):
    interview_code = models.ForeignKey(Interview, on_delete=models.CASCADE)
    available_slots = models.CharField(max_length=100)  # Adjust max_length as needed

    def __str__(self):
        return f"slots for{self.interview_code}"
