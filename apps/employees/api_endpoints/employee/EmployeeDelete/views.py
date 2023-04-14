from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.employees.models import Employee


class EmployeeDestroyAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    permission_classes = (IsAdminUser,)
