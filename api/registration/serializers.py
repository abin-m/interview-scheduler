from rest_framework import serializers
from .models import CandidateDetails, InterviewerDetails

class CandidateDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateDetails
        fields = ['id', 'full_name', 'email', 'contact','candidate_id']  

class InterviewerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewerDetails
        fields = ['id', 'full_name', 'email', 'contact','interviewer_id']