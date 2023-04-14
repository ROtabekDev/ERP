from rest_framework.serializers import ModelSerializer

from apps.project.models import Project


class ProjectUpdateSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'slug', 'client', 'project_category', 'description', 'deadline', 'status', 'price')
