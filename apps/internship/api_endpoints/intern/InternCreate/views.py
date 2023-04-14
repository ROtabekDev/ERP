from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import InternCreateSerializer


class InternCreateAPIView(CreateAPIView):
    serializer_class = InternCreateSerializer
    permission_classes = (IsAdminUser,)
