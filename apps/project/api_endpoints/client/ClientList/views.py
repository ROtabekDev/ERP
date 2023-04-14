from rest_framework.generics import ListAPIView

from apps.project.models import Client
from .serializers import ClientListSerializer


class ClientListAPIView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer
