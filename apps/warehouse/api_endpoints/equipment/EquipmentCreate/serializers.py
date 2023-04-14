from rest_framework.serializers import ModelSerializer

from apps.warehouse.models import Equipment


class EquipmentCreateSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('equipment_name', 'equipment_category', 'price', 'qty')
