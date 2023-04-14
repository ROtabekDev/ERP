from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.project.models import Organization


class OrganizationDestroyAPIView(DestroyAPIView):
    queryset = Organization.objects.all()
    permission_classes = (IsAdminUser,)
