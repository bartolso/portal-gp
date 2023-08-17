from django.db import models

class ScoresConfiguration(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    setting = models.CharField()
    value = models.CharField(null=True)

    def __str__(self):
        return(f"{self.setting}")