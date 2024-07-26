"""from django.contrib import admin
from .models import Produit, Fournisseur, Incoterms, EntreeStock, SortieStock, EtatStock

admin.site.register(Produit)
admin.site.register(Fournisseur)
admin.site.register(Incoterms)
admin.site.register(EntreeStock)
admin.site.register(SortieStock)
admin.site.register(EtatStock)"""

from django.contrib import admin
from .models import Produit, Fournisseur, Incoterms

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('code_article', 'designation', 'gamme', 'prix', 'fournisseur', 'fournisseur_id')
    search_fields = ('designation', 'code_article', 'fournisseur__nom_fournisseur')

class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom_fournisseur', 'ville', 'email')
    search_fields = ('nom_fournisseur', 'ville', 'email')

class IncotermsAdmin(admin.ModelAdmin):
    list_display = ('nom', 'definition')
    search_fields = ('nom', 'definition')

admin.site.register(Produit, ProduitAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Incoterms, IncotermsAdmin)
