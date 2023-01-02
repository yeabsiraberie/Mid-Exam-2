from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from employeapi.models import Employe
from .serializers import EmployeSerializers
from rest_framework import status




@api_view(['GET'])
def lisemp(request):
    employe=Employe.objects.all()
    serialzer=EmployeSerializers(employe,many=True)
    return Response(serialzer.data)

@api_view(['POST'])
def setemp(request):
    serialzer=EmployeSerializers(data=request.data)
    if serialzer.is_valid():
        serialzer.save()

    return Response(serialzer.data)    

@api_view(['DELETE'])
def delemp(request,pk):
    employe=Employe.objects.get(pk=pk)
    employe.delete()

    return Response(status=status.HTTP_202_ACCEPTED)    
# Create your views here.
