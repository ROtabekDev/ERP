from rest_framework.serializers import ModelSerializer

from apps.project.models import ProjectCategory


class ProjectCategoryListSerializer(ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = ('id', 'title', 'slug')
