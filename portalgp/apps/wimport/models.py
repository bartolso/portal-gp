from django.db import models

class ImportRecord(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    gp_amount = models.IntegerField()
    user = models.CharField(max_length=20, null=False)

    def __str__(self):
        return(f"{self.created_at}")