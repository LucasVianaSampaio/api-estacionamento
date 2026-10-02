from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Vehicle
from .tasks import complete_vechile_data

@receiver(post_save, sender=Vehicle)
def complete_vechile_data_post_save(sender, instance, created, **kwargs):
    if created and not instance.brand or not instance.model or not instance.color:
        complete_vechile_data.delay(instance.license_plate)