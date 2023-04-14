from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.project.models import Client


class ClientListSerializer(ModelSerializer):
    organization = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = ('id', 'full_name', 'organization', 'client_type')
