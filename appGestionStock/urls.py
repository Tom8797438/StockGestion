from django.urls import path
from appGestionStock  import views
# exemple =  path("api/dorm_recap_trimestre/", viewsDorm.dorm_recap_trimestre, name ="dorm_recap_trimestre"),
app_name = 'appGestionStock'
urlpatterns = [
    path("creer_produit/", views.creer_produit, name="creer_produit"),
    path("recherche_produit/", views.recherche_produit, name="recherche_produit"),
    path("creer_incoterms/", views.creer_incoterms, name="creer_incoterms"),
    path("rechercher_incoterms/", views.rechercher_incoterms, name="rechercher_incoterms"),
    path("modifier_incoterm/", views.modifier_incoterm, name="modifier_incoterm"),
    path("creer_fournisseur/", views.creer_fournisseur, name="creer_fournisseur"),
    path("modifier_fournisseur/", views.modifier_fournisseur, name="modifier_fournisseur"),
]