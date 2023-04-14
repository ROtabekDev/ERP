from rest_framework.generics import ListAPIView

from apps.project.models import Organization
from .serializers import OrganizationListSerializer


class OrganizationListAPIView(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationListSerializer
