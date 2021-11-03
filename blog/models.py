from django.conf import settings  #ici4
from django.db import models
from django.utils import timezone #ici4



# Create your models here.
class Post (models.Model):
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    texte = models.TextField()  # ICI blank= True , null= True 'BAS : Les types CHAR et TEXT ne sont jamais enregistrés comme NULL par Django, donc null=True n'est pas nécessaire. Cependant, vous pouvez définir manuellement l'un de ces champs sur Aucun pour le forcer à être défini sur NULL. Si vous avez un scénario où cela pourrait être nécessaire, vous devez toujours inclure null=True.'
    date_de_creation = models.DateTimeField (default= timezone.now())
    date_de_publication =models.DateTimeField(blank= True , null= True) # (blank=True) lève IntegrityError si vide,) # NULL autorisé, mais doit être rempli dans un formulaire

    def publicatoion (self):
        self.date_de_publication = timezone.now() # cest ma methode publication cf:ma modelisation de l'objet Post
        self.save()

    def __str__(self):
        return self.titre # ON on btiendra le text et le titre du post
