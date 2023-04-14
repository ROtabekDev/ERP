from rest_framework.serializers import ModelSerializer

from apps.project.models import Client


class ClientCreateSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('full_name', 'organization', 'client_type')
