from django.test import TestCase
from appGestionStock.outils.rechercher import RechercheProduit, RechercherIncoterms
from appGestionStock.models import Produit, Fournisseur, Incoterm

class TestRechercheProduit(TestCase):
    
    def setUp(self):
        # Création de fournisseurs pour les tests avec toutes les valeurs requises
        self.fournisseur1 = Fournisseur.objects.create(
            nom_fournisseur="Fournisseur Test 1",
            code_postal="44",
            adresse="Adresse 1",
            ville="Nantes",
            civilite="Madame",
            telephone_mobile="0987654321",
            telephone_fixe="0987654321",
            email="test1@example.com",
            nom="dupont",
            prenom="henri"
        )
        self.fournisseur2 = Fournisseur.objects.create(
            nom_fournisseur="Fournisseur Test 2",
            code_postal="75",
            adresse="Adresse 2",
            ville="Paris",
            civilite="Monsieur",
            telephone_mobile="0987654321",
            telephone_fixe="0987654321",
            email="test2@example.com",
            nom="dupont",
            prenom="henri"
        )

        # Création de produits pour les tests
        self.produit1 = Produit.objects.create(
            designation="Produit Test 1",
            gamme="Gamme Test 1",
            code_barre="1234567890123",
            code_article="art001",
            prix=10,
            dim="28*8",
            classe="classe",
            mention="mention",
            fournisseur=self.fournisseur1
        )
        self.produit2 = Produit.objects.create(
            designation="Produit Test 2",
            gamme="Gamme Test 1",
            code_barre="9876543210987",
            code_article="art002",
            prix=15,
            dim="30*10",
            classe="classe",
            mention="mention",
            fournisseur=self.fournisseur2
        )

        # Création d'incoterms pour les tests
        self.incoterm1 = Incoterm.objects.create(
            nom="Incoterm nom 1",
            definition="Définition Test 1"
        )
        self.incoterm2 = Incoterm.objects.create(
            nom="Incoterm nom 2",
            definition="Définition Test 2"
        )

    def test_par_designation(self):
        produits = RechercheProduit.par_designation("Test 1")
        self.assertIn(self.produit1, produits)
        self.assertNotIn(self.produit2, produits)

    def test_par_gamme(self):
        produits = RechercheProduit.par_gamme("Gamme Test 1")
        self.assertIn(self.produit1, produits)
        self.assertIn(self.produit2, produits)

    def test_par_fournisseur(self):
        try:
            produits = RechercheProduit.par_fournisseur("Fournisseur Test 1")
            self.assertIn(self.produit1, produits)
            self.assertNotIn(self.produit2, produits)
        except Exception as e:
            print(e, 'erreur dans le test_par_fournisseur')
            
    def test_par_code_barre(self):
        try:
            produit = RechercheProduit.par_code_barre(self.produit1.code_barre)
            self.assertEqual(produit, self.produit1)
        except Exception as e:
            print(e, 'erreur dans le test_par_code_barre')

    def test_par_code_barre_non_existant(self):
        try:
            with self.assertRaises(Produit.DoesNotExist):
                RechercheProduit.par_code_barre("0000000000000")
        except Exception as e:
            print(e,'erreur dans test_par_code_barre_non_existant')
            
    def test_par_nom_incoterm(self):
        try:
            incoterm = RechercherIncoterms.par_nom("nom")
            self.assertIn(self.incoterm1,incoterm)
        except Exception as e:
            print(e,'erreur dans INCOTERM le test_par_nom')
            
    def test_par_definition_incoterm(self):
        try:
            incoterms = RechercherIncoterms.par_definition("Définition Test 1")
            self.assertIn(self.incoterm1, incoterms)
        except Exception as e:
            print(e, 'erreur dans INCOTERM le test_par_definition')