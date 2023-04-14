from rest_framework.generics import ListAPIView

from .serializers import EventListSerializer

from apps.event.models import Event


class EventListAPIView(ListAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.all()

