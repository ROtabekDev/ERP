from rest_framework.generics import ListAPIView

from apps.employees.models import District
from .serializers import DistrictListSerializer


class DistrictListAPIView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictListSerializer