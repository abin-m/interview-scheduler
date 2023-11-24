from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CandidateAvailability, InterviewerAvailability
from .serializers import CandidateAvailabilitySerializer, InterviewerAvailabilitySerializer


from .serializers import CandidateAvailabilitySerializer, InterviewerAvailabilitySerializer
from api.interview.models import Interview

# Candidate Availability views
@api_view(['GET', 'POST',])
def candidate_availability(request):
    if request.method == 'GET':
        candidate_avails = CandidateAvailability.objects.all()
        serializer = CandidateAvailabilitySerializer(candidate_avails, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        serializer = CandidateAvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_candidate_availability(request, interview_code):
    try:
        candidate_availability = CandidateAvailability.objects.get(interview_code=interview_code)
    except CandidateAvailability.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    candidate_availability.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Interviewer Availability views
@api_view(['GET', 'POST'])
def interviewer_availability(request):
    if request.method == 'GET':
        interviewer_avails = InterviewerAvailability.objects.all()
        serializer = InterviewerAvailabilitySerializer(interviewer_avails, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InterviewerAvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_interviewer_availability(request, interview_code):
    try:
        interviewer_availability = InterviewerAvailability.objects.get(interview_code=interview_code)
    except InterviewerAvailability.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    interviewer_availability.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
