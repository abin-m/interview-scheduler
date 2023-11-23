from django.db import models
from api.registration.models import CandidateDetails, InterviewerDetails
import random
# Create your models here.


def generate_unique_random_id():
    return ''.join([str(random.randint(0, 9)) for _ in range(5)])

class Interview(models.Model):
    interview_date = models.CharField(max_length=20)
    interview_time_slot = models.CharField(max_length=20,default="NULL")
    role = models.CharField(max_length=100)
    interview_code = models.CharField(max_length=5, primary_key=True, default=generate_unique_random_id)
    candidate_id = models.ForeignKey(CandidateDetails, on_delete=models.CASCADE)
    interviewer_id = models.ForeignKey(InterviewerDetails, on_delete=models.CASCADE)

    def __str__(self):
        return f"Interview for: {self.role} - Date: {self.interview_date}"
