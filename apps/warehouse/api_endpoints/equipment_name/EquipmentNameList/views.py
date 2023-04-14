from rest_framework.generics import ListAPIView

from apps.warehouse.models import EquipmentName
from .serializers import EquipmentNameListSerializer


class EquipmentNameListAPIView(ListAPIView):
    queryset = EquipmentName.objects.all()
    serializer_class = EquipmentNameListSerializer