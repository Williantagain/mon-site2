from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.


class etudiants(models.Model):
   l_name = models.CharField(max_length= 20)
   f_name= models.CharField(max_length=20)
   m_name = models.CharField(max_length=20)
   date_of_birth = models.DateField(null=True , blank= True)
   classe = models.CharField
   travail = models.CharField (null=True, blank= True)
   #consulter = models.CharField(null= True , blank= True)

   def stagiare (self):
       self.travail = timezone.now() # regarde ceci
       self.save()

   def __str__(self):
       return self.travail