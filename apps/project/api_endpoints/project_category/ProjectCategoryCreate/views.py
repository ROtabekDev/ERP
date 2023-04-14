from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import ProjectCategoryCreateSerializer


class ProjectCategoryCreateAPIView(CreateAPIView):
    serializer_class = ProjectCategoryCreateSerializer
    permission_classes = (IsAdminUser,)
