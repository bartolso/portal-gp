from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import GP 
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404

from .tasks import update_streaks, update_gpv, update_positions

from .scripts.gpv import GPV

@receiver(post_save, sender=GP)
def update_positions_queue(sender, instance, **kwargs):
    update_positions.delay(sender, instance)

@receiver(post_save, sender=GP)
def update_streaks_queue(sender, instance, **kwargs):
    update_streaks.delay(sender, instance)

@receiver(post_save, sender=GP)
def update_gpv_queue(sender, instance, **kwargs):
    #update_gpv.delay(sender, instance)
    pass




post_save.connect(update_positions_queue, sender=GP)
post_save.connect(update_streaks_queue, sender=GP)
post_save.connect(update_gpv_queue, sender=GP)