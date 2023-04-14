from rest_framework.generics import ListAPIView

from apps.project.models import ProjectCategory
from .serializers import ProjectCategoryListSerializer


class ProjectCategoryListAPIView(ListAPIView):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategoryListSerializer
