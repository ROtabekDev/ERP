from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.warehouse.models import Equipment


class EquipmentDetailSerializer(ModelSerializer):
    equipment_name = serializers.StringRelatedField()
    equipment_category = serializers.StringRelatedField()

    class Meta:
        model = Equipment
        fields = ('id', 'equipment_name', 'equipment_category', 'price', 'qty')
