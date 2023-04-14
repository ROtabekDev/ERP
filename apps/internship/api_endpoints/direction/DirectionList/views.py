from rest_framework.generics import ListAPIView

from apps.internship.models import Direction

from .serializers import DirectionListSerializer


class DirectionListAPIView(ListAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionListSerializer
