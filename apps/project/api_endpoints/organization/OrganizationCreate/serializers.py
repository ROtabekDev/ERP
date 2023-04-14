from rest_framework.serializers import ModelSerializer

from apps.project.models import Organization


class OrganizationCreateSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = ('title', 'slug')
