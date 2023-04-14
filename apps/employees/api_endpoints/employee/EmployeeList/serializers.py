from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.employees.models import Employee
from apps.employees.api_endpoints.address import AddressListSerializer


class EmployeeListSerializer(ModelSerializer):
    position = serializers.StringRelatedField()
    address = AddressListSerializer()

    class Meta:
        model = Employee
        fields = (
            'id', 'first_name', 'last_name', 'phone_number', 'position', 'birthday', 'age', 'gender', 'image',
            'resume_file', 'salary', 'address')
