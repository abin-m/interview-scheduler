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

