@receiver(post_save, sender=GP)
def update_streaks(sender, instance, **kwargs):
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