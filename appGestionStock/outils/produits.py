from abc import ABC, abstractmethod
from appGestionStock.models import Produit, Fournisseur


class AbstractProduit(ABC):
    """
    Initialiser ce que comprend un produit
    """
    def __init__(self, code_barre, code_article, designation, gamme, prix, dim, classe, mention, fournisseur):
        self.code_barre = code_barre 
        self.code_article = code_article
        self.designation = designation
        self.gamme = gamme
        self.prix = prix
        self.dim = dim
        self.classe = classe
        self.mention = mention
        self.fournisseur = fournisseur

    @abstractmethod
    def afficher_details(self):
        pass

    @property
    def code_barre(self):
        return self._code_barre

    @code_barre.setter
    def code_barre(self, value):
        if len(value) != 13 or not value.isdigit():
            raise ValueError("Le code_barre doit être une chaîne de 13 chiffres.")
        self._code_barre = value

    @property
    def code_article(self):
        return self._code_article

    @code_article.setter
    def code_article(self, value):
        self._code_article = value

    @property
    def designation(self):
        return self._designation

    @designation.setter
    def designation(self, value):
        self._designation = value

    @property
    def gamme(self):
        return self._gamme

    @gamme.setter
    def gamme(self, value):
        self._gamme = value

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, value):
        self._prix = value

    @property
    def dim(self):
        return self._dim

    @dim.setter
    def dim(self, value):
        self._dim = value

    @property
    def classe(self):
        return self._classe

    @classe.setter
    def classe(self, value):
        self._classe = value

    @property
    def mention(self):
        return self._mention

    @mention.setter
    def mention(self, value):
        self._mention = value

    @property
    def fournisseur(self):
        return self._fournisseur

    @fournisseur.setter
    def fournisseur(self, value):
        if isinstance(value, Fournisseur):
            self._fournisseur = value
        else:
            raise ValueError("fournisseur must be an instance of Fournisseur")

class ProduitModifier(AbstractProduit):
    """
    Permet la modification d'un article
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def recuperation_donnee(self, data):
        self.code_barre = data.get('code_barre')
        self.code_article = data.get('code_article')
        self.designation = data.get('designation')
        self.gamme = data.get('gamme')
        self.prix = data.get('prix')
        self.dim = data.get('dim')
        self.classe = data.get('classe')
        self.mention = data.get('mention')
        
        fournisseur_nom = data.get('fournisseur')
        fournisseur = Fournisseur.objects.get(nom_fournisseur=fournisseur_nom)
        self.fournisseur = fournisseur
        
        produit = Produit.objects.create(
            code_barre=self.code_barre,
            code_article=self.code_article,
            designation=self.designation,
            gamme=self.gamme,
            prix=self.prix,
            dim=self.dim,
            classe=self.classe,
            mention=self.mention,
            fournisseur=self.fournisseur
        )
        return produit

    def afficher_details(self):
        return (f"Produit: {self.designation}, code_article: {self.code_article}, Prix: {self.prix}, "
                f"fournisseur: {self.fournisseur.nom_fournisseur}, code_barre: {self.code_barre}, gamme: {self.gamme}, "
                f"dim: {self.dim}, classe: {self.classe}, mention: {self.mention}")


class ProduitService:
    @staticmethod
    def creer_produit(data):
        fournisseur_id = data.get('fournisseur')
        fournisseur = Fournisseur.objects.get(id=fournisseur_id)
        
        produit_modifier = ProduitModifier(
            code_barre=data.get('code_barre'),
            code_article=data.get('code_article'),
            designation=data.get('designation'),
            gamme=data.get('gamme'),
            prix=data.get('prix'),
            dim=data.get('dim'),
            classe=data.get('classe'),
            mention=data.get('mention'),
            fournisseur=fournisseur  # Passe l'instance de Fournisseur ici
        )
        produit = produit_modifier.recuperation_donnee(data , produit)
        return produit
    
    @staticmethod
    def intégrer_produit(data):
        fournisseur_id = data.get('fournisseur')
        fournisseur = Fournisseur.objects.get(id=fournisseur_id)
        
        produit_modifier = ProduitModifier(
            code_barre=data.get('code_barre'),
            code_article=data.get('code_article'),
            designation=data.get('designation'),
            gamme=data.get('gamme'),
            prix=data.get('prix'),
            dim=data.get('dim'),
            classe=data.get('classe'),
            mention=data.get('mention'),
            fournisseur=fournisseur  # Passe l'instance de Fournisseur ici
        )
        produit = produit_modifier.recuperation_donnee(data)
        return produit
