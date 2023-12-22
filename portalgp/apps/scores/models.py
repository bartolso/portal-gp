from django.db import models

class ScoresConfiguration(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    configuration_name = models.CharField(max_length=200)
    json_data = models.JSONField()

    def __str__(self):
        return(f"{self.configuration}")