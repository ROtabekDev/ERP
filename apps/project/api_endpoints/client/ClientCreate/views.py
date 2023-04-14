from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import ClientCreateSerializer


class ClientCreateAPIView(CreateAPIView):
    serializer_class = ClientCreateSerializer
    permission_classes = (IsAdminUser,)
