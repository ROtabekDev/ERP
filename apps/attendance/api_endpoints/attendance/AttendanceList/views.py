from rest_framework.generics import ListAPIView

from apps.attendance.models import Attendance
from .serializers import AttendanceListSerializer


class AttendanceListAPIView(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceListSerializer
    filterset_fields = ['date', 'employee', 'intern']
