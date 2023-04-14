from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import EquipmentUpdateSerializer

from apps.warehouse.models import Equipment


class EquipmentUpdateAPIView(UpdateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentUpdateSerializer
    permission_classes = (IsAdminUser,)
