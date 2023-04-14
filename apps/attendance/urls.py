from django.urls import path

from .api_endpoints import attendance, missed_dates

urlpatterns = [
    # attendance
    path('list/', attendance.AttendanceListAPIView.as_view(), name="attendance-list"),
    path('create/', attendance.AttendanceCreateAPIView.as_view(), name="attendance-create"),

    # missed_dates
    path('missed-dates/list/', missed_dates.MissedTimesListAPIView.as_view(), name="missed-dates-list"),
]