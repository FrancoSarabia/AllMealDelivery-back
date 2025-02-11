from rest_framework import serializers
from ..models.employee import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['_id', 'person', 'user']