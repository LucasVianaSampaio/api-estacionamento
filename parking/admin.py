from django.contrib import admin
from parking.models import ParkingRecord, ParkingSpot

# Register your models here.


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['spot_number', 'is_occuped']
    search_fields = ['spot_number']
    list_filter = ['is_occuped']


@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'parking_spot', 'entry_time', 'exit_time']
    search_fields = ['vehicle__licence_plate', 'parking_spot__spot_number']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parking_spot' and not request.resolver_match.url_name.endswith('change'):
            kwargs['queryset'] = ParkingSpot.objects.filter(is_occuped=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
