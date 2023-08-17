from django.db import models
from apps.game.mbds.models import models
from apps.persons.models import models
from django.db.models import F, Count, Min

class GP(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey('persons.Person', on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()
    mbd = models.ForeignKey('mbds.MBD', on_delete=models.SET_NULL, null=True, blank=True)
    position = models.IntegerField(blank=True, null=True)
    streak = models.IntegerField(blank=True, null=True)
    valid = models.CharField(max_length=20, blank=True, default='Sin revisar')
    message = models.CharField(max_length=5, blank=True, null=True)
    gpv = models.CharField(max_length=50, blank=True, null=True)
    locked = models.BooleanField(default=False)
    comment = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return(f"{self.person} - {self.date} {self.time}")
    