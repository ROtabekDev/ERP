from rest_framework.generics import ListAPIView

from apps.employees.models import Employee
from .serializers import EmployeeListSerializer


class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer
