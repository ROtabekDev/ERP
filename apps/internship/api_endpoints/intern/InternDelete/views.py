from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.internship.models import Intern


class InternDestroyAPIView(DestroyAPIView):
    queryset = Intern.objects.all()
    permission_classes = (IsAdminUser,)
