from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import EmployeeCreateSerializer


class EmployeeCreateAPIView(CreateAPIView):
    serializer_class = EmployeeCreateSerializer
    permission_classes = (IsAdminUser,)
