from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import ClientUpdateSerializer

from apps.project.models import Client


class ClientUpdateAPIView(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientUpdateSerializer
    permission_classes = (IsAdminUser,)
