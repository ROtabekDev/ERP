from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.attendance.models import MissedTimes


class MissedTimesListSerializer(ModelSerializer):
    class Meta:
        model = MissedTimes
        fields = ('id', 'employee', 'intern', 'date', 'minutes_late')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if representation['employee'] is None:
            representation.pop('employee')
        if representation['intern'] is None:
            representation.pop('intern')

        return representation