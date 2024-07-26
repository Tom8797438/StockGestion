from django import forms
from .models import Incoterms, Fournisseur

"""
Les formulaires de l'application
"""


class IncotermForm(forms.ModelForm):
    # formulaire pour la recherche d'incoterm
    class Meta:
        model = Incoterms
        fields = ['nom', 'definition'] 
        
class FournisseurForm(forms.ModelForm):
    # formulaire pour la recherche de fournisseur
    class Meta:
        model = Fournisseur
        fields = ['nom_fournisseur','adresse','code_postal','ville','civilite','nom','prenom','email','telephone_mobile','telephone_fixe']
