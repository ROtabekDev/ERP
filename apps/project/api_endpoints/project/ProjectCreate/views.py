from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import ProjectCreateSerializer


class ProjectCreateAPIView(CreateAPIView):
    serializer_class = ProjectCreateSerializer
    permission_classes = (IsAdminUser,)
