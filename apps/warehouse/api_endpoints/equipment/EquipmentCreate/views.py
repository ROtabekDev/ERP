from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import EquipmentCreateSerializer


class EquipmentCreateAPIView(CreateAPIView):
    serializer_class = EquipmentCreateSerializer
    permission_classes = (IsAdminUser,)
