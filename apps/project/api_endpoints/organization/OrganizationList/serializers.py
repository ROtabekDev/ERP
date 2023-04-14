from rest_framework.serializers import ModelSerializer

from apps.project.models import Organization


class OrganizationListSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'title', 'slug')
