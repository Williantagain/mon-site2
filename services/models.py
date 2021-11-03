from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Services(models.Model):
    le_type = models.CharField(max_length=50, null=True , blank= True)
    le_nom = models.CharField(max_length=50, null=True , blank= True)
    la_cible = models.CharField(max_length=25, null=True , blank= True)

    def etudiants(self):
        self.la_cible = timezone.now()
        self.save()
    def __str__(self):
        return self.la_cible
