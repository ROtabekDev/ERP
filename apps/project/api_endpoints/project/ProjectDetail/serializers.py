from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.project.models import Project

from apps.project.api_endpoints.client import ClientListAPIView


class ProjectDetailSerializer(ModelSerializer):
    client = ClientListAPIView()
    project_category = serializers.StringRelatedField()

    class Meta:
        model = Project
        fields = ('id', 'title', 'slug', 'client', 'project_category', 'description', 'deadline', 'status', 'price')
