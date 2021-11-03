from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post)   # Afin que notre modèle (Post) soit visible dans l'interface d'administration, nous avons besoin d'enregistrer