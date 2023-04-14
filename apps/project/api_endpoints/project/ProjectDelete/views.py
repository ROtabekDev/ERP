from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.project.models import Project


class ProjectDestroyAPIView(DestroyAPIView):
    queryset = Project.objects.all()
    permission_classes = (IsAdminUser,)
