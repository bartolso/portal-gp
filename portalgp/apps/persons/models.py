from django.db import models

class Person(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20, null=True)

    def __str__(self):
        return(f"{self.name}")