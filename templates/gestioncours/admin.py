from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Filiere)

admin.site.register(models.Enseignant)
admin.site.register(models.Etudiant)
admin.site.register(models.Pfe)
admin.site.register(models.Classe)
admin.site.register(models.Matiere)
admin.site.register(models.Examen)
admin.site.register(models.Ressource)
admin.site.register(models.Module)
admin.site.register(models.Cours)
admin.site.register(models.Salle)
admin.site.register(models.Emploi)
