from rest_framework.generics import RetrieveAPIView

from apps.warehouse.models import Equipment
from .serializers import EquipmentDetailSerializer


class EquipmentRetrieveAPIView(RetrieveAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentDetailSerializer
