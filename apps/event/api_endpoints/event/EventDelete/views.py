from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.event.models import Event


class EventDestroyAPIView(DestroyAPIView):
    queryset = Event.objects.all()
    permission_classes = (IsAdminUser,)
