from rest_framework import serializers
from .models import CandidateAvailability,InterviewerAvailability



class CandidateAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateAvailability
        fields = ['candidate_id', 'interview_code', 'start_time', 'end_time']

class InterviewerAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewerAvailability
        fields = ['interviewer_id', 'interview_code', 'start_time', 'end_time']