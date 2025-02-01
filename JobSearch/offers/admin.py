from django.contrib import admin

from .models import *

class CategorieAdmin(admin.ModelAdmin):
    list_display = ["libelle"]

class OffreAdmin(admin.ModelAdmin):
    list_display = ["nom","description","recruteur"]

class CandidatAdmin(admin.ModelAdmin):
    list_display = ["nom","specialite"]


class RecruteurAdmin(admin.ModelAdmin):
    list_display = ["nom_entreprise_ou_recruteur","domaine_ou_services"]


class PostOffreAdmin(admin.ModelAdmin):
    list_display = ["offre__nom","candidat__nom"]

admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Offre,OffreAdmin)
admin.site.register(Candidat,CandidatAdmin)
admin.site.register(Recruteur,RecruteurAdmin)
admin.site.register(PostOffre,PostOffreAdmin)