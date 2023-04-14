from rest_framework.serializers import ModelSerializer

from apps.project.models import ProjectCategory


class ProjectCategoryUpdateSerializer(ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = ('title', 'slug')
