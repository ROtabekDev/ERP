from django.contrib import admin

from .models import Attendance, MissedTimes

admin.site.register(Attendance)
admin.site.register(MissedTimes)