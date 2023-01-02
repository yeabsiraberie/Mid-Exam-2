from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from teacherapi.models import Teacher
from .serializers import TeacherSerializers
from rest_framework import status




@api_view(['GET'])
def listea(request):
    teacher=Teacher.objects.all()
    serialzer=TeacherSerializers(Teacher,many=True)
    return Response(serialzer.data)

@api_view(['POST'])
def settea(request):
    serialzer=TeacherSerializers(data=request.data)
    if serialzer.is_valid():
        serialzer.save()

    return Response(serialzer.data)  

@api_view(['DELETE'])
def deltea(request,pk):
    teacher=Teacher.objects.get(pk=pk)
    teacher.delete()

    return Response(status=status.HTTP_202_ACCEPTED)      
# Create your views here.
