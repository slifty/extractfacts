from django.db import models

# Create your models here.

class Speak(models.Model):
    claim = models.TextField(blank=True, null=True)
    speaker = models.TextField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    trans_id = models.TextField(blank=True, null=True)
    claim_id = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'speak'