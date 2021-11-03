from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Contacts (models.Model):
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=254,)
    text = models.TextField(max_length=200, blank= True , null= True)



    def __str__(self):
        return self.phone_number