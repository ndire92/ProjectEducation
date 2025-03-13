from django import forms
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
#identification et de localisation d'une éco
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # Définir un related_name unique
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Définir un related_name unique
        blank=True
    )


class Ecole_identification(models.Model):
    ancien_code = models.IntegerField(max_length=50, null=True, blank=True)  # Ancien code de l'école
    nouveau_code = models.IntegerField(max_length=50, null=True, blank=True)  # Nouveau code de l'école
    nom = models.CharField(max_length=200)  # Nom de l'école
    ancien_nom = models.CharField(max_length=200, null=True, blank=True)  # Ancien nom de l'école
    date_creation = models.DateField(null=True, blank=True)  # Date de création de l'école
    statut = models.CharField(max_length=20, choices=[
        ('public', 'Public'),
        ('prive', 'Privé')
    ], null=True, blank=True)  # Statut de l'école
    

    Localisation_administrative = models.CharField(max_length=20, choices=[
    ('wilaya', 'Wilaya'),
    ('moughataa', 'Moughataa'),  # Added comma here
    ('commune', 'Commune'),
    ('localite', 'Localite')
], null=True, blank=True)  # Zone de localisation (Rurale/Urbaine)


    

    Localisation_scolaire = models.CharField(max_length=20, choices=[
        ('dren', 'dren'),
        ('iden', 'iden')
    ], null=True, blank=True)  
    
    zone = models.CharField(max_length=20, choices=[
        ('rurale', 'Rurale'),
        ('urbaine', 'Urbaine')
    ], null=True, blank=True)  # Zone de localisation (Rurale/Urbaine)
    
    
    def __str__(self):
        return self.nom

#-------------------l'environnement socio-économique des localités-----------------

# Définition des choix en dehors de la classe
ACTIVITES_CHOICES = [
    ('cultures_vivrières', 'Cultures vivrières'),
    ('elevage', 'Élevage'),
    ('cultures_maraîchères', 'Cultures maraîchères'),
    ('peche', 'Pêche'),
    ('cultures_fruitières', 'Cultures fruitières'),
    ('artisanat', 'Artisanat'),
    ('cultures_industrielles', 'Cultures industrielles'),
    ('autres', 'Autres'),
]

class LocaliteRurale(models.Model):
    type_acces = models.CharField(max_length=100, choices=[
        ('route_goudronnee', 'Route goudronnée'),
        ('route_bitumee', 'Route bitumée'),
        ('accessible_tous_vehicules', 'Piste accessible à tous véhicules'),
        ('vehicule_tout_terrain', 'Piste accessible véhicule tout terrain'),
        ('uniquement_pied', 'Accessible uniquement à pied'),
        ('autre', 'Autre accès (à préciser)')
    ])

    electricite_disponible = models.BooleanField()
    type_eau = models.CharField(max_length=100, choices=[
        ('robinets', 'Robinets'),
        ('puits_cloture', 'Puits clôturés ou avec margelle'),
        ('puits_non_cloture', 'Puits non clôturés sans margelle'),
        ('citerne', 'Citerne'),
        ('eaux_surface', 'Fleuve, mare, marigot'),
        ('forage', 'Forage')
    ])

    service_sante_disponible = models.BooleanField()
    type_service_sante = models.CharField(max_length=100, choices=[
        ('poste', 'Poste de santé'),
        ('unite_base', 'Unité de santé de base'),
        ('autres', 'Autres services de santé')
    ], null=True, blank=True)

    mosquee_disponible = models.BooleanField()
    mahadra_disponible = models.BooleanField()
    bibliotheque_disponible = models.BooleanField()
    terrain_sport_disponible = models.BooleanField()
    autres_structures_animation = models.TextField(null=True, blank=True)

    # Utilisation de ManyToManyField pour plusieurs choix
    activites_dominantes = models.ManyToManyField(
        'Activite',  # Modèle pour stocker les activités
        related_name="localites",
        help_text="Sélectionnez jusqu'à trois activités économiques dominantes."
    )

    type_marche = models.CharField(max_length=100, choices=[
        ('permanent', 'Permanent'),
        ('hebdomadaire', 'Hebdomadaire'),
        ('absent', 'Pas de marché')
    ])

    type_de_coperation = models.CharField(max_length=100, choices=[
        ('agricole', 'Agricole'),
        ('pastoral', 'Pastoral'),
        ('artisanal', 'Artisanal'),
        ('autre', 'Autres')
    ])

    developpe_socio_économique = models.BooleanField()
    secteur_intervention = models.CharField(max_length=100, choices=[
        ('agricole', 'Agricole'),
        ('pastoral', 'Pastoral'),
        ('hydraulique', 'Hydraulique'),
        ('sante', 'Santé'),
        ('educatif', 'Éducatif'),
        ('artisanal', 'Artisanal'),
    ], null=True, blank=True)

    bailleurs_ong = models.TextField(null=True, blank=True)
    
    def clean_activites_dominantes(self):
        activites = self.cleaned_data.get('activites_dominantes')
        if activites.count() > 3:
            raise forms.ValidationError("Vous ne pouvez sélectionner que trois activités économiques dominantes.")
        
        return activites


    def __str__(self):
        return f"Localité rurale - Accès {self.type_acces}"


class Activite(models.Model):
    nom = models.CharField(max_length=100, choices=ACTIVITES_CHOICES, unique=True)

    def __str__(self):
        return self.get_nom_display()
#----------------------------INFORMATIONS GÉNÉRALES SUR L'ÉCOLE----------------------------
ACTIVITES_APE_CHOICES = [
    ('construction', 'Construction'),
    ('réhabilitation', 'Réhabilitation'),
    ('suivi_présence_des_enseignants', 'Suivi présence des enseignants'),
    ('Activités_de_sensibilisation', 'Activités de sensibilisation'),
    ('cantine', 'Cantine'),
    ('autres', 'Autres'),
]

class Ecole(models.Model):
    nom = models.CharField(max_length=200)  # Nom de l'école
    info_ecole = models.CharField(max_length=20, choices=[
        ('ouverte', 'ouverte'),
        ('veilleuse', 'Veilleuse')
    ], null=True, blank=True)  # Statut de l'école

    accessible_toute_annee = models.BooleanField()  # Accessible toute l'année

    # Ressources
    eau_disponible = models.BooleanField()  # École alimentée en eau
    type_eau = models.CharField(max_length=20, choices=[
        ('robiet', 'Robiet'),
        ('citerne', 'Citerne'),
        ('puits_avec_cloture', 'Puits avec cloture'),
        ('puits_avec_margelle', 'Puits avec margelle'),
    ], null=True, blank=True)
    nb_postes_eau = models.IntegerField(null=True, blank=True)  # Nombre de postes d'eau
    electricite_disponible = models.BooleanField()  # Électricité disponible
    nb_classes_electrifiees = models.IntegerField(null=True, blank=True)

    # Infrastructures
    cantine_fonctionnelle = models.BooleanField()
    nb_rationnaires = models.IntegerField(null=True, blank=True)  # Nombre de rationnaires
    nb_de_fille_beneficiaires = models.IntegerField(null=True, blank=True)
    source_financement = models.CharField(max_length=20, choices=[
        ('gvt', 'GVT'),
        ('pam', 'PAM'),
        ('autres', 'Autres'),
    ], null=True, blank=True)  # Ex : Gvt, PAN, etc.
    laves_mains_disponibles = models.BooleanField()
    nb_laves_mains = models.IntegerField(null=True, blank=True)
    domaine_cloture = models.BooleanField()  # Domaine scolaire clôturé
    superficie_cloture = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    type_cloture = models.CharField(max_length=20, choices=[
        ('dur', 'Dur'),
        ('banco', 'Banco'),
        ('haie', 'Haie'),
        ('grillage', 'Grillage'),
        ('semi_dur', 'Semi-dur'),
    ], null=True, blank=True)

    espace_recreation_disponible = models.BooleanField()
    superficie_recreation = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Superficie en m²
    jardin_scolaire = models.BooleanField()
    utilisation_de_la_produit = models.CharField(max_length=20, choices=[
        ('vendu', 'Vendu'),
        ('distribue', 'Distribue'),
        ('cantine', 'Cantine'),
    ], null=True, blank=True)  # Utilisation de la production

    # Sanitaires
    nb_total_latrines = models.IntegerField(null=True, blank=True)
    nb_latrines_filles = models.IntegerField(null=True, blank=True)
    nb_latrines_garcons = models.IntegerField(null=True, blank=True)
    nb_latrines_mixt = models.IntegerField(null=True, blank=True)

    # Gouvernance
    ape_existe = models.BooleanField()  # APE (Association des Parents d'Élèves) existe
    femmes_ape = models.IntegerField(null=True, blank=True)
    hommes_ape = models.IntegerField(null=True, blank=True)
    activites_ape = models.ManyToManyField(
        'Activite_APE',
        related_name="ecoles",
        help_text="Sélectionnez jusqu'à trois activités."
    )  # Modèle pour stocker les activités

    presidence_ape = models.CharField(max_length=20, choices=[
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    ], null=True, blank=True)  # Normaliser 'Femme' en 'femme'
    
    comite_gestion_existe = models.BooleanField()
    femmes_comite = models.IntegerField(null=True, blank=True)
    hommes_comite = models.IntegerField(null=True, blank=True)
    presidence_comite = models.CharField(max_length=20, choices=[
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    ], null=True, blank=True)

    # Autres
    distance_centre_sante = models.IntegerField(null=True, blank=True)  # Distance en km
    apport_en_vitamine_A = models.BooleanField()  # Supprimer la duplication de ce champ
    boite_pharmacie_disponible = models.BooleanField()
    visite_médicale_année_dernière = models.BooleanField()
    campagne_de_déparasitage = models.BooleanField()
    campagne_de_sensibilisation_au_VIH = models.BooleanField()  # Sensibilisation au VIH
    campagne_de_sensibilisation_au_palu = models.BooleanField()
    association_eleve = models.BooleanField()

    def __str__(self):
        return self.nom
    
    
class Activite_APE(models.Model):
    nom = models.CharField(max_length=100, choices=ACTIVITES_APE_CHOICES, unique=True)

    def __str__(self):
        return self.get_nom_display()

#----------------------------------------CARACTÉRISTIQUES ET ÉTAT DES LOCAUX---------------------------
Affectation = [
    ('Salle_de_classe_utiliseé', 'Salle de classe utiliseé'),
    ('salle_de_classe _non_utiliseé', 'Salle de classe  non utiliseé'),
    ('magasin_pédagogique', 'Magasin pédagogique'),
    (' magasin alimantaire', 'Magasin alimantaire'),
    ('Bureau_directeur', 'Bureau directeur'),
    ('logement', 'Logement'),
    ('réfectoire', 'Réfectoire'),
]
DONT= [
    ('Salle_autre_école', 'Salle autre école'),
    ('Local_emprunté_loué', 'Local emprunté / loué'),

]
Nature_Murs= [
    ('en_dur', 'En dur'),
    ('semi_dur', 'Semi dur'),
    ('banco', 'Banco'),
    ('paillotes', 'Paillotes'),
    ('autres', 'Autres'),

]
Etat_Murs= [
    ('bon_acceptable', 'Bon / acceptable'),
    ('mauvais', 'Mauvais'),

]

Nature_Toit= [
    ('dur', 'Dur'),
    ('tole', 'Tole'),
    ('chaume', 'Chaume'),
    ('autres', 'Autres'),

]

Etat_Toit= [
    ('bon_acceptable', 'Bon / acceptable'),
    ('mauvais', 'Mauvais'),

]
Nature_Sol= [
    ('ciment', 'Ciment'),
    ('terre', 'Terre'),
    ('autres', 'Autres'),

]
Etat_Sol= [
    ('bon_acceptable', 'Bon / acceptable'),
    ('mauvais', 'Mauvais'),

]
Etat_Porte= [
    ('bon_acceptable', 'Bon / acceptable'),
    ('mauvais', 'Mauvais'),
    ('Non_installées', 'Non installées'),

]
Etat_Fe= [
    ('bon_acceptable', 'Bon / acceptable'),
    ('mauvais', 'Mauvais'),
    ('Non_installées', 'Non installées'),
    

]
Source_Fe= [
    ('etat', 'Etat'),
    ('commune', 'Commune'),
    ('parents', 'Parents'),
    

]
from django.db import models

class Affec(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class Do(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class NatureMur(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class EtatMur(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class NatureToit(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class EtatToit(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class NatureSol(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class EtatSol(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class EtatPorte(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class EtatFenetre(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class SourceFinancement(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class Local(models.Model):
    numero = models.IntegerField(unique=True)  # Numéro du local
    affectation_du_local = models.ManyToManyField(Affec, related_name="locaux")
    dont = models.ManyToManyField(Do, related_name="locaux")
    annee_mise_en_service = models.IntegerField(null=True, blank=True)
    surface = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Surface en m²

    # Caractéristiques physiques
    nature_murs = models.ManyToManyField(NatureMur, related_name="locaux")
    etat_murs = models.ManyToManyField(EtatMur, related_name="locaux")
    nature_toit = models.ManyToManyField(NatureToit, related_name="locaux")
    etat_toit = models.ManyToManyField(EtatToit, related_name="locaux")
    nature_sol = models.ManyToManyField(NatureSol, related_name="locaux")
    etat_sol = models.ManyToManyField(EtatSol, related_name="locaux")

    # Portes et fenêtres
    etat_portes = models.ManyToManyField(EtatPorte, related_name="locaux")
    etat_fenetres = models.ManyToManyField(EtatFenetre, related_name="locaux")

    # Source de financement
    source_financement = models.ManyToManyField(SourceFinancement, related_name="locaux")

    # Observations supplémentaires
    observations = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Local nº{self.numero}"


#----------------------------------CARACTÉRISTIQUES  DU MOBILIER ET DES ÉQUIPEMENTS---------------------------

ETAT_CHOIX = [
    ('bon_acceptable', 'Bon / acceptable'),
    ('mauvais', 'Mauvais'),
]

# Choix pour les types de mobiliers des élèves
TYPE_TABLE_BANC = [
    ('1_place', '1 place'),
    ('2_places', '2 places'),
    ('4_places', '4 places'),
]

class MobilierCollectif(models.Model):
    # Mobilier et équipements collectifs
    nom = models.CharField(max_length=100)  # Exemple : Tableau, Bureau de maître
    etat = models.CharField(max_length=20, choices=ETAT_CHOIX)
    nombre = models.PositiveIntegerField(default=0)  # Quantité

    def __str__(self):
        return f"{self.nom} - {self.etat} ({self.nombre})"


class MobilierEleve(models.Model):
    # Mobilier pour les élèves
    type_table_banc = models.CharField(max_length=10, choices=TYPE_TABLE_BANC)  # Exemple : 1 place, 2 places
    etat = models.CharField(max_length=20, choices=ETAT_CHOIX)
    nombre = models.PositiveIntegerField(default=0)  # Quantité



#-----------------------------------ÉQUIPEMENTS DIDACTIQUES--------------------------


class EquipementDidactique(models.Model):
    # Équipements collectifs
    regles = models.IntegerField(null=True, blank=True)  # Nombre de règles
    rapporteurs = models.IntegerField(null=True, blank=True)  # Nombre de rapporteurs
    cartes = models.IntegerField(null=True, blank=True)  # Nombre de cartes
    bandes_dessinees = models.IntegerField(null=True, blank=True)  # Nombre de bandes dessinées
    planches = models.IntegerField(null=True, blank=True)  # Nombre de planches
    compas = models.IntegerField(null=True, blank=True)  # Nombre de compas
    equerres = models.IntegerField(null=True, blank=True)  # Nombre d'équerres
    globes = models.IntegerField(null=True, blank=True)  # Nombre de globes terrestres
    litres = models.IntegerField(null=True, blank=True)  # Nombre d'objets pour les mesures (litres)

    # État du matériel collectif
    bon_etat = models.IntegerField(null=True, blank=True)  # Nombre en bon état
    mauvais_etat = models.IntegerField(null=True, blank=True)  # Nombre en mauvais état

    # Dotation scolaire des élèves
    eleves_dotes = models.IntegerField(null=True, blank=True)  # Nombre d'élèves dotés cette année (sac, cahiers, etc.)

    def __str__(self):
        return f"Équipements didactiques - ID {self.id}"

class GuideEtManuel(models.Model):
    # Niveaux scolaires
    niveau = models.CharField(max_length=10, choices=[
        ('1A', '1ère Année'),
        ('2A', '2ème Année'),
        ('3A', '3ème Année'),
        ('4A', '4ème Année'),
        ('5A', '5ème Année'),
        ('6A', '6ème Année')
    ])
    matiere = models.CharField(max_length=100, choices=[
        ('lecture', 'Lecture'),
        ('calcul', 'Calcul'),
        ('science', 'Science'),
        ('histoire', 'Histoire'),
        ('geographie', 'Géographie'),
        ('education_islamique', 'Éducation Islamique'),
        ('instruction_civique', 'Instruction Civique')
    ])
    langue = models.CharField(max_length=50, choices=[
        ('arabe', 'Arabe'),
        ('francais', 'Français')
    ])
    guides = models.IntegerField(null=True, blank=True)  # Nombre de guides
    manuels = models.IntegerField(null=True, blank=True)  # Nombre de manuels

    def __str__(self):
        return f"{self.niveau} - {self.matiere} ({self.langue})"
#---------------------------------------------informations relatives au personnel---------------------------


class Personnel(models.Model):
    nom = models.CharField(max_length=200)  # Nom de la personne
    genre = models.CharField(max_length=1, choices=[('H', 'Homme'), ('F', 'Femme')])  # Genre
    age = models.IntegerField(null=True, blank=True)  # Âge
    fonction = models.CharField(max_length=200)  # Fonction (par exemple : enseignant, directeur)
    
    # Formation
    niveau_formation = models.CharField(max_length=200, null=True, blank=True)  # Niveau de formation
    formation_continue = models.BooleanField(default=False)  # A participé à une formation continue
    
    def __str__(self):
        return f"{self.nom} - {self.fonction}"

#---------------------------------répartition des nouveaux inscrits----------------------------

class NouveauxInscrits(models.Model):
    situation_prescolaire = models.CharField(max_length=100)  # Ex : Garderie, Jardins d'enfants, etc.
    nombre_garcons = models.IntegerField()  # Nombre de garçons inscrits
    nombre_filles = models.IntegerField()  # Nombre de filles inscrites
    total_inscrits = models.IntegerField()  # Total des inscrits

    def __str__(self):
        return f"{self.situation_prescolaire} - Total : {self.total_inscrits}"


#-----------------------------RÉPARTITION DES ÉLEVES PAR DIVISION PÉDAGOGIQUE----------------------------------



class DivisionPedagogique(models.Model):
    niveau = models.CharField(max_length=100)  # Niveau d'étude (ex : CP, CE1, etc.)
    numero_salle = models.IntegerField(null=True, blank=True)  # Numéro de la salle de classe
    vacation = models.CharField(max_length=50, choices=[('simple', 'Simple'), ('double', 'Double')], null=True, blank=True)
    multigrade = models.BooleanField(default=False)  # Si la division est multigrade
    double_flux = models.BooleanField(default=False)  # Si c'est une classe à double flux

    # Répartition des élèves par âge et sexe
    age_6_ans = models.JSONField(null=True, blank=True)  # Structure détaillée (ex : {"garcons": 5, "filles": 4})
    age_7_ans = models.JSONField(null=True, blank=True)
    age_8_ans = models.JSONField(null=True, blank=True)
    # Ajoutez les autres groupes d'âge ici...

    total_eleves = models.IntegerField(null=True, blank=True)  # Total des élèves
    redoublants = models.IntegerField(null=True, blank=True)  # Nombre de redoublants

    def __str__(self):
        return f"{self.niveau} - Classe nº{self.numero_salle}"

#--------------------------Aire Recrutement----------------------------

class AireRecrutement(models.Model):
    localite = models.CharField(max_length=200)  # Nom de la localité ou du quartier
    distance_km = models.FloatField(null=True, blank=True)  # Distance estimée de l'école (en km)
    nombre_eleves_garcons = models.IntegerField(default=0)  # Total garçons
    nombre_eleves_filles = models.IntegerField(default=0)  # Total filles
    total_eleves = models.IntegerField(default=0)  # Total élèves (garçons + filles)
    redoublants_garcons = models.IntegerField(default=0)  # Garçons redoublants
    redoublants_filles = models.IntegerField(default=0)  # Filles redoublantes

    def __str__(self):
        return f"{self.localite} ({self.distance_km} km)"

class StatistiqueGenerale(models.Model):
    annee_scolaire = models.CharField(max_length=10)  # Année scolaire (ex. 2024/2025)
    total_inscrits = models.IntegerField(default=0)  # Nombre total des inscrits
    total_redoublants = models.IntegerField(default=0)  # Total redoublants

    def __str__(self):
        return f"Statistiques - Année : {self.annee_scolaire}"



#------------------------------Mobilite Eleves------------------------------


class MobiliteEleves(models.Model):
    nom_etablissement = models.CharField(max_length=200)  # Nom de l'établissement fréquenté
    localite_origine = models.CharField(max_length=200)  # Localité d'origine (exemple : Wilaya, commune)
    pays_origine = models.CharField(max_length=100, null=True, blank=True)  # Pays d'origine (si étranger)
    statut_scolarisation = models.CharField(
        max_length=50,
        choices=[
            ('scolarisé', 'Scolarisé'),
            ('non_scolarisé', 'Non scolarisé'),
            ('origine_inconnue', 'Origine inconnue')
        ]
    )

    # Répartition par genre
    nombre_garcons = models.IntegerField(default=0)
    nombre_filles = models.IntegerField(default=0)

    # Statistiques spécifiques
    total_redoublants = models.IntegerField(default=0)  # Nombre total de redoublants
    total_eleves = models.IntegerField(default=0)  # Nombre total d'élèves

    def __str__(self):
        return f"{self.nom_etablissement} - Origine : {self.localite_origine} ({self.pays_origine})"



#------------------------------StructurePedagogique----------------------------


class StructurePedagogique(models.Model):
    division = models.CharField(max_length=100)  # Nom ou niveau de la division pédagogique (ex. CP, CE1)
    nombre_divisions = models.IntegerField()  # Nombre de divisions pédagogiques
    nombre_eleves_garcons = models.IntegerField()  # Nombre de garçons inscrits
    nombre_eleves_filles = models.IntegerField()  # Nombre de filles inscrites
    total_eleves = models.IntegerField()  # Total d'élèves inscrits
    redoublants_garcons = models.IntegerField()  # Nombre de garçons redoublants
    redoublants_filles = models.IntegerField()  # Nombre de filles redoublantes
    total_redoublants = models.IntegerField()  # Total des redoublants

    # Informations supplémentaires
    multigrade = models.BooleanField(default=False)  # Indique si la classe est multigrade
    double_flux = models.BooleanField(default=False)  # Indique si la classe est à double flux

    def __str__(self):
        return f"Division {self.division} - Total élèves : {self.total_eleves}"


#--------------------------------------Finances  Ecole-------------------------------


class FinancesEcole(models.Model):
    # Contributions
    contributions_familles = models.FloatField(null=True, blank=True)  # Contributions des familles
    autres_contributions = models.FloatField(null=True, blank=True)  # Contributions des ONG, individus, etc.
    activites_generatrices_revenus = models.FloatField(null=True, blank=True)  # Revenus issus d'activités

    # Budget et utilisation
    construction_batiments = models.FloatField(null=True, blank=True)  # Dépenses de construction
    renovation_batiments = models.FloatField(null=True, blank=True)  # Dépenses de rénovation
    achat_mobilier = models.FloatField(null=True, blank=True)  # Achats de mobilier
    renovation_mobilier = models.FloatField(null=True, blank=True)  # Rénovation de mobilier
    achat_equipements_pedagogiques = models.FloatField(null=True, blank=True)  # Achats d'équipements pédagogiques
    logement_enseignants = models.FloatField(null=True, blank=True)  # Logement pour enseignants

    # Salaires et cantine
    salaires_personnel_enseignant = models.FloatField(null=True, blank=True)  # Salaires des enseignants
    salaires_personnel_autre = models.FloatField(null=True, blank=True)  # Autres salaires
    cantine_scolaire = models.FloatField(null=True, blank=True)  # Budget pour la cantine

    # Projets
    financement_projets = models.FloatField(null=True, blank=True)  # Financement de projets en cours

    def __str__(self):
        return f"Finances de l'école - ID : {self.id}"


#----------------------------ObservationEventuelle--------------------------


class ObservationEventuelle(models.Model):
    contenu = models.TextField()  # Champ pour les observations éventuelles
    date_creation = models.DateField(auto_now_add=True)  # Date de création automatique

    def __str__(self):
        return f"Observation du {self.date_creation}"

class SignatureEtCachet(models.Model):
    observation = models.ForeignKey(ObservationEventuelle, on_delete=models.CASCADE, related_name='signatures')  # Relie la signature à une observation
    nom_signataire = models.CharField(max_length=200)  # Nom du signataire
    fonction_signataire = models.CharField(max_length=100, choices=[
        ('directeur', 'Directeur de l\'école'),
        ('inspecteur', 'Inspecteur départemental'),
        ('directeur_regional', 'Directeur régional')
    ])  # Fonction du signataire
    date_signature = models.DateField()  # Date de la signature
    cachet_present = models.BooleanField(default=False)  # Indique si un cachet est apposé

    def __str__(self):
        return f"{self.nom_signataire} ({self.fonction_signataire}) - Signé le {self.date_signature}"



