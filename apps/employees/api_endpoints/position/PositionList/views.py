from rest_framework.generics import ListAPIView

from apps.employees.models import Position
from .serializers import PositionListSerializer


class PositionListAPIView(ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionListSerializer
