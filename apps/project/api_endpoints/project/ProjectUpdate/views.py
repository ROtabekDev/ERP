from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import ProjectUpdateSerializer

from apps.project.models import Project


class ProjectUpdateAPIView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectUpdateSerializer
    permission_classes = (IsAdminUser,)
