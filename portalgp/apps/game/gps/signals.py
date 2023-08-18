from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import GP 
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404

from .tasks import update_streaks, update_gpv

# update_positions() se podría mover a tasks.py
@receiver(post_save, sender=GP)
def update_positions(sender, instance, **kwargs):
    same_day_gps = GP.objects.filter(date=instance.date, valid="Si", locked=False).order_by("time")
    
    position_map = {}
    
    position = 1
    for gp in same_day_gps:
        position_map[gp.pk] = position
        position += 1

    for pk, new_position in position_map.items():
        same_day_gps.filter(pk=pk).update(position=new_position)

    same_day_invalid_gps = GP.objects.filter(date=instance.date, valid__in=["Sin revisar", "No"], locked=False)

    same_day_invalid_gps.update(position=None)

@receiver(post_save, sender=GP)
def update_streaks_queue(sender, instance, **kwargs):
    update_streaks.delay(sender, instance)

@receiver(post_save, sender=GP)
def update_gpv_queue(sender, instance, **kwargs):
    update_gpv.delay(sender, instance)

post_save.connect(update_positions, sender=GP)
post_save.connect(update_streaks_queue, sender=GP)
post_save.connect(update_gpv_queue, sender=GP)