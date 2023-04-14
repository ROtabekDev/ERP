from datetime import datetime

from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Attendance, MissedTimes


@receiver(post_save, sender=Attendance)
def create_attendance(sender, instance, created, **kwargs):
    if created:
        arrival_time = str(instance.arrival_time).split()
        start_time = datetime.strptime('10:00:00', '%H:%M:%S')
        arrival_time = datetime.strptime(arrival_time[0], '%H:%M:%S')
        if arrival_time > start_time:
            datetime1 = datetime.combine(instance.date, arrival_time.time())
            datetime2 = datetime.combine(instance.date, start_time.time())

            minutes_late = datetime1 - datetime2

            MissedTimes.objects.create(employee=instance.employee, intern=instance.intern, date=instance.date,
                                       minutes_late=str(minutes_late))
