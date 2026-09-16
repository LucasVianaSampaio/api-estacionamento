from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets

from customers.filters import CustomerFilterClass
from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    rql_filter_class = CustomerFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]
