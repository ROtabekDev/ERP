from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import EventCreateSerializer


class EventCreateAPIView(CreateAPIView):
    serializer_class = EventCreateSerializer
    permission_classes = (IsAdminUser,)
