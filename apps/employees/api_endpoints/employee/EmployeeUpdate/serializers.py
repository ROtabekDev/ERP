from rest_framework.serializers import ModelSerializer

from apps.employees.models import Employee


class EmployeeUpdateSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'first_name', 'last_name', 'phone_number', 'position', 'birthday', 'age', 'gender', 'image', 'resume_file',
            'salary', 'address')