from rest_framework.serializers import ModelSerializer

from apps.employees.models import Region


class RegionListSerializer(ModelSerializer):

    class Meta:
        model = Region
        fields = ('id', 'title', 'slug')