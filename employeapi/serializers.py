from rest_framework import serializers
from employeapi.models import Employe

class EmployeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Employe
        fields='__all__'