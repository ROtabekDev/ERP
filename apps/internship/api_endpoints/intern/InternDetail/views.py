from rest_framework.generics import RetrieveAPIView

from apps.internship.models import Intern
from .serializers import InternDetailSerializer


class InternDetailAPIView(RetrieveAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternDetailSerializer
