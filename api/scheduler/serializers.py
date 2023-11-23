from rest_framework import serializers
from .models import AvailableTimeSlots

class AvailableTimeSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTimeSlots
        fields = ['interview_code', 'available_slots']