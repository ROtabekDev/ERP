from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.employees.models import Address


class AddressListSerializer(ModelSerializer):
    region = serializers.StringRelatedField()
    district = serializers.StringRelatedField()

    class Meta:
        model = Address
        fields = ('id', 'region', 'district', 'home_address')