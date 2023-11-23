from rest_framework import serializers
from .models import CandidateDetails, InterviewerDetails

class CandidateDetailsSerializer(serializers.ModelSerializer):
    candidate_id = serializers.IntegerField(required=False)  

    class Meta:
        model = CandidateDetails
        fields = ['candidate_id', 'full_name', 'email', 'contact']

class InterviewerDetailsSerializer(serializers.ModelSerializer):
    interviewer_id = serializers.IntegerField(required=False)  

    class Meta:
        model = InterviewerDetails
        fields = ['interviewer_id', 'full_name', 'email', 'contact']

