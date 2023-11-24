from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from .serializers import AvailableTimeSlotsSerializer
from api.interview.models import Interview

# from api.registration.models import Interview,InterviewerAvailability
from api.registration.availability_pro.models import CandidateAvailability,InterviewerAvailability

def find_available_time_slots(candidate_start, candidate_end, interviewer_start, interviewer_end, candidate_id, interviewer_id):
    cache_key = f"availability_{candidate_start}_{candidate_end}_{interviewer_start}_{interviewer_end}"
    cached_slots = cache.get(cache_key)
    if cached_slots:
        print("used a slot from cache")
        return cached_slots

    try:
        candidate_start = datetime.strptime(candidate_start, "%I:%M %p")
        candidate_end = datetime.strptime(candidate_end, "%I:%M %p")
        interviewer_start = datetime.strptime(interviewer_start, "%I:%M %p")
        interviewer_end = datetime.strptime(interviewer_end, "%I:%M %p")
    except ValueError:
        return "Invalid time format. Please use HH:MM AM/PM format."

    earliest_start = max(candidate_start, interviewer_start)
    latest_end = min(candidate_end, interviewer_end)
    diff = latest_end - earliest_start

    if diff >= timedelta(hours=1):
        available_time_slots = []
        current_time = earliest_start
        start_slot = None

        while current_time <= latest_end:
            if (
                current_time >= interviewer_start
                and current_time + timedelta(hours=1) <= interviewer_end
                and current_time >= candidate_start
                and current_time + timedelta(hours=1) <= candidate_end
            ):
                if start_slot is None:
                    start_slot = current_time

                next_slot = current_time + timedelta(hours=1)

                if next_slot > latest_end:
                    available_time_slots.append(f"{start_slot.strftime('%I:%M %p')} , {current_time.strftime('%I:%M %p')}")
                    break
                elif next_slot not in available_time_slots:
                    available_time_slots.append(f"{start_slot.strftime('%I:%M %p')} , {next_slot.strftime('%I:%M %p')}")
                    start_slot = None

            current_time += timedelta(hours=1)

        # Storing data in Redis cache
        cache.set(cache_key, available_time_slots, timeout=3600)  # Setting a timeout of 1 hour for the cache entry

        return available_time_slots if available_time_slots else "NO SLOTS FOUND"
    else:
        return "NO SLOTS FOUND"


@api_view(['POST'])
def schedule_interview(request, candidate_id, interviewer_id):
    
    interview_code = request.data.get('interview_code')
    candidate_availability = get_object_or_404(CandidateAvailability, candidate_id=candidate_id)
    interviewer_availability = get_object_or_404(InterviewerAvailability, interviewer_id=interviewer_id)
    slot = find_available_time_slots(candidate_availability.start_time, candidate_availability.end_time,
                                     interviewer_availability.start_time, interviewer_availability.end_time, candidate_id, interviewer_id)

    if slot == "NO SLOTS FOUND":
        return Response("No available slots found", status=status.HTTP_404_NOT_FOUND)

    schedule = {
        "interview_code": str(interview_code),
        "available_slots": str(slot),
    }

    serializer = AvailableTimeSlotsSerializer(data=schedule)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def slot_confirmation(request):
#     interview_code = request.data.get('interview_code')