from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import OrganizationUpdateSerializer

from apps.project.models import Organization


class OrganizationUpdateAPIView(UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationUpdateSerializer
    permission_classes = (IsAdminUser,)