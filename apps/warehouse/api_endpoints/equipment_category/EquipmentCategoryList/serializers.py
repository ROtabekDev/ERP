from rest_framework.serializers import ModelSerializer

from apps.warehouse.models import EquipmentCategory


class EquipmentCategoryListSerializer(ModelSerializer):
    class Meta:
        model = EquipmentCategory
        fields = ('id', 'title')