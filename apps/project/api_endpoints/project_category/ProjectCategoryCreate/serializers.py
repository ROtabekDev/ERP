from rest_framework.serializers import ModelSerializer

from apps.project.models import ProjectCategory


class ProjectCategoryCreateSerializer(ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = ('title', 'slug')
