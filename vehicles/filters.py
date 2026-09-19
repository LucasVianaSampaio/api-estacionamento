from dj_rql.filter_cls import AutoRQLFilterClass

from vehicles.models import Vehicle, VehicleType


class VehicleFilterClass(AutoRQLFilterClass):
    MODEL = Vehicle
    FILTERS = (
        {
            'filter': 'vehicle_type',
            'source': 'vehicle_type__name',
        },
        {
            'filter': 'owner',
            'source': 'owner__name',
        },
    )


class VehicleTypeFilterClass(AutoRQLFilterClass):
    MODEL = VehicleType
