from django.db import models
from api.registration.models import CandidateDetails,InterviewerDetails
from api.interview.models import Interview

# Modal for Time availability

class CandidateAvailability(models.Model):
    candidate_id = models.ForeignKey(CandidateDetails, on_delete=models.CASCADE)
    interview_code = models.ForeignKey(Interview, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)

    class Meta:
        unique_together = ('candidate_id', 'interview_code', 'start_time', 'end_time')

class InterviewerAvailability(models.Model):
    interviewer_id = models.ForeignKey(InterviewerDetails, on_delete=models.CASCADE)
    interview_code = models.ForeignKey(Interview, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)

    class Meta:
        unique_together = ('interviewer_id', 'interview_code', 'start_time', 'end_time')
