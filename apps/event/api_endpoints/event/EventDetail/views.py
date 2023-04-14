from rest_framework.generics import RetrieveAPIView

from apps.event.models import Event
from .serializers import EventDetailSerializer


class EventDetailAPIView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
