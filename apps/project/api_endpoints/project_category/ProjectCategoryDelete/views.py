from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.project.models import ProjectCategory


class ProjectCategoryDestroyAPIView(DestroyAPIView):
    queryset = ProjectCategory.objects.all()
    permission_classes = (IsAdminUser,)