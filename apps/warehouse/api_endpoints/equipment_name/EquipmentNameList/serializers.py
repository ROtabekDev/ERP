from rest_framework.serializers import ModelSerializer

from apps.warehouse.models import EquipmentName


class EquipmentNameListSerializer(ModelSerializer):
    class Meta:
        model = EquipmentName
        fields = ('id', 'title')