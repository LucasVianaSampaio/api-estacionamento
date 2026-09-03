from django.contrib import admin

from vehicles.models import Vehicle, VehicleType

# Register your models here.

@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['licence_plate', 'brand', 'model', 'color', 'owner', 'vehicle_type']
    search_fields = ['licence_plate', 'model']
    list_filter = ['vehicle_type']
