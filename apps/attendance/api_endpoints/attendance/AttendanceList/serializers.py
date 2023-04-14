from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.attendance.models import Attendance


class AttendanceListSerializer(ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('id', 'employee', 'intern', 'date', 'arrival_time')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if representation['employee'] is None:
            representation.pop('employee')
        if representation['intern'] is None:
            representation.pop('intern')

        return representation
