from rest_framework.serializers import ModelSerializer

from apps.internship.models import Direction


class DirectionListSerializer(ModelSerializer):
    class Meta:
        model = Direction
        fields = ('id', 'title')
