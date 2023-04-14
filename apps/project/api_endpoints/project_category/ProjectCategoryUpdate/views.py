from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

from .serializers import ProjectCategoryUpdateSerializer

from apps.project.models import ProjectCategory


class ProjectCategoryUpdateAPIView(UpdateAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategoryUpdateSerializer
    permission_classes = (IsAdminUser,)