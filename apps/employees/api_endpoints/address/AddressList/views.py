from rest_framework.generics import ListAPIView

from apps.employees.models import Address
from .serializers import AddressListSerializer


class AddressListAPIView(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListSerializer
