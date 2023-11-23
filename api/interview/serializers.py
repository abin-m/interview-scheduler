from rest_framework import serializers
from .models import Interview

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ['interview_date', 'role', 'interview_code', 'candidate_id', 'interviewer_id','interview_time_slot']
