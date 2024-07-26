from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from appGestionStock.outils.produits import ProduitService
from appGestionStock.outils.fournisseurs import FournisseurService
from .models import Incoterms, Fournisseur, Produit
from .forms import IncotermForm, FournisseurForm
from appGestionStock.outils.rechercher import RechercheProduit, RechercherIncoterms
from appGestionStock.outils.incoterms import IncotermService


@csrf_exempt
def creer_produit(request):
    context = {}
    if request.method == "POST":
        data = {
            'code_barre': request.POST.get('code_barre'),
            'code_article': request.POST.get('code_article'),
            'designation': request.POST.get('designation'),
            'gamme': request.POST.get('gamme'),
            'prix': request.POST.get('prix'),
            'dim': request.POST.get('dim'),
            'classe': request.POST.get('classe'),
            'mention': request.POST.get('mention'),
            'fournisseur': request.POST.get('fournisseur')  # ID du fournisseur
        }
        produit = ProduitService.creer_produit(data)
        context['produit'] = produit
        context['message'] = "Produit créé avec succès"
    
    fournisseurs = Fournisseur.objects.all()
    context['fournisseurs'] = fournisseurs
    
    return render(request, 'creer_produit.html', context)


@csrf_exempt
def recherche_produit(request):
    designation = request.GET.get('designation', '')
    fournisseur_nom = request.GET.get('fournisseur', '')
    gamme = request.GET.get('gamme', '')
    code_barre = request.GET.get('code_barre', '')

    produits_par_designation = RechercheProduit.par_designation(designation) if designation else None
    produits_par_fournisseur = RechercheProduit.par_fournisseur(fournisseur_nom) if fournisseur_nom else None
    produits_par_gamme = RechercheProduit.par_gamme(gamme) if gamme else None
    produits_par_code_barre = RechercheProduit.par_code_barre(code_barre) if code_barre else None
    fournisseurs = Fournisseur.objects.all()
    context = {
        'produits_par_designation': produits_par_designation,
        'produits_par_fournisseur': produits_par_fournisseur,
        'produits_par_gamme': produits_par_gamme,
        'produits_par_code_barre': produits_par_code_barre,
        'fournisseurs': fournisseurs,
    }
   
    return render(request, 'recherche_produit.html', context)


@csrf_exempt
def creer_incoterms(request):
    context = {}
    if request.method == "POST":
        data = {
            'nom': request.POST.get('nom'),
            'definition': request.POST.get('definition')
        }
        try:
            incoterm = IncotermService.creer_incoterm(data)
            context['incoterm'] = incoterm
            context['message'] = "Incoterm créé avec succès"
        except Exception as e:
            context['message'] = f"Erreur : {e}"
    
    return render(request, 'creer_incoterm.html', context)


@csrf_exempt
def rechercher_incoterms(request):
    nom = request.GET.get('nom','')
    definition = request.GET.get('definition','')
    
    incoterms_par_nom = RechercherIncoterms.par_nom(nom) if nom else None
    incoterms_par_definition = RechercherIncoterms.par_definition(definition) if definition else None
    
    incoterms = Incoterms.objects.all()
    
    context = {
        'incoterms_par_nom': incoterms_par_nom,
        'incoterms_par_definition': incoterms_par_definition,
        'incoterms': incoterms
    }
        
    return render(request, 'appGestionStock/recherche_produit.html', context)


@csrf_exempt
def modifier_incoterm(request):
    context = {}
    incoterms = Incoterms.objects.all()  # Récupérer tous les incoterms pour la liste déroulante
    context['incoterms'] = incoterms

    if request.method == 'POST':
        incoterm_id = request.POST.get('incoterms')
        if incoterm_id:
            incoterm = get_object_or_404(Incoterms, pk=incoterm_id)
            form = IncotermForm(request.POST, instance=incoterm)
            if form.is_valid():
                form.save()
                context['message'] = "Incoterm modifié avec succès"
            else:
                context['message'] = "Erreur lors de la modification de l'incoterm"
        else:
            form = IncotermForm()  # éviter l'erreur si incoterm_id n'est pas fourni
            context['message'] = "Veuillez sélectionner un incoterm"
    else:
        form = IncotermForm()  # initialiser le formulaire en cas de GET

    context['form'] = form
    return render(request, 'modifier_incoterm.html', context)


@csrf_exempt
def creer_fournisseur(request):
    context = {}
    context['fournisseur'] = None  # Initialise la variable fournisseur à None
    if request.method == "POST":
        form = FournisseurForm(request.POST)
        if form.is_valid():
            fournisseur = form.save()
            context['fournisseur'] = fournisseur
            context['message'] = "Fournisseur créé avec succès"
        else:
            context['message'] = "Erreur lors de la création du fournisseur"
            context['errors'] = form.errors  # Ajoutez cette ligne pour afficher les erreurs de formulaire
    else:
        form = FournisseurForm()

    context['form'] = form
    return render(request, 'fournisseurs.html', context)


@csrf_exempt
def modifier_fournisseur(request):
    context = {}
    fournisseurs = Fournisseur.objects.all()  # Récupérer tous les fournisseurs pour la liste déroulante
    context['fournisseurs'] = fournisseurs

    if request.method == 'POST':
        # Vérifiez si le formulaire de sélection du fournisseur a été soumis
        if 'fournisseur' in request.POST:
            fournisseur_id = request.POST.get('fournisseur')
            if fournisseur_id:
                fournisseur = get_object_or_404(Fournisseur, pk=fournisseur_id)
                form = FournisseurForm(instance=fournisseur)
                context['selected_fournisseur'] = fournisseur
            else:
                form = FournisseurForm()
        else:
            # Vérifiez si le formulaire de modification du fournisseur a été soumis
            fournisseur_id = request.POST.get('fournisseur_id')
            if fournisseur_id:
                fournisseur = get_object_or_404(Fournisseur, pk=fournisseur_id)
                form = FournisseurForm(request.POST, instance=fournisseur)
                if form.is_valid():
                    form.save()
                    context['message'] = "Fournisseur modifié avec succès"
                    # Recharge les données du fournisseur modifié
                    fournisseur = get_object_or_404(Fournisseur, pk=fournisseur_id)
                    form = FournisseurForm(instance=fournisseur)
                    context['selected_fournisseur'] = fournisseur
                else:
                    context['message'] = "Erreur lors de la modification du fournisseur"
                    context['selected_fournisseur'] = fournisseur
            else:
                context['message'] = "Veuillez sélectionner un fournisseur"
                form = FournisseurForm()  # Initialiser le formulaire vide
    else:
        form = FournisseurForm()  # Initialiser le formulaire vide

    context['form'] = form
    return render(request, 'modifier_fournisseur.html', context)


@csrf_exempt
def entree_stock(request,creer_produit):
    context = {}
    if request.method == "POST":
        data = {
            'code_barre': request.POST.get('code_barre'),
            'code_article': request.POST.get('code_article'),
            'designation': request.POST.get('designation'),
            'gamme': request.POST.get('gamme'),
            'prix': request.POST.get('prix'),
            'dim': request.POST.get('dim'),
            'classe': request.POST.get('classe'),
            'mention': request.POST.get('mention'),
            'fournisseur': request.POST.get('fournisseur')  # ID du fournisseur
        }
        produit = ProduitService.creer_produit(data)
        context['produit'] = produit
        context['message'] = "Produit créé avec succès"
    
    fournisseurs = Fournisseur.objects.all()
    context['fournisseurs'] = fournisseurs
    
    return render(request, 'creer_produit.html', context)