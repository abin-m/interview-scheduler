from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Interview
from .serializers import InterviewSerializer

@api_view(['GET', 'POST'])
def interview_list(request):
    if request.method == 'GET':
        interviews = Interview.objects.all()
        serializer = InterviewSerializer(interviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InterviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def interview_detail(request, interview_code):
    try:
        interview = Interview.objects.get(pk=interview_code)
    except Interview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InterviewSerializer(interview)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InterviewSerializer(interview, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        interview.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
