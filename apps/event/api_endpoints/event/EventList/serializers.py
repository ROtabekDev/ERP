from rest_framework.serializers import ModelSerializer

from apps.event.models import Event


class EventListSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'slug', 'place_name', 'date', 'description')
