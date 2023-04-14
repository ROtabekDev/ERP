from rest_framework.generics import RetrieveAPIView

from apps.employees.models import Employee
from .serializers import EmployeeDetailSerializer


class EmployeeRetrieveAPIView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeDetailSerializer
