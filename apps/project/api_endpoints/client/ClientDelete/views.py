from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.project.models import Client


class ClientDestroyAPIView(DestroyAPIView):
    queryset = Client.objects.all()
    permission_classes = (IsAdminUser,)
