from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Count  # Ajoutez cet import
from django.db.models import Count, Q 
from django.db.models import Sum


from django.contrib.auth.models import User
from django.contrib import messages
from .models import Contributions, DonneeFinanciere, DotationEleve, Ecole, Ecole_identification, GuideEtManuel
from .forms import ContributionsForm, DotationEleveForm, EcoleForm, EcoleIdentificationForm
from .models import LocaliteRurale
from .forms import LocaliteRuraleForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ecole
from .forms import EcoleForm
from .models import Local
from .forms import LocalForm
from .models import MobilierCollectif, MobilierEleve
from .forms import MobilierCollectifForm, MobilierEleveForm
from .models import EquipementDidactique
from .forms import EquipementDidactiqueForm
from .models import Personnel
from .forms import PersonnelForm
from .models import NouveauxInscrits
from .forms import NouveauxInscritsForm
from .models import DivisionPedagogique
from .forms import DivisionPedagogiqueForm
from .models import StatistiqueGenerale
from .forms import StatistiqueGeneraleForm

from .models import MobiliteEleves
from .forms import MobiliteElevesForm
from .models import AireRecrutement
from .forms import AireRecrutementForm
from .models import StructurePedagogique
from .forms import StructurePedagogiqueForm
from .models import ObservationEventuelle
from .forms import ObservationEventuelleForm
from .models import DonneeFinanciere
from .forms import DonneeFinanciereForm
from django.contrib import messages




from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from app import models

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Échec de la connexion.")
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Le nom d'utilisateur existe déjà.")
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, "Inscription réussie ! Connectez-vous maintenant.")
                return redirect('login')
        else:
            messages.error(request, "Les mots de passe ne correspondent pas.")
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def gestion_ecole(request, pk=None):
    # Si pk est fourni, on charge l'école correspondante, sinon on initialise une nouvelle école
    ecole = get_object_or_404(Ecole, pk=pk) if pk else Ecole()

    # Filtrage basé sur la recherche
    query = request.GET.get('q', '').strip()  # Supprime les espaces inutiles
    if query:
        ecoles = Ecole.objects.filter(
            Q(nom__icontains=query) | Q(nouveau_code__icontains=query)
        )
    else:
        ecoles = Ecole.objects.all()

    # Gestion du formulaire
    if request.method == "POST":
        form = EcoleForm(request.POST, instance=ecole)
        if form.is_valid():
            form.save()
            messages.success(request, "École enregistrée avec succès !")
            return redirect('gestion_ecole')  # Redirection après succès
        else:
            messages.error(request, "Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = EcoleForm(instance=ecole)

    # Rendu de la page
    return render(request, 'app/gestion_ecole.html', {
        'form': form,
        'ecoles': ecoles,
        'ecole': ecole,
        'query': query
    })
def supprimer_ecole(request, pk):
    ecole = get_object_or_404(Ecole, pk=pk)
    if request.method == "POST":
        ecole.delete()
        messages.success(request, "École supprimée avec succès !")
        return redirect('gestion_ecole')

    return render(request, 'app/confirm_delete.html', {'ecole': ecole})


def identi_ecole(request, pk=None):
    ecole_i = get_object_or_404(Ecole_identification, pk=pk) if pk else None

    # Filtrage basé sur la recherche
    query = request.GET.get('q', '')
    if query:
        identi_ecole = Ecole_identification.objects.filter(nom__icontains=query) | Ecole_identification.objects.filter(nouveau_code__icontains=query)
    else:
        identi_ecole = Ecole_identification.objects.all()

    if request.method == "POST":
        form = EcoleIdentificationForm(request.POST, instance=ecole_i)
        if form.is_valid():
            form.save()
            messages.success(request, "identification enregistrée avec succès !")
            return redirect('identification')

    else:
        form = EcoleIdentificationForm(instance=ecole_i)

    return render(request, 'app/identification.html', {
        'form': form, 
        'identi_ecole': identi_ecole, 
        'ecole_i': ecole_i, 
        'query': query
    })


def supprimer_identification(request, pk):
    identi_ecole= get_object_or_404(Ecole_identification, pk=pk)
    if request.method == "POST":
        identi_ecole.delete()
        messages.success(request, "identification supprimée avec succès !")
        return redirect('identification')

    return render(request, 'app/ide_delete.html', {'identi_ecole': identi_ecole})


# Liste, ajout et modification des localités
def gestion_localites(request, pk=None):
    localite = get_object_or_404(LocaliteRurale, pk=pk) if pk else None

    # Filtrage basé sur la recherche
    query = request.GET.get('q', '')
    if query:
        localites = LocaliteRurale.objects.filter(type_acces__icontains=query)
    else:
        localites = LocaliteRurale.objects.all()

    if request.method == "POST":
        form = LocaliteRuraleForm(request.POST, instance=localite)
        if form.is_valid():
            form.save()
            messages.success(request, "Localité enregistrée avec succès !")
            return redirect('gestion_localites')
    else:
        form = LocaliteRuraleForm(instance=localite)

    return render(request, 'app/localites.html', {
        'form': form,
        'localites': localites,
        'localite': localite,
        'query': query
    })

# Suppression des localités
def supprimer_localite(request, pk):
    localite = get_object_or_404(LocaliteRurale, pk=pk)
    if request.method == "POST":
        localite.delete()
        messages.success(request, "Localité supprimée avec succès !")
        return redirect('gestion_localites')

    return render(request, 'app/localite_delete.html', {'localite': localite})


# Vue pour gérer les mobiliers et équipements
def gestion_mobilier(request, pk=None):
    # Formulaires

    mobilier_collectif_form = MobilierCollectifForm(request.POST or None)
    mobilier_eleve_form = MobilierEleveForm(request.POST or None)

    # Traitement des formulaires
    if request.method == 'POST':
        if mobilier_collectif_form.is_valid():
            mobilier_collectif_form.save()
            return redirect('gestion_mobilier')  # Recharge la page pour afficher les changements
        elif mobilier_eleve_form.is_valid():
            mobilier_eleve_form.save()
            return redirect('gestion_mobilier')

    # Récupérer les données pour les tableaux
  
    mobiliers_collectifs = MobilierCollectif.objects.all()
    mobiliers_eleves = MobilierEleve.objects.all()

    # Contexte pour le template
    context = {
     
        'mobilier_collectif_form': mobilier_collectif_form,
        'mobilier_eleve_form': mobilier_eleve_form,
    
        'mobiliers_collectifs': mobiliers_collectifs,
        'mobiliers_eleves': mobiliers_eleves,
    }

    return render(request, 'app/mobilier.html', context)
  
# Vue pour supprimer un mobilier
def supprimer_mobilier(request, pk):
    mobilier = get_object_or_404(MobilierEtEquipements, pk=pk)
    if request.method == "POST":
        mobilier.delete()
        messages.success(request, "Mobilier supprimé avec succès !")
        return redirect('gestion_mobilier')

    return render(request, 'app/mobilier_delete.html', {'mobilier': mobilier})

# Vue pour lister, ajouter ou modifier un local
def gestion_locaux(request, pk=None):
    local = get_object_or_404(Local, pk=pk) if pk else None

    # Filtrage basé sur la recherche
    query = request.GET.get('q', '')
    if query:
        locaux = Local.objects.filter(affectation__icontains=query)
    else:
        locaux = Local.objects.all()

    if request.method == "POST":
        form = LocalForm(request.POST, instance=local)
        if form.is_valid():
            form.save()
            messages.success(request, "Local enregistré avec succès !")
            return redirect('gestion_locaux')
    else:
        form = LocalForm(instance=local)

    return render(request, 'app/locaux.html', {
        'form': form,
        'locaux': locaux,
        'local': local,
        'query': query
    })

# Vue pour supprimer un local
def supprimer_local(request, pk):
    local = get_object_or_404(Local, pk=pk)
    if request.method == "POST":
        local.delete()
        messages.success(request, "Local supprimé avec succès !")
        return redirect('gestion_locaux')

    return render(request, 'app/local_delete.html', {'local': local})

    
def gestion_equipements(request, pk=None):
    # Formulaires
    equipement_form = EquipementDidactiqueForm(request.POST or None)
    dotation_form = DotationEleveForm(request.POST or None)

    # Traitement des formulaires
    if request.method == 'POST':
        if equipement_form.is_valid():
            equipement_form.save()
            return redirect('equipements_didactiques')  # Recharge la page
        if dotation_form.is_valid():
            dotation_form.save()
            return redirect('equipements_didactiques')

    # Récupérer les données existantes
    equipements = EquipementDidactique.objects.all()
    dotation = DotationEleve.objects.first()

    context = {
        'equipement_form': equipement_form,
        'dotation_form': dotation_form,
        'equipements': equipements,
        'dotation': dotation,
    }
    return render(request, 'app/equipements.html',context)



def supprimer_equipement(request, pk):
    equipement = get_object_or_404(EquipementDidactique, pk=pk)
    if request.method == "POST":
        equipement.delete()
        messages.success(request, "Équipement supprimé avec succès !")
        return redirect('gestion_equipements')

    return render(request, 'app/equipement_delete.html', {'equipement': equipement})




from .forms import GuideEtManuelForm

def gestion_guides(request, pk=None):
    guide = get_object_or_404(GuideEtManuel, pk=pk) if pk else None

    # Filtrage par recherche
    query = request.GET.get('q', '')
    if query:
        guides = GuideEtManuel.objects.filter(niveau__icontains=query)
    else:
        guides = GuideEtManuel.objects.all()

    if request.method == "POST":
        form = GuideEtManuelForm(request.POST, instance=guide)
        if form.is_valid():
            form.save()
            messages.success(request, "Guide ou manuel enregistré avec succès !")
            return redirect('gestion_guides')
    else:
        form = GuideEtManuelForm(instance=guide)

    return render(request, 'app/guides.html', {
        'form': form,
        'guides': guides,
        'guide': guide,
        'query': query
    })



def supprimer_guide(request, pk):
    guide = get_object_or_404(GuideEtManuel, pk=pk)
    if request.method == "POST":
        guide.delete()
        messages.success(request, "Guide supprimé avec succès !")
        return redirect('gestion_guides')

    return render(request, 'app/guide_delete.html', {'guide': guide})



def gestion_personnel(request, pk=None):
    personnel = get_object_or_404(Personnel, pk=pk) if pk else None

    # Filtrage par recherche
    query = request.GET.get('q', '')
    if query:
        personnels = Personnel.objects.filter(nom__icontains=query)
    else:
        personnels = Personnel.objects.all()

    if request.method == "POST":
        form = PersonnelForm(request.POST, instance=personnel)
        if form.is_valid():
            form.save()
            messages.success(request, "Personnel enregistré avec succès !")
            return redirect('gestion_personnel')
    else:
        form = PersonnelForm(instance=personnel)

    return render(request, 'app/personnel.html', {
        'form': form,
        'personnels': personnels,
        'personnel': personnel,
        'query': query
    })

def supprimer_personnel(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)
    if request.method == "POST":
        personnel.delete()
        messages.success(request, "Personnel supprimé avec succès !")
        return redirect('gestion_personnel')

    return render(request, 'app/personnel_delete.html', {'personnel': personnel})




def gestion_inscriptions(request, pk=None):
    inscription = get_object_or_404(NouveauxInscrits, pk=pk) if pk else None

    # Recherche par filtre
    query = request.GET.get('q', '')
    inscriptions = NouveauxInscrits.objects.filter(situation_prescolaire__icontains=query) if query else NouveauxInscrits.objects.all()

    # Pagination
    paginator = Paginator(inscriptions, 10)  # Afficher 10 inscriptions par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Calculs des totaux
    total_garcons = sum(inscrit.garcons for inscrit in inscriptions)
    total_filles = sum(inscrit.filles for inscrit in inscriptions)
    total_general = total_garcons + total_filles

    # Formulaire pour ajout/mise à jour
    if request.method == "POST":
        form = NouveauxInscritsForm(request.POST, instance=inscription)
        if form.is_valid():
            form.save()
            messages.success(request, "Nouvelle inscription enregistrée avec succès !")
            return redirect('gestion_inscriptions')
        else:
            messages.error(request, "Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = NouveauxInscritsForm(instance=inscription)

    return render(request, 'app/inscriptions.html', {
        'form': form,
        'page_obj': page_obj,
        'inscription': inscription,
        'query': query,
        'total_garcons': total_garcons,
        'total_filles': total_filles,
        'total_general': total_general,
    })

def supprimer_inscription(request, pk):
    inscription = get_object_or_404(NouveauxInscrits, pk=pk)
    if request.method == "POST":
        inscription.delete()
        messages.success(request, "Inscription supprimée avec succès !")
        return redirect('gestion_inscriptions')

    return render(request, 'app/inscription_delete.html', {'inscription': inscription})





def gestion_divisions(request, pk=None):
    division = get_object_or_404(DivisionPedagogique, pk=pk) if pk else None

    # Filtrage par recherche
    query = request.GET.get('q', '')
    if query:
        divisions = DivisionPedagogique.objects.filter(niveau__icontains=query)
    else:
        divisions = DivisionPedagogique.objects.all()

    if request.method == "POST":
        form = DivisionPedagogiqueForm(request.POST, instance=division)
        if form.is_valid():
            form.save()
            messages.success(request, "Division pédagogique enregistrée avec succès !")
            return redirect('gestion_divisions')
    else:
        form = DivisionPedagogiqueForm(instance=division)

    return render(request, 'app/divisions.html', {
        'form': form,
        'divisions': divisions,
        'division': division,
        'query': query
    })

def supprimer_division(request, pk):
    division = get_object_or_404(DivisionPedagogique, pk=pk)
    if request.method == "POST":
        division.delete()
        messages.success(request, "Division supprimée avec succès !")
        return redirect('gestion_divisions')

    return render(request, 'app/division_delete.html', {'division': division})



def gestion_aires(request, pk=None):
    aire = get_object_or_404(AireRecrutement, pk=pk) if pk else None

    # Filtrage par recherche
    query = request.GET.get('q', '')
    if query:
        aires = AireRecrutement.objects.filter(localite__icontains=query)
    else:
        aires = AireRecrutement.objects.all()

    if request.method == "POST":
        form = AireRecrutementForm(request.POST, instance=aire)
        if form.is_valid():
            form.save()
            messages.success(request, "Aire de recrutement enregistrée avec succès !")
            return redirect('gestion_aires')
    else:
        form = AireRecrutementForm(instance=aire)

    return render(request, 'app/aires.html', {
        'form': form,
        'aires': aires,
        'aire': aire,
        'query': query
    })

def supprimer_aire(request, pk):
    aire = get_object_or_404(AireRecrutement, pk=pk)
    if request.method == "POST":
        aire.delete()
        messages.success(request, "Aire supprimée avec succès !")
        return redirect('gestion_aires')

    return render(request, 'app/aire_delete.html', {'aire': aire})


def gestion_statistiques(request, pk=None):
    statistique = get_object_or_404(StatistiqueGenerale, pk=pk) if pk else None

    # Filtrage par année scolaire
    query = request.GET.get('q', '')
    if query:
        statistiques = StatistiqueGenerale.objects.filter(annee_scolaire__icontains=query)
    else:
        statistiques = StatistiqueGenerale.objects.all()

    if request.method == "POST":
        form = StatistiqueGeneraleForm(request.POST, instance=statistique)
        if form.is_valid():
            form.save()
            messages.success(request, "Statistique générale enregistrée avec succès !")
            return redirect('gestion_statistiques')
    else:
        form = StatistiqueGeneraleForm(instance=statistique)

    return render(request, 'app/statistiques.html', {
        'form': form,
        'statistiques': statistiques,
        'statistique': statistique,
        'query': query
    })

def supprimer_statistique(request, pk):
    statistique = get_object_or_404(StatistiqueGenerale, pk=pk)
    if request.method == "POST":
        statistique.delete()
        messages.success(request, "Statistique supprimée avec succès !")
        return redirect('gestion_statistiques')

    return render(request, 'app/statistique_delete.html', {'statistique': statistique})



def gestion_mobilite(request, pk=None):
    mobilite = get_object_or_404(MobiliteEleves, pk=pk) if pk else None

    # Filtrage par établissement
    query = request.GET.get('q', '')
    if query:
        mobilites = MobiliteEleves.objects.filter(nom_etablissement__icontains=query)
    else:
        mobilites = MobiliteEleves.objects.all()

    if request.method == "POST":
        form = MobiliteElevesForm(request.POST, instance=mobilite)
        if form.is_valid():
            form.save()
            messages.success(request, "Mobilité enregistrée avec succès !")
            return redirect('gestion_mobilite')
    else:
        form = MobiliteElevesForm(instance=mobilite)

    return render(request, 'app/mobilite.html', {
        'form': form,
        'mobilites': mobilites,
        'mobilite': mobilite,
        'query': query
    })

def supprimer_mobilite(request, pk):
    mobilite = get_object_or_404(MobiliteEleves, pk=pk)
    if request.method == "POST":
        mobilite.delete()
        messages.success(request, "Mobilité supprimée avec succès !")
        return redirect('gestion_mobilite')

    return render(request, 'app/mobilite_delete.html', {'mobilite': mobilite})



def gestion_structures(request, pk=None):
    structure = get_object_or_404(StructurePedagogique, pk=pk) if pk else None

    # Filtrage par division
    query = request.GET.get('q', '')
    if query:
        structures = StructurePedagogique.objects.filter(division__icontains=query)
    else:
        structures = StructurePedagogique.objects.all()

    if request.method == "POST":
        form = StructurePedagogiqueForm(request.POST, instance=structure)
        if form.is_valid():
            form.save()
            messages.success(request, "Structure pédagogique enregistrée avec succès !")
            return redirect('gestion_structures')
    else:
        form = StructurePedagogiqueForm(instance=structure)
        # Calcul des totaux
    total_simples = sum(s.simples for s in structures)
    total_multigrades = sum(s.multigrades for s in structures)
    total_double_flux = sum(s.double_flux for s in structures)
    total_general = sum(s.divisions_total for s in structures)

    total_inscrits_garcons = sum(s.inscrits_garcons for s in structures)
    total_inscrits_filles = sum(s.inscrits_filles for s in structures)
    total_inscrits = sum(s.inscrits_total for s in structures)

    total_redoublants_garcons = sum(s.redoublants_garcons for s in structures)
    total_redoublants_filles = sum(s.redoublants_filles for s in structures)
    total_redoublants = sum(s.redoublants_total for s in structures)

    return render(request, 'app/structures.html', {
        'form': form,
        'structures': structures,
        'structure': structure,
        'query': query,
      'total_simples': total_simples,
        'total_multigrades': total_multigrades,
        'total_double_flux': total_double_flux,
        'total_general': total_general,
        'total_inscrits_garcons': total_inscrits_garcons,
        'total_inscrits_filles': total_inscrits_filles,
        'total_inscrits': total_inscrits,
        'total_redoublants_garcons': total_redoublants_garcons,
        'total_redoublants_filles': total_redoublants_filles,
        'total_redoublants': total_redoublants,
    })

def supprimer_structure(request, pk):
    structure = get_object_or_404(StructurePedagogique, pk=pk)
    if request.method == "POST":
        structure.delete()
        messages.success(request, "Structure supprimée avec succès !")
        return redirect('gestion_structures')

    return render(request, 'app/structure_delete.html', {'structure': structure})


def gestion_finances(request, pk=None):
    # Vérification de l'existence d'une instance de DonneeFinanciere
    finance = get_object_or_404(DonneeFinanciere, pk=pk) if pk else None

    # Filtrage : Vérifier si le champ activites_generatrices_revenus existe
    query = request.GET.get('q', '')
    if query:
        try:
            query_value = float(query)
            finances = DonneeFinanciere.objects.filter(activites_generatrices_revenus__gte=query_value)
        except ValueError:
            finances = DonneeFinanciere.objects.all()  # Si la conversion échoue, on affiche tout
    else:
        finances = DonneeFinanciere.objects.all()

    # Récupération des contributions et calcul des totaux
    contributions = Contributions.objects.all()
    totaux = Contributions.calculer_totaux()

    # Initialisation des formulaires
    form_donnee_financiere = DonneeFinanciereForm(request.POST or None, instance=finance)
    form_contributions = ContributionsForm(request.POST or None)

    if request.method == "POST":
        if form_donnee_financiere.is_valid():
            form_donnee_financiere.save()
            messages.success(request, "Les données financières ont été enregistrées avec succès !")
            return redirect('gestion_finances')

        if form_contributions.is_valid():
            form_contributions.save()
            messages.success(request, "Les contributions ont été enregistrées avec succès !")
            return redirect('gestion_finances')

    return render(request, 'app/finances.html', {
        'form_donnee_financiere': form_donnee_financiere,
        'form_contributions': form_contributions,
        'finances': finances,
        'contributions': contributions,
        'query': query,
        'total_annee_precedente': totaux['total_annee_precedente'],
        'total_annee_en_cours': totaux['total_annee_en_cours'],
    })


def supprimer_finance(request, pk):
    finance = get_object_or_404(DonneeFinanciere, pk=pk)
    if request.method == "POST":
        finance.delete()
        messages.success(request, "Finance supprimée avec succès !")
        return redirect('gestion_finances')

    return render(request, 'app/finance_delete.html', {'finance': finance})



def gestion_observations(request, pk=None):
    observation = get_object_or_404(ObservationEventuelle, pk=pk) if pk else None

    # Filtrage par contenu
    query = request.GET.get('q', '')
    if query:
        observations = ObservationEventuelle.objects.filter(contenu__icontains=query)
    else:
        observations = ObservationEventuelle.objects.all()

    if request.method == "POST":
        form = ObservationEventuelleForm(request.POST, instance=observation)
        if form.is_valid():
            form.save()
            messages.success(request, "Observation enregistrée avec succès !")
            return redirect('gestion_observations')
    else:
        form = ObservationEventuelleForm(instance=observation)

    return render(request, 'app/observations.html', {
        'form': form,
        'observations': observations,
        'observation': observation,
        'query': query
    })

def supprimer_observation(request, pk):
    observation = get_object_or_404(ObservationEventuelle, pk=pk)
    if request.method == "POST":
        observation.delete()
        messages.success(request, "Observation supprimée avec succès !")
        return redirect('gestion_observations')

    return render(request, 'app/observation_delete.html', {'observation': observation})

from django.db.models import Count, Case, When, IntegerField

def dashboard(request):
    # Statistiques des écoles
    total_ecoles = Ecole_identification.objects.count()
    ecoles_par_statut = Ecole_identification.objects.values('statut').annotate(count=Count('id'))
    ecoles_par_zone = Ecole_identification.objects.values('zone').annotate(count=Count('id'))
    
    # Statistiques des localités rurales
    total_localites = LocaliteRurale.objects.count()
    localites_par_acces = LocaliteRurale.objects.values('type_acces').annotate(count=Count('id'))
    localites_services = LocaliteRurale.objects.aggregate(
        electricite=Count('id', filter=Q(electricite_disponible=True)),
        sante=Count('id', filter=Q(service_sante_disponible=True))
    )    # **Statistiques des écoles**
    total_ecoles = Ecole.objects.count()
    ecoles_par_statut = Ecole.objects.values('info_ecole').annotate(count=Count('id'))
    ecoles_eau = Ecole.objects.filter(eau_disponible=True).count()
    ecoles_electricite = Ecole.objects.filter(electricite_disponible=True).count()

    # **Statistiques des locaux**
    total_locaux = Local.objects.count()
    locaux_surface_totale = Local.objects.aggregate(total_surface=Sum('surface'))['total_surface']
    

    context = {
        'total_ecoles': total_ecoles,
        'ecoles_par_statut': ecoles_par_statut,
        'ecoles_par_zone': ecoles_par_zone,
        'total_localites': total_localites,
        'localites_par_acces': localites_par_acces,
        'localites_services': localites_services,
        'total_ecoles': total_ecoles,
        'ecoles_par_statut': ecoles_par_statut,
        'ecoles_eau': ecoles_eau,
        'ecoles_electricite': ecoles_electricite,
        'total_locaux': total_locaux,
        
        'locaux_surface_totale': locaux_surface_totale,
    }
    return render(request, 'app/dashboard.html', context)