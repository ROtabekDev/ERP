from rest_framework.serializers import ModelSerializer

from apps.internship.models import Intern


class InternUpdateSerializer(ModelSerializer):
    class Meta:
        model = Intern
        fields = (
            'first_name', 'last_name', 'phone_number', 'direction', 'birthday', 'age', 'gender', 'image', 'resume_file'
        )
