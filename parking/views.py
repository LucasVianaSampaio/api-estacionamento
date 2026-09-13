from rest_framework.permissions import DjangoModelPermissions
from rest_framework import viewsets

from parking.models import ParkingSpot, ParkingRecord
from parking.serializers import ParkingSpotSerializer, ParkingRecordSerializer

class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [DjangoModelPermissions]


class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    permission_classes = [DjangoModelPermissions]

