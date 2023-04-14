from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import EmployeeUpdateSerializer

from apps.employees.models import Employee


class EmployeeUpdateAPIView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeUpdateSerializer
    permission_classes = (IsAdminUser,)
