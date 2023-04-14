from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import InternUpdateSerializer

from apps.internship.models import Intern


class InternUpdateAPIView(UpdateAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternUpdateSerializer
    permission_classes = (IsAdminUser,)
