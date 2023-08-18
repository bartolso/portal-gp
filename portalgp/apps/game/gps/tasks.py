from django_rq import job
from .models import GP 
from datetime import timedelta

from .scripts.gpv import GPV

@job
def update_positions(sender, instance):
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

@job
def update_streaks(sender, instance):
    # la instancia solo se usa para seleccionar el mes concreto para actualizar
    same_month_gps = GP.objects.filter(date__month=instance.date.month, valid='Si', locked=False).order_by("date") # PONER VALID!!!!!!!!!!!!!

    list_of_names = GP.objects.values_list('person__name', flat=True).distinct()
   
    for player in list_of_names:
        player_gps = same_month_gps.filter(person__name=player)

        streak = 1
        streak_map = {}
        for gp in player_gps:
            streak_map[gp.pk] = streak
            next_date = gp.date + timedelta(days=1)
            next_day_exists = player_gps.filter(date=next_date, person__name=gp.person.name).exists()
            if next_day_exists:
                streak += 1
            else:
                streak = 1

        for pk, new_streak in streak_map.items():
            player_gps.filter(pk=pk).update(streak=new_streak)

    same_month_invalid_gps = GP.objects.filter(date__month=instance.date.month, valid__in=["No", "Sin revisar"], locked=False)

    same_month_invalid_gps.update(streak=None)

@job
def update_gpv(sender, instance):
    gp_time = instance.time #tipo datetime.time
    mbd_time = instance.mbd.time
    drg_time = instance.mbd.drg.time
    position = instance.position
    streak = instance.streak

    print("----------------------")
    print(position)
    print(streak)

    gpv = GPV(hora_gp=gp_time, hora_mbd=mbd_time, hora_drg=drg_time, puesto=position, racha=streak)

    gpv = gpv.get_gpv()

    GP.objects.filter(pk=instance.pk).update(gpv=gpv)
