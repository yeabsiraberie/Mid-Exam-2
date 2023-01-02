from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from studentapi.models import Student
from .serializers import StudentSerializers
from rest_framework import status




@api_view(['GET'])
def lisstu(request):
    student=Student.objects.all()
    serialzer=StudentSerializers(student,many=True)
    return Response(serialzer.data)

@api_view(['POST'])
def setstu(request):
    serialzer=StudentSerializers(data=request.data)
    if serialzer.is_valid():
        serialzer.save()

    return Response(serialzer.data)   

@api_view(['DELETE'])
def delstu(request,pk):
    student=Student.objects.get(pk=pk)
    student.delete()

    return Response(status=status.HTTP_202_ACCEPTED)     
# Create your views here.
