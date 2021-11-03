from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Entreprises(models.Model):
    nom = models.CharField(max_length= 25 , null=True , blank= True)
    secteur_activites= models.CharField(max_length=25, null=True, blank=True)
    recruter = models.CharField(max_length= 25 , null=True , blank= True)


    def etudiant (self):
        self.recruter = timezone.now()
        self.save()

    def __str__(self):
        return self.recruter
