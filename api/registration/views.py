from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CandidateDetails, InterviewerDetails
from .serializers import CandidateDetailsSerializer, InterviewerDetailsSerializer


@api_view(['GET', 'POST'])
def candidate_list(request):
    if request.method == 'GET':
        candidates = CandidateDetails.objects.all()
        serializer = CandidateDetailsSerializer(candidates, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CandidateDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def candidate_details(request, pk):
    try:
        candidate = CandidateDetails.objects.get(candidate_id=pk)
    except CandidateDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CandidateDetailsSerializer(candidate)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CandidateDetailsSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def interviewer_list(request):
    if request.method == 'GET':
        interviewers = InterviewerDetails.objects.all()
        serializer = InterviewerDetailsSerializer(interviewers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InterviewerDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def interviewer_details(request, pk):
    try:
        interviewer = InterviewerDetails.objects.get(interviewer_id=pk)
    except InterviewerDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InterviewerDetailsSerializer(interviewer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InterviewerDetailsSerializer(interviewer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        interviewer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
