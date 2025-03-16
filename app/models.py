from django import forms
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
#identification et de localisation d'une éco
from django.contrib.auth.models import AbstractUser
from django.db.models import Sum
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
    ancien_code  = models.CharField(max_length=16, null=True, blank=True)  # Ancien nom de l'école  # Ancien code de l'école
    nouveau_code = models.CharField(max_length=16, null=True, blank=True)  # Nouveau code de l'école
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
    nb_latrines_filles = models.IntegerField(default=0, blank=True, null=True)
    nb_latrines_garcons = models.IntegerField(default=0, blank=True, null=True)
    nb_latrines_mixt = models.IntegerField(default=0, blank=True, null=True)
    nb_total_latrines = models.IntegerField(default=0, blank=True, null=True)  # Total calculé
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
SOURCE_CHOICES = [
    ('Etat', 'Etat'),
    ('Commune', 'Commune'),
    ('Parents', 'Parents'),
    ('Autres sources', 'Autres sources'),
    ]
class Local(models.Model):
    numero = models.CharField(max_length=100)
    affectation_du_local = models.CharField(max_length=250, choices=[
        ('salle_classe_utilisée', 'Salle de classe utilisée'),
        ('salle_classe_non_utilisée', 'Salle de classe  non utilisée'),
           ('magasin_pédagogique', 'Magasin pédagogique'),
        ('magasin_alimentaire', 'Magasin alimentaire'),
           ('Bureau directeur', 'Bureau directeur'),
        ('Logement', 'Logement'),
           ('Réfectoire', 'Réfectoire'),
    ], null=True, blank=True)

    dont = models.CharField(max_length=250, choices=[
        ('salle_autre_école', 'Salle autre école'),
        ('local_emprunté_Loué', 'Local emprunté/Loué'),
    ], null=True, blank=True)

    annee_mise_en_service = models.IntegerField()
    surface = models.FloatField()
    nature_murs = models.CharField(max_length=250, choices=[
        ('endur', 'En dur'),
        ('semi_dur', 'Semi dur'),
        ('banco', 'Banco'),
        ('Paillotes', 'Paillotes'),
        ('autres', 'Autres'),
        
    ], null=True, blank=True)

    etat_murs = models.CharField(max_length=250, choices=[
        ('bon_acceptable', 'Bon / acceptable'),
        ('mauvais', 'Mauvais'),
    ], null=True, blank=True)

    nature_toit = models.CharField(max_length=250, choices=[
        ('dur', 'Dur'),
        ('tôle', 'Tôle'),
        ('chaume', 'Chaume'),
        ('autres', 'Autres'),
        
    ], null=True, blank=True)

    etat_toit = models.CharField(max_length=250, choices=[
        ('bon_acceptable', 'Bon / acceptable'),
        ('mauvais', 'Mauvais'),
    ], null=True, blank=True)

    nature_sol = models.CharField(max_length=250, choices=[
        ('ciment', 'Ciment'),
        ('terre', 'Terre'),
        ('autre', 'Autre'),
    ], null=True, blank=True)

    etat_sol = models.CharField(max_length=250, choices=[
        ('bon_acceptable', 'Bon / acceptable'),
        ('mauvais', 'Mauvais'),
    ], null=True, blank=True)

    etat_portes = models.CharField(max_length=250, choices=[
        ('bon', 'Bon'),
        ('mauvais', 'mauvais'),
        ('non installée','Non installée'),
    ], null=True, blank=True)

    etat_fenetres = models.CharField(max_length=250, choices=[
        ('bon', 'Bon'),
        ('mauvais', 'mauvais'),
        ('non installée','Non installée')
    ], null=True, blank=True)

    source_financement = models.ManyToManyField(
        'Source_F',
        related_name="local",
        help_text="Sélectionnez jusqu'à une source."
    )  
    observations = models.TextField()

    def __str__(self):
        return self.numero
    
class Source_F(models.Model):
    nom = models.CharField(max_length=100, choices=ACTIVITES_APE_CHOICES, unique=True)

    def __str__(self):
        return self.get_nom_display()

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

    nom = models.CharField(max_length=100)  # Exemple : Règle, Rapporteur
    quantite = models.PositiveIntegerField(default=0)  # Quantité disponible

    def __str__(self):
        return f"{self.nom} - {self.quantite}"


class DotationEleve(models.Model):
    nombre_eleves_dotes = models.PositiveIntegerField(default=0)  # Nombre d'élèves ayant reçu des matériels

    def __str__(self):
        return f"Élèves dotés : {self.nombre_eleves_dotes}"
    
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
    numero_ordre = models.IntegerField("N° ordre du fonctionnaire")
    matricule_solde = models.CharField("Matricule/solde", max_length=50)
    genre = models.CharField("Genre", max_length=1, choices=[('H', 'Homme'), ('F', 'Femme')])
    annee_naissance = models.IntegerField("Année de naissance")
    annee_recrutement = models.IntegerField("Année de recrutement")
    annee_arrivee_ecole = models.IntegerField("Année d'arrivée à l'école")
    statut = models.CharField("Statut", max_length=50, choices=[
        ('Instituteur adjoint', 'Instituteur adjoint'),
        ('Instituteur', 'Instituteur'),
        ('Moniteur', 'Moniteur'),
        ('Contractuel', 'Contractuel'),
        ('Stagiaire', 'Stagiaire'),
        ('Autre', 'Autre'),
    ])
    fonction = models.CharField("Fonction", max_length=50, choices=[
        ('Directeur', 'Directeur'),
        ('Enseignant classe', 'Enseignant classe'),
        ('Suppléant', 'Suppléant'),
        ('Personnel d\'appui', 'Personnel d\'appui'),
        ('ENI-Normal', 'ENI-Normal'),
        ('ENI-Adaptée', 'ENI-Adaptée'),
        ('Autres', 'Autres'),
    ])
    formation_initiale = models.CharField("Formation professionnelle", max_length=20, choices=[
        ('normal', 'ENI-Normal'),
        ('accéléré', ' ENI- Accéléré'),
        ('autres', 'Autres'),
        ('sans', 'Sans'),
    ])
    formation_continue =  models.CharField("Formation continue", max_length=20, choices=[
        ('Multigrade', 'Multigrade'),
        (' Double-flux', 'Double-flux'),
        ('APC', 'APC'),
        ('langueFranc_ou_Arab','Langue (Franc ou Arab.)'),
        (' gestion_pédagogique', 'Gestion pédagogique'),
        ('Gestion_cantine', 'Gestion cantine'),
        ('vih','VIH'),
    ])
    langue_formation = models.CharField("Langue de formation", max_length=20, choices=[
        ('Arabe', 'Arabe'),
        ('Français', 'Français'),
    ])
    langue_travail = models.CharField("Langue de travail", max_length=20, choices=[
        ('Arabe', 'Arabe'),
        ('Français', 'Français'),
        ('Anglais', 'Anglais'),
    ])
    peut_enseigner = models.CharField("Peut enseigner en", max_length=20, choices=[
        ('Arabe', 'Arabe'),
        ('Français', 'Français'),
        ('Anglais', 'Anglais'),
    ])
    nombre_inspections = models.IntegerField("Nombre d'inspections l'année passée")
    present_ecole = models.BooleanField("Effectivement présent dans l'école", default=True)

    def __str__(self):
        return f"{self.numero_ordre} - {self.matricule_solde}"


#---------------------------------répartition des nouveaux inscrits----------------------------



class NouveauxInscrits(models.Model):
    SITUATION_PRESCOLAIRE_CHOICES = [
        ('garderie', 'Garderie'),
        ('jardin_enfants', 'Jardins d\'enfants'),
        ('ecole_coraniques', 'Ecoles coraniques'),
        ('aucun_enseignement', 'Aucun enseignement'),
        ('origine_non_connu', 'Origine non connue'),
    ]

    situation_prescolaire = models.CharField(
        "Situation préscolaire",
        max_length=50,
        choices=SITUATION_PRESCOLAIRE_CHOICES
    )
    garcons = models.IntegerField("Garçons", default=0)
    filles = models.IntegerField("Filles", default=0)

    def total_inscrits(self):
        """Calcule le total des inscrits (Garçons + Filles)."""
        return self.garcons + self.filles


#-----------------------------RÉPARTITION DES ÉLEVES PAR DIVISION PÉDAGOGIQUE----------------------------------


class DivisionPedagogique(models.Model):
    division_pedagogique = models.CharField(max_length=100, verbose_name="Division pédagogique")
    annee_etude = models.CharField(max_length=50, verbose_name="Année d'étude/Niveau")  # Exemple : "1ère année", "6ème année"
    numero_salle_classe = models.PositiveIntegerField(verbose_name="N°  salle de classe")	

    type_classe_choices = [
        ('simple', 'Simple vacation'),
        ('double', 'Double vacation'),
        ('multigrad', 'Multi-grade'),
    ]
    type_classe = models.CharField(max_length=10, choices=type_classe_choices, verbose_name="Type de classe")
    numero_enseignant_arabe = models.PositiveIntegerField(verbose_name="N° ordre arabe")
    numero_enseignant_francais = models.PositiveIntegerField(verbose_name="N° ordre francais")
    
    # Répartition des âges
    apres_oct_2008_moins_6 = models.PositiveIntegerField(default=0, verbose_name="Moins de 6 ans (après octobre 2008)")
    oct_2008_6_ans = models.PositiveIntegerField(default=0, verbose_name="6 ans (Oct-08)")
    oct_2007_7_ans = models.PositiveIntegerField(default=0, verbose_name="7 ans (Oct-07)")
    oct_2006_8_ans = models.PositiveIntegerField(default=0, verbose_name="8 ans (Oct-06)")
    oct_2005_9_ans = models.PositiveIntegerField(default=0, verbose_name="9 ans (Oct-05)")
    oct_2004_10_ans = models.PositiveIntegerField(default=0, verbose_name="10 ans (Oct-04)")
    oct_2003_11_ans = models.PositiveIntegerField(default=0, verbose_name="11 ans (Oct-03)")
    oct_2002_12_ans = models.PositiveIntegerField(default=0, verbose_name="12 ans (Oct-02)")
    oct_2001_13_ans = models.PositiveIntegerField(default=0, verbose_name="13 ans (Oct-01)")
    oct_2000_14_ans = models.PositiveIntegerField(default=0, verbose_name="14 ans (Oct-00)")
    avant_2000_plus_14 = models.PositiveIntegerField(default=0, verbose_name="Plus de 14 ans (Avant 2000)")

    # Totaux et statistiques
    total_eleves = models.PositiveIntegerField(default=0, verbose_name="Total")
    dont_redoublants = models.PositiveIntegerField(default=0, verbose_name="Dont redoublants")
    redoublants_avec_cef = models.PositiveIntegerField(default=0, verbose_name="Redoublants 6ème année avec CEF")

    # Calcul automatique du total
    def save(self, *args, **kwargs):
        self.total_eleves = (
            self.apres_oct_2008_moins_6 + self.oct_2008_6_ans + self.oct_2007_7_ans +
            self.oct_2006_8_ans + self.oct_2005_9_ans + self.oct_2004_10_ans +
            self.oct_2003_11_ans + self.oct_2002_12_ans + self.oct_2001_13_ans +
            self.oct_2000_14_ans + self.avant_2000_plus_14
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Division: {self.division_pedagogique}, Total élèves: {self.total_eleves}"


#--------------------------Aire Recrutement----------------------------

from django.db import models

class AireRecrutement(models.Model):
    # Informations générales
    localite = models.CharField(max_length=100, verbose_name="Localité/Quartier")
    distance_choices = [
        ('moins_de_1km', '<1 km'),
        ('entre_1_et_3km', '1-3 km'),
        ('entre_3_et_5km', '3-5 km'),
        ('plus_de_5km', '>5 km'),
        ('indetermine', 'Indéterminée'),
    ]
    distance = models.CharField(max_length=20, choices=distance_choices, verbose_name="Distance de l'école")

    # Répartition des élèves par classe et genre
    g_1a = models.PositiveIntegerField(default=0, verbose_name="Garçons 1A")
    f_1a = models.PositiveIntegerField(default=0, verbose_name="Filles 1A")
    g_2a = models.PositiveIntegerField(default=0, verbose_name="Garçons 2A")
    f_2a = models.PositiveIntegerField(default=0, verbose_name="Filles 2A")
    g_3a = models.PositiveIntegerField(default=0, verbose_name="Garçons 3A")
    f_3a = models.PositiveIntegerField(default=0, verbose_name="Filles 3A")
    g_4a = models.PositiveIntegerField(default=0, verbose_name="Garçons 4A")
    f_4a = models.PositiveIntegerField(default=0, verbose_name="Filles 4A")
    g_5a = models.PositiveIntegerField(default=0, verbose_name="Garçons 5A")
    f_5a = models.PositiveIntegerField(default=0, verbose_name="Filles 5A")
    g_6a = models.PositiveIntegerField(default=0, verbose_name="Garçons 6A")
    f_6a = models.PositiveIntegerField(default=0, verbose_name="Filles 6A")

    # Totaux
    total_garcons = models.PositiveIntegerField(default=0, verbose_name="Total Garçons")
    total_filles = models.PositiveIntegerField(default=0, verbose_name="Total Filles")

    # Calcul automatique des totaux
    def save(self, *args, **kwargs):
        self.total_garcons = self.g_1a + self.g_2a + self.g_3a + self.g_4a + self.g_5a + self.g_6a
        self.total_filles = self.f_1a + self.f_2a + self.f_3a + self.f_4a + self.f_5a + self.f_6a
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.localite} - Distance: {self.get_distance_display()}"




class StatistiqueGenerale(models.Model):
    annee_scolaire = models.CharField(max_length=10)  # Année scolaire (ex. 2024/2025)
    total_inscrits = models.IntegerField(default=0)  # Nombre total des inscrits
    total_redoublants = models.IntegerField(default=0)  # Total redoublants

    def __str__(self):
        return f"Statistiques - Année : {self.annee_scolaire}"



#------------------------------Mobilite Eleves------------------------------

class MobiliteEleves(models.Model):
    # Types d'établissements fréquentés l'année précédente
    etablissement_choices = [
        ('meme_ecole', 'Même école'),
        ('ecole_meme_moughataa', 'École fondamentale de la même Moughataa'),
        ('ecole_autre_moughataa', 'École d\'une autre Moughataa, même Wilaya'),
        ('ecole_autre_wilaya', 'École fondamentale d\'une autre Wilaya'),
        ('ecole_etranger', 'École d\'un pays étranger'),
        ('prescolaire', 'Préscolaire'),
        ('mahadra', 'Mahadra'),
        ('non_scolarise', 'Non scolarisés'),
        ('origine_inconnue', 'Origine non connue'),
    ]
    etablissement = models.CharField(max_length=50, choices=etablissement_choices, verbose_name="Établissement fréquenté")

    # Répartition des élèves par niveau et genre
    g_1a = models.PositiveIntegerField(default=0, verbose_name="Garçons 1A")
    f_1a = models.PositiveIntegerField(default=0, verbose_name="Filles 1A")
    g_2a = models.PositiveIntegerField(default=0, verbose_name="Garçons 2A")
    f_2a = models.PositiveIntegerField(default=0, verbose_name="Filles 2A")
    g_3a = models.PositiveIntegerField(default=0, verbose_name="Garçons 3A")
    f_3a = models.PositiveIntegerField(default=0, verbose_name="Filles 3A")
    g_4a = models.PositiveIntegerField(default=0, verbose_name="Garçons 4A")
    f_4a = models.PositiveIntegerField(default=0, verbose_name="Filles 4A")
    g_5a = models.PositiveIntegerField(default=0, verbose_name="Garçons 5A")
    f_5a = models.PositiveIntegerField(default=0, verbose_name="Filles 5A")
    g_6a = models.PositiveIntegerField(default=0, verbose_name="Garçons 6A")
    f_6a = models.PositiveIntegerField(default=0, verbose_name="Filles 6A")

    # Totaux
    total_garcons = models.PositiveIntegerField(default=0, verbose_name="Total Garçons", editable=False)
    total_filles = models.PositiveIntegerField(default=0, verbose_name="Total Filles", editable=False)

    # Calcul automatique des totaux
    def save(self, *args, **kwargs):
        self.total_garcons = self.g_1a + self.g_2a + self.g_3a + self.g_4a + self.g_5a + self.g_6a
        self.total_filles = self.f_1a + self.f_2a + self.f_3a + self.f_4a + self.f_5a + self.f_6a
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_etablissement_display()} - Garçons: {self.total_garcons}, Filles: {self.total_filles}"

#------------------------------StructurePedagogique----------------------------


from django.db import models

class StructurePedagogique(models.Model):
    NIVEAUX = [
        ('1A', '1A'), 
        ('2A', '2A'), 
        ('3A', '3A'),
        ('4A', '4A'), 
        ('5A', '5A'), 
        ('6A', '6A')
    ]

    # Niveau pédagogique (ex: 1A, 2A, etc.)
    niveau = models.CharField(max_length=2, choices=NIVEAUX, unique=True)

    # Divisions pédagogiques
    simples = models.PositiveIntegerField(default=0, verbose_name="Divisions simples")
    multigrades = models.PositiveIntegerField(default=0, verbose_name="Divisions multigrades")
    double_flux = models.PositiveIntegerField(default=0, verbose_name="Divisions double flux")

    # Élèves inscrits
    inscrits_garcons = models.PositiveIntegerField(default=0, verbose_name="Élèves garçons inscrits")
    inscrits_filles = models.PositiveIntegerField(default=0, verbose_name="Élèves filles inscrites")

    # Élèves redoublants
    redoublants_garcons = models.PositiveIntegerField(default=0, verbose_name="Redoublants garçons")
    redoublants_filles = models.PositiveIntegerField(default=0, verbose_name="Redoublants filles")

    # Propriétés calculées
    @property
    def inscrits_total(self):
        return self.inscrits_garcons + self.inscrits_filles

    @property
    def redoublants_total(self):
        return self.redoublants_garcons + self.redoublants_filles

    @property
    def divisions_total(self):
        return self.simples + self.multigrades + self.double_flux

    def __str__(self):
        return f"Niveau {self.niveau}: {self.inscrits_total} élèves inscrits"

    def save(self, *args, **kwargs):
        # Vous pouvez ajouter des validations ou d'autres calculs si nécessaire ici.
        super().save(*args, **kwargs)

#--------------------------------------Finances  Ecole-------------------------------
from django.db import models

class Contributions(models.Model):
    CONTRIBUTION_RECUES = [
        ('montant_global', 'Montant GLOBAL annuel de la cotisation de l\'Association des Parents d\'Elèves'),
        ('cotisations_parents', 'Autres cotisations des parents d\'élèves'),
        ('frais_inscription', 'Montant GLOBAL des frais d\'inscription (pour le privé)'),
        ('autres_contributions', 'Autres contributions (ONG, Individus, etc.)'),
        ('activites_generatrices_revenus', 'Activités génératrices de revenus'),
    ]

    contributions_reçues_familles = models.CharField(
        max_length=50, choices=CONTRIBUTION_RECUES, verbose_name="Catégorie de contribution"
    )

    annee_precedente = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    annee_courante = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Contribution financière"
        verbose_name_plural = "Contributions financières"

    def __str__(self):
        return f"{self.get_contributions_reçues_familles_display()} | {self.annee_courante} FCFA"

    @staticmethod
    def calculer_totaux():
        """
        Calcule les totaux globaux de toutes les contributions enregistrées.
        """
        total_annee_precedente = Contributions.objects.aggregate(total=Sum('annee_precedente'))['total'] or 0
        total_annee_en_cours = Contributions.objects.aggregate(total=Sum('annee_courante'))['total'] or 0

        return {
            'total_annee_precedente': total_annee_precedente,
            'total_annee_en_cours': total_annee_en_cours
        }

class DonneeFinanciere(models.Model):
    
    CATEGORIES_DEPENSES = [
        ('construction_batiments', 'Construction bâtiments'),
        ('renovation_batiments', 'Rénovation bâtiments'),
        ('achat_mobilier', 'Achat de mobilier'),
        ('renovation_mobilier', 'Rénovation de mobilier'),
        ('achat_equipements_pedagogiques', 'Achat équipements pédagogiques'),
        ('achat_manuels_scolaires', 'Achat de manuels scolaires'),
        ('logements_enseignants', 'Logements des enseignants'),
        ('factures_eau', 'Factures d\'eau'),
        ('factures_electricite', 'Factures d\'électricité'),
        ('factures_telephone', 'Factures de téléphone'),
        ('salaire_enseignants', 'Salaire personnel enseignant'),
        ('salaire_personnel_autre', 'Salaire personnel autre'),
        ('cantines_scolaires', 'Cantines scolaires'),
    ]
    
    PARTENARIAT_CHOICES = [
        ('jumelage', 'Jumelage'),
        ('ong', 'ONG'),
        ('prive', 'Privé'),
    ]

    categorie = models.CharField(max_length=50, choices=CATEGORIES_DEPENSES, verbose_name="Catégorie de dépense")
    budget_ecole = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Budget école")
    collectivites = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Collectivités")
    ape = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="APE")
    autre = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="AUTRE")

    projet_ecole = models.BooleanField(default=False, verbose_name="L'école envisage-t-elle un projet d'école ?")
    nature_projet = models.CharField(
        max_length=255,  # Set an appropriate value for the maximum length
        blank=True,
        null=True,
        verbose_name="Nature du projet",
        help_text="Décrivez le projet si applicable"
    )
    partenariat = models.BooleanField(default=False, verbose_name="L'école a-t-elle établi un ou des partenariats ?")
    type_partenariat = models.CharField(max_length=20, choices=PARTENARIAT_CHOICES, blank=True, null=True, verbose_name="Type de partenariat")


#----------------------------ObservationEventuelle--------------------------


class ObservationEventuelle(models.Model):
    observations = models.TextField(verbose_name="Observations éventuelles", blank=True, null=True)
    directeur_nom = models.CharField(max_length=255, verbose_name="Nom du directeur de l'école", blank=True, null=True)
    directeur_date = models.DateField(verbose_name="Date (Directeur de l'école)", blank=True, null=True)
    directeur_signature = models.BooleanField(verbose_name="Signature et cachet (Directeur de l'école)", default=False)
    inspection_date = models.DateField(verbose_name="Date (Inspection départementale)", blank=True, null=True)
    inspection_signature = models.BooleanField(verbose_name="Signature et cachet (Inspection départementale)", default=False)
    direction_date = models.DateField(verbose_name="Date (Direction régionale)", blank=True, null=True)
    direction_signature = models.BooleanField(verbose_name="Signature et cachet (Direction régionale)", default=False)

    def __str__(self):
        return f"Formulaire par {self.directeur_nom or 'Directeur inconnu'}"
