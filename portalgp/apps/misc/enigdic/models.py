from django.db import models
from apps.persons.models import models

# cuando un jugador cambia su carta, se guarda un CardEntry y se actualiza su item en Cards.
class CardEntry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey('persons.Person', on_delete=models.SET_NULL, null=True)
    card = models.CharField(max_length=1000, null=False, blank=False) # string de "verde", "rojo" o "gris"

# cambiar esto a "card"...
class Cards(models.Model):
    person = models.ForeignKey('persons.Person', on_delete=models.SET_NULL, null=True)
    card = models.CharField(max_length=1000, null=False, blank=False) 