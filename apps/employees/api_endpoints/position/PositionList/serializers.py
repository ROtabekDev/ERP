from rest_framework.serializers import ModelSerializer

from apps.employees.models import Position


class PositionListSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'title', 'slug')
