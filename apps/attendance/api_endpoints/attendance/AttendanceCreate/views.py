from rest_framework.generics import CreateAPIView

from .serializers import AttendanceCreateSerializer


class AttendanceCreateAPIView(CreateAPIView):
    serializer_class = AttendanceCreateSerializer
