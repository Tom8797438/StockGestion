from django.db import models

class Fournisseur(models.Model):
    nom_fournisseur = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    code_postal = models.SmallIntegerField()
    ville = models.CharField(max_length=100)
    civilite = models.CharField(max_length=50)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telephone_mobile = models.CharField(max_length=20)
    telephone_fixe = models.CharField(max_length=20)
    def __str__(self):
        return self.nom_fournisseur
    
class Produit(models.Model):
    code_barre = models.CharField(max_length=13)
    code_article = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    gamme = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    dim = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)
    mention = models.CharField(max_length=200)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

class Incoterms(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    definition = models.CharField(max_length=255)

class EntreeStock(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    date_entree = models.DateField()
    numero_commande = models.CharField(max_length=100)

class SortieStock(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    date_sortie = models.DateField()
    numero_commande_client = models.CharField(max_length=100)

class EtatStock(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    date_etat = models.DateField()

