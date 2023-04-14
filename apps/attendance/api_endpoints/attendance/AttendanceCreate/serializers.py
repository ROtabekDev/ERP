from rest_framework.serializers import ModelSerializer

from apps.attendance.models import Attendance


class AttendanceCreateSerializer(ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('employee', 'intern', 'date', 'arrival_time')

