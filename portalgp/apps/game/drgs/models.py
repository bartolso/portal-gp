from django.db import models
from apps.game.mbds.models import models
from apps.persons.models import models

class DRG(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey('persons.Person', on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()
    message = models.CharField(max_length=200)
    valid = models.CharField(max_length=20, default='Sin revisar')
    mbd = models.ForeignKey('mbds.MBD', on_delete=models.CASCADE, null=True, related_name='drg_relation', blank=True)
    locked = models.BooleanField(default=False)
    comment = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return(f"ID {self.id}: {self.date} - {self.time}")
