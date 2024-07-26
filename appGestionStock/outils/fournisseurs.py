from abc import ABC, abstractmethod
from appGestionStock.models import Fournisseur

class AbstractFournisseur(ABC):
    """
    Initialiser ce que comprend un incoterm
    """
    def __init__(self, nom_fournisseur,adresse,code_postal,ville,civilite,nom,prenom,email,telephone_mobile,telephone_fixe):
        self.nom_fournisseur = nom_fournisseur 
        self.adresse = adresse
        self.code_postal=code_postal
        self.ville=ville
        self.civilite=civilite
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone_mobile = telephone_mobile
        self.telephone_fixe = telephone_fixe
    @abstractmethod
    def afficher_details(self):
        pass
    
    @property
    def nom_fournisseur(self):
        return self._nom_fournisseur

    @nom_fournisseur.setter
    def nom_fournisseur(self, value):
        self._nom_fournisseur = value
    
    @property
    def adresse(self):
        return self._adresse

    @adresse.setter
    def adresse(self, value):
        self._adresse = value
        
    @property
    def code_postal(self):
        return self._code_postal

    @code_postal.setter
    def code_postal(self, value):
        self._code_postal = value
    
    @property
    def ville(self):
        return self._ville

    @ville.setter
    def ville(self, value):
        self._ville = value
    
    @property
    def civilite(self):
        return self._civilite

    @civilite.setter
    def civilite(self, value):
        self._civilite = value
    
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value
        
    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, value):
        self._prenom = value
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def telephone_mobile(self):
        return self._telephone_mobile

    @telephone_mobile.setter
    def telephone_mobile(self, value):
        self._telephone_mobile = value
        
    @property
    def telephone_fixe(self):
        return self._telephone_fixe

    @telephone_fixe.setter
    def telephone_fixe(self, value):
        self._telephone_fixe = value
        
class FournisseurModifier(AbstractFournisseur):
    """
    Permet la modification d'un fournisseur
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def recuperation_donnee(self, data):
        self.nom_fournisseur =data.get('nom_fournisseur') 
        self.adresse =data.get('adresse')
        self.code_postal=data.get('code_postal')
        self.ville=data.get('ville')
        self.civilite=data.get('civilite')
        self.nom = data.get('nom')
        self.prenom =data.get('prenom')
        self.email =data.get('email')
        self.telephone_mobile = data.get('telephone_mobile')
        self.telephone_fixe =data.get('telephone_fixe')
   
        fournisseur = Fournisseur.objects.create(
            nom_fournisseur=self.nom_fournisseur, 
            adresse = self.adresse,
            code_postal = self.code_postal,
            ville=self.ville,
            civilite=self.civilite,
            nom=self.nom,
            prenom=self.prenom,
            email= self.email,
            telephone_mobile = self.telephone_mobile,
            telephone_fixe = self.telephone_fixe,
        )
        return fournisseur
    
    def afficher_details(self):
            
        return (f"Raison sociale: {self.nom_fournisseur},"
                f"Adresse: {self.adresse},"
                f"Code_postal: {self.code_postal}," 
                f"Ville: {self.ville},"
                f"Civilite: {self.civilite},"
                f"Nom: {self.nom},"
                f"Prenom: {self.prenom},"
                f"Email: {self.email},"
                f"téléphone mobile: {self.telephone_mobile}," 
                f"téléphone fixe: {self.telephone_fixe},")
    
    def afficher_details(self):
        return (f"Raison sociale: {self.nom_fournisseur}, "
                f"Adresse: {self.adresse}, "
                f"Code_postal: {self.code_postal}, " 
                f"Ville: {self.ville}, "
                f"Civilite: {self.civilite}, "
                f"Nom: {self.nom}, "
                f"Prenom: {self.prenom}, "
                f"Email: {self.email}, "
                f"téléphone mobile: {self.telephone_mobile}, " 
                f"téléphone fixe: {self.telephone_fixe}, ")
    
class FournisseurService:
    
    @staticmethod
    def creer_fournisseur(data):
        
        fournisseur_modifier = FournisseurModifier(
            nom_fournisseur =data.get('nom_fournisseur'),
            adresse =data.get('adresse'),
            code_postal=data.get('code_postal'),
            ville=data.get('ville'),
            civilite=data.get('civilite'),
            nom = data.get('nom'),
            prenom =data.get('prenom'),
            email =data.get('email'),
            telephone_mobile = data.get('telephone_mobile'),
            telephone_fixe =data.get('telephone_fixe'),
        )
        fournisseur = fournisseur_modifier.recuperation_donnee(data)
        return fournisseur