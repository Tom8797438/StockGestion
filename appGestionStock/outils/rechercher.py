from appGestionStock.models import Produit, Fournisseur, Incoterms

class RechercheProduit:
    """
    Classe pour rechercher des produits par désignation ou gamme ou fournisseur (liste déroulante).
    """

    @staticmethod
    def par_designation(designation):
        """
        Rechercher des produits par désignation.
        """
        produits = Produit.objects.filter(designation__icontains=designation)
        return produits
    
    @staticmethod
    def par_gamme (gamme):
        """
        Rechercher des produits par gamme.
        """
        produits = Produit.objects.filter(gamme__icontains=gamme)
        return produits

    @staticmethod
    def par_fournisseur(nom_fournisseur):
        """
        Rechercher des produits par fournisseur.
        """
        fournisseur = Fournisseur.objects.get(nom_fournisseur=nom_fournisseur)
        return Produit.objects.filter(fournisseur=fournisseur)
    
    @staticmethod
    def par_code_barre(code_barre):
        """
        Rechercher des produits par code barre.
        """
        produits = Produit.objects.get(code_barre__icontains=code_barre)
        return produits
    

class RechercherIncoterms:
    """
    Class pour rechercher des incoterms
    
    """
    
    @staticmethod
    def par_nom(nom):
        incoterms = Incoterm.objects.filter(nom__icontains=nom)
        return incoterms
    
    @staticmethod
    def par_definition(definition):
        incoterms = Incoterm.objects.filter(definition__icontains=definition)
        return incoterms
    