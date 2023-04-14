from rest_framework.serializers import ModelSerializer

from apps.project.models import Client


class ClientUpdateSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('full_name', 'organization', 'client_type')
