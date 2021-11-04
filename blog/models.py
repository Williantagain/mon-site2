from django.conf import settings  #ici4
from django.db import models
from django.utils import timezone #ici4



# Create your models here.
class Post (models.Model):
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    texte = models.TextField()  # ICI blank= True , null= True 'BAS : Les types CHAR et TEXT ne sont jamais enregistrés comme NULL par Django, donc null=True n'est pas nécessaire. Cependant, vous pouvez définir manuellement l'un de ces champs sur Aucun pour le forcer à être défini sur NULL. Si vous avez un scénario où cela pourrait être nécessaire, vous devez toujours inclure null=True.'
    date_de_creation = models.DateTimeField (default= timezone.now())
    date_de_publication =models.DateTimeField(blank= True , null= True)   #methode : publication               # (blank=True) lève IntegrityError si vide,) # NULL autorisé, mais doit être rempli dans un formulaire

    def publication (self): # cest ma methode (ou action) publication  cf:ma modelisation de l'objet Post.
         self.date_de_publication = timezone.now() #  cette ligne veut dire que de 'date_de_publication' j'attend quoi? ou je veux quoi? ici par exemple , de la date de publication on veut l'heure actuel commender par 'timezone.now()'
         self.save()

    def __str__(self):
        return self.titre # ON on btiendra le text et le titre du post


class Chat(models.Model):
    color = models.CharField (blank=True, null=True, max_length=15)
    date_of_birth = models.DateTimeField(blank=True , null= True, max_length=15)
    proprietaire = models.CharField(blank=True, null=True, max_length=15) # methode: personne
    nourriture = models.CharField(blank=True, null=True , max_length=15) # methode: nourriture_pour_chat


    def personne(self):
        self.proprietaire = timezone.now() # juste pour le moment on veut la timezone et apres on va mieux modeliser
        self.save()

    def nourriture_pour_chat(self):
            self.nourriture = timezone.now()
            self.save()

    def __str__(self):
        return self.proprietaire


class Chat1(models.Model):
    color = models.CharField(blank=True, null=True, max_length=15)
    date_of_birth = models.DateTimeField(blank=True, null=True, max_length=15)
    proprietaire1 = models.CharField( blank=True, null=True, max_length=15)  # methode: personne
    nourriture = models.CharField(blank=True, null=True ,max_length=15)  # methode: nourriture_pour_chat

    def personne1(self):
        self.proprietaire1 = timezone.now()  # juste pour le moment on veut la timezone et apres on va mieux modeliser
        self.save()

    def nourriture_pour_chat1(self):
        self.nourriture=timezone.now()
        self.save()

    def __str__(self):
        return self.proprietaire1



class Chat2(models.Model):
    color = models.CharField(blank=True, null=True, max_length=15)
    date_of_birth = models.DateTimeField(blank=True, null=True , max_length=15)
    proprietaire2 = models.CharField( blank=True, null=True,max_length=15)  # methode: personne
    nourriture = models.CharField(blank=True, null=True, max_length=15)  # methode: nourriture_pour_chat

    def personne2(self):
        self.proprietaire2 = timezone.now()  # juste pour le moment on veut la timezone et apres on va mieux modeliser
        self.save()

    def nourriture_pour_chat2(self):
        self.nourriture=timezone.now()
        self.save()

    def __str__(self):
        return self.proprietaire2

