from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Publicites (models.Model):
    le_type = models.CharField(max_length=50, null=True, blank=True)
    nom = models.CharField(max_length=25, null=True, blank=True)
    duree = models.DurationField()

    def __str__(self):
        self.duree = timezone

        self.save()
        return self.duree
