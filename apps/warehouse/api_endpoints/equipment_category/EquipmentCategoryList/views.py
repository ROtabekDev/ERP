from rest_framework.generics import ListAPIView

from apps.warehouse.models import EquipmentCategory
from .serializers import EquipmentCategoryListSerializer


class EquipmentCategoryListAPIView(ListAPIView):
    queryset = EquipmentCategory.objects.all()
    serializer_class = EquipmentCategoryListSerializer
