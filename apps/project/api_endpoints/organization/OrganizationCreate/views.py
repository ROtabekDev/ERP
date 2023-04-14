from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import OrganizationCreateSerializer


class OrganizationCreateAPIView(CreateAPIView):
    serializer_class = OrganizationCreateSerializer
    permission_classes = (IsAdminUser,)
