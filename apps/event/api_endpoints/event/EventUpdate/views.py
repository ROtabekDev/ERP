from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import EventUpdateSerializer

from apps.event.models import Event


class EventUpdateAPIView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventUpdateSerializer
    permission_classes = (IsAdminUser,)
