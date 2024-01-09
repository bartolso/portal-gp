from django.db import models
from django.utils import timezone
from apps.persons.models import models

# cuando un jugador cambia su carta, se guarda un CardEntry y se actualiza su item en Cards.
class CardEntry(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    person = models.ForeignKey('persons.Person', on_delete=models.SET_NULL, null=True)
    card = models.CharField(max_length=1000, null=False, blank=False) # string de "verde", "rojo" o "gris"

# cambiar esto a "card"...
class Cards(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.SET_NULL, null=True)
    card = models.CharField(max_length=1000, null=False, blank=False)

# almacena un tal para cada puntuacion obtenida. para calcular la puntuación final se suman todos los scores de un jugador.
class UserScore(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.SET_NULL, null=True)
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)
    turn = models.ForeignKey('enigdic.Turn', on_delete=models.SET_NULL, null=True)

class Prisopunto(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.SET_NULL, null=True)
    score = models.IntegerField(default=0)

class Turn(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    number = models.IntegerField(null=False)

class Log(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    json = models.JSONField()

class Enigma(models.Model):
    question = models.CharField(max_length=100000, null=False, blank=False)
    answers = models.JSONField()
    completed_by = models.ForeignKey('persons.Person', on_delete=models.SET_NULL, null=True)
    completed_at = models.DateTimeField()