from rest_framework.generics import RetrieveAPIView

from apps.project.models import Project
from .serializers import ProjectDetailSerializer


class ProjectRetrieveAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
