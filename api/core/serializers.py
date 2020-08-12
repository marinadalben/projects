from rest_framework import serializers
from .models import Employee

class EmployeeSerializer (serializers.ModelSerializer):
    class Meta:
	    model = Employee
	    fields = ('pk', 'name', 'email', 'department')
    def create(self, validated_data):
        employee = Employee.objects.create(**validated_data)
        employee.save()
        return employee    