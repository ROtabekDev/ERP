from rest_framework.generics import ListAPIView

from apps.warehouse.models import Equipment
from .serializers import EquipmentListSerializer


class EquipmentListAPIView(ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentListSerializer
