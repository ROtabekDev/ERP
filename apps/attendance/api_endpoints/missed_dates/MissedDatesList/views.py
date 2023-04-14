from rest_framework.generics import ListAPIView

from apps.attendance.models import MissedTimes
from .serializers import MissedTimesListSerializer


class MissedTimesListAPIView(ListAPIView):
    queryset = MissedTimes.objects.all()
    serializer_class = MissedTimesListSerializer
    filterset_fields = ['date', 'employee', 'intern']
