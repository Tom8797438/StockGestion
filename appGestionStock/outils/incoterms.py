from abc import ABC, abstractmethod
from appGestionStock.models import Incoterms

class AbstractIncoterm(ABC):
    """
    Initialiser ce que comprend un incoterm
    """
    def __init__(self, nom, definition):
        self.nom = nom 
        self.definition = definition
    
    @abstractmethod
    def afficher_details(self):
        pass
    
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, value):
        self._definition = value
        
class IncotermModifier(AbstractIncoterm):
    """
    Permet la modification d'un incoterm
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def recuperation_donnee(self, data):
        self.nom = data.get('nom')
        self.definition = data.get('definition')
        
    
        incoterm = Incoterms.objects.create(
            nom=self.nom,
            definition=self.definition
        )
        return incoterm
    
    def afficher_details(self):
        
        return (f"Nom: {self.nom}," 
                f"désignation: {self.definition}")
    
class IncotermService:
    
    @staticmethod
    def creer_incoterm(data):
        
        incoterm_modifier = IncotermModifier(
            nom=data.get('nom'),
            definition=data.get('definition')
        )
        incoterm = incoterm_modifier.recuperation_donnee(data)
        return incoterm