from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.warehouse.models import Equipment


class EquipmentDestroyAPIView(DestroyAPIView):
    queryset = Equipment.objects.all()
    permission_classes = (IsAdminUser,)
