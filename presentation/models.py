from django.conf import settings  #ici4
from django.db import models
from django.utils import timezone #ici4

# Create your models here.
class Presentation (models.Model):
    titre = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.titre
