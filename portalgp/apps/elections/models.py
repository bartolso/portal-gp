from django.db import models
from apps.persons.models import models

class Vote(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey('persons.Person', on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()
    voted_person = models.ForeignKey('persons.Person', on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return(f"{self.person} - {self.date} {self.time}")
    