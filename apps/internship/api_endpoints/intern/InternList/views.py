from rest_framework.generics import ListAPIView

from apps.internship.models import Intern
from .serializers import InternListSerializer


class InternListAPIView(ListAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternListSerializer
