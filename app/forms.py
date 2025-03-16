from django import forms
from .models import AireRecrutement,Contributions, DivisionPedagogique, DonneeFinanciere, DotationEleve, Ecole, Ecole_identification, EquipementDidactique, GuideEtManuel, Local, LocaliteRurale, MobilierCollectif, MobilierEleve,MobiliteEleves, NouveauxInscrits, ObservationEventuelle, Personnel, StatistiqueGenerale, StructurePedagogique

from django import forms
from .models import Ecole
from django.core.exceptions import ValidationError
from .models import ACTIVITES_CHOICES,LocaliteRurale,Activite_APE

class EcoleForm(forms.ModelForm):
    class Meta:
        model = Ecole
        fields = [
            'nom', 'info_ecole', 'accessible_toute_annee',
            'eau_disponible', 'type_eau', 'nb_postes_eau',
            'electricite_disponible', 'nb_classes_electrifiees',
            'cantine_fonctionnelle', 'nb_rationnaires', 'nb_de_fille_beneficiaires',
            'source_financement', 'laves_mains_disponibles', 'nb_laves_mains',
            'domaine_cloture', 'superficie_cloture', 'type_cloture',
            'espace_recreation_disponible', 'superficie_recreation',
            'jardin_scolaire', 'utilisation_de_la_produit',
            'nb_latrines_filles', 'nb_latrines_garcons', 'nb_latrines_mixt', 'nb_total_latrines',
            'ape_existe', 'femmes_ape', 'hommes_ape', 'activites_ape', 'presidence_ape',
            'comite_gestion_existe', 'femmes_comite', 'hommes_comite', 'presidence_comite',
            'distance_centre_sante', 'apport_en_vitamine_A', 'boite_pharmacie_disponible',
            'visite_médicale_année_dernière', 'campagne_de_déparasitage',
            'campagne_de_sensibilisation_au_VIH', 'campagne_de_sensibilisation_au_palu',
            'association_eleve',
        ]

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'école'}),
            'info_ecole': forms.Select(attrs={'class': 'form-select'}),
            'accessible_toute_annee': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'eau_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'type_eau': forms.Select(attrs={'class': 'form-select'}),
            'nb_postes_eau': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de postes d\'eau'}),
            'electricite_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nb_classes_electrifiees': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantine_fonctionnelle': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nb_rationnaires': forms.NumberInput(attrs={'class': 'form-control'}),
            'nb_de_fille_beneficiaires': forms.NumberInput(attrs={'class': 'form-control'}),
            'source_financement': forms.Select(attrs={'class': 'form-select'}),
            'laves_mains_disponibles': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nb_laves_mains': forms.NumberInput(attrs={'class': 'form-control'}),
            'domaine_cloture': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'superficie_cloture': forms.NumberInput(attrs={'class': 'form-control'}),
            'type_cloture': forms.Select(attrs={'class': 'form-select'}),
            'espace_recreation_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'superficie_recreation': forms.NumberInput(attrs={'class': 'form-control'}),
            'jardin_scolaire': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'utilisation_de_la_produit': forms.Select(attrs={'class': 'form-select'}),
            'nb_latrines_filles': forms.NumberInput(attrs={'class': 'form-control'}),
            'nb_latrines_garcons': forms.NumberInput(attrs={'class': 'form-control'}),
            'nb_latrines_mixt': forms.NumberInput(attrs={'class': 'form-control'}),
            'nb_total_latrines': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'ape_existe': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'femmes_ape': forms.NumberInput(attrs={'class': 'form-control'}),
            'hommes_ape': forms.NumberInput(attrs={'class': 'form-control'}),
            'activites_ape': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'presidence_ape': forms.Select(attrs={'class': 'form-select'}),
            'comite_gestion_existe': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'femmes_comite': forms.NumberInput(attrs={'class': 'form-control'}),
            'hommes_comite': forms.NumberInput(attrs={'class': 'form-control'}),
            'presidence_comite': forms.Select(attrs={'class': 'form-select'}),
            'distance_centre_sante': forms.NumberInput(attrs={'class': 'form-control'}),
            'apport_en_vitamine_A': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'boite_pharmacie_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'visite_médicale_année_dernière': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'campagne_de_déparasitage': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'campagne_de_sensibilisation_au_VIH': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'campagne_de_sensibilisation_au_palu': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'association_eleve': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }     
    

        labels = {
            'nom': "Nom de l'école",
            'info_ecole': "Statut de l'école",
            'accessible_toute_annee': "Accessible toute l'année",
            'eau_disponible': "École alimentée en eau",
            'type_eau': "Type d'alimentation en eau",
            'nb_postes_eau': "Nombre de postes d'eau",
            'electricite_disponible': "Électricité disponible",
            'nb_classes_electrifiees': "Nombre de classes électrifiées",
            'cantine_fonctionnelle': "Cantine fonctionnelle",
            'nb_rationnaires': "Nombre de rationnaires",
            'nb_de_fille_beneficiaires': "Nombre de filles bénéficiaires",
            'source_financement': "Source de financement",
            'laves_mains_disponibles': "Laves-mains disponibles",
            'nb_laves_mains': "Nombre de laves-mains",
            'domaine_cloture': "Domaine scolaire clôturé",
            'superficie_cloture': "Superficie clôturée (m²)",
            'type_cloture': "Type de clôture",
            'espace_recreation_disponible': "Espace de récréation disponible",
            'superficie_recreation': "Superficie de récréation (m²)",
            'jardin_scolaire': "Jardin scolaire",
            'utilisation_de_la_produit': "Utilisation de la production",
            'nb_latrines_filles': "Nombre de latrines pour filles",
            'nb_latrines_garcons': "Nombre de latrines pour garçons",
            'nb_latrines_mixt': "Nombre de latrines mixtes",
            'nb_total_latrines': "Nombre total de latrines",
            
            'ape_existe': "L'APE (Association des Parents d'Élèves) existe",
            'femmes_ape': "Nombre de femmes dans l'APE",
            'hommes_ape': "Nombre d'hommes dans l'APE",
            'activites_ape': "Activités de l'APE",
            'presidence_ape': "Présidence de l'APE",
            'comite_gestion_existe': "Comité de gestion existe",
            'femmes_comite': "Nombre de femmes dans le comité de gestion",
            'hommes_comite': "Nombre d'hommes dans le comité de gestion",
            'presidence_comite': "Présidence du comité de gestion",
            'distance_centre_sante': "Distance au centre de santé (km)",
            'apport_en_vitamine_A': "Apport en vitamine A",
            'boite_pharmacie_disponible': "Boîte pharmacie disponible",
            'visite_médicale_année_dernière': "Visite médicale l'année dernière",
            'campagne_de_déparasitage': "Campagne de déparasitage",
            'campagne_de_sensibilisation_au_VIH': "Sensibilisation au VIH",
            'campagne_de_sensibilisation_au_palu': "Sensibilisation au paludisme",
            'association_eleve': "Association d'élèves existe",
        }

    def clean_activites_ape(self):
        activites = self.cleaned_data.get('activites_ape', [])
        if len(activites) > 3:
            raise forms.ValidationError("Vous ne pouvez sélectionner que trois activités.")
        return activites

    def clean(self):
        cleaned_data = super().clean()

        latrines_filles = cleaned_data.get('nb_latrines_filles') or 0
        latrines_garcons = cleaned_data.get('nb_latrines_garcons') or 0
        latrines_mixt = cleaned_data.get('nb_latrines_mixt') or 0

        # Calcul automatique
        total_latrines = latrines_filles + latrines_garcons + latrines_mixt
        cleaned_data['nb_total_latrines'] = total_latrines

        if total_latrines == 0:
            self.add_error(None, "Veuillez renseigner au moins une latrine.")

        return cleaned_data 


class EcoleIdentificationForm(forms.ModelForm):
    class Meta:
        model = Ecole_identification
        fields = [
            'ancien_code', 'nouveau_code', 'nom', 'ancien_nom',
            'date_creation', 'statut','Localisation_administrative', 
            'Localisation_scolaire','zone'
        ]
        widgets = {
            'ancien_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Entrez l\'ancien code'}),
            'nouveau_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nouveau code'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'école'}),
            'ancien_nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ancien nom de l\'école'}),
            'date_creation': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'statut': forms.Select(attrs={'class': 'form-select'}),
            'Localisation_administrative': forms.Select(attrs={'class': 'form-select'}),
            'Localisation_scolaire': forms.Select(attrs={'class': 'form-select'}),
        'zone': forms.Select(attrs={'class': 'form-select'}),
           
        }
        labels = {
            'ancien_code': 'Ancien Code',
            'nouveau_code': 'Nouveau Code',
            'nom': 'Nom de l\'École',
            'ancien_nom': 'Ancien Nom',
            'date_creation': 'Date de Création',
            'statut': 'Statut',
            
            'Localisation_administrative': 'Localisation Administrative',
            'Localisation_scolaire': 'Localisation Scolaire',
            'zone': 'Zone',
        }


    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if not nom:
            raise forms.ValidationError("Le nom de l'école est obligatoire.")
        if len(nom) > 100:
            raise forms.ValidationError("Le nom de l'école ne peut pas dépasser 100 caractères.")
        return nom
    
    
    
    
class LocaliteRuraleForm(forms.ModelForm):
    class Meta:
        model = LocaliteRurale
        fields = [
            'type_acces',
            'electricite_disponible',
            'type_eau',
            'service_sante_disponible',
            'type_service_sante',
            'mosquee_disponible',
            'mahadra_disponible',
            'bibliotheque_disponible',
            'terrain_sport_disponible',
            'autres_structures_animation',
            'activites_dominantes',
            'type_marche',
            'type_de_coperation',
            'developpe_socio_économique',
            'secteur_intervention',
            'bailleurs_ong'
        ]
        widgets = {
            'type_acces': forms.Select(attrs={'class': 'form-select'}),
            'electricite_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'type_eau': forms.Select(attrs={'class': 'form-select'}),
            'service_sante_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'type_service_sante': forms.Select(attrs={'class': 'form-select'}),
            'mosquee_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'mahadra_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'bibliotheque_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'terrain_sport_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'autres_structures_animation': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 3,
                'placeholder': 'Décrivez d’autres structures disponibles'
            }),
            'activites_dominantes': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),

            'type_marche': forms.Select(attrs={'class': 'form-select'}),
            'type_de_coperation': forms.Select(attrs={'class': 'form-select'}),
            'developpe_socio_économique': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'secteur_intervention': forms.Select(attrs={'class': 'form-select'}),
            'bailleurs_ong': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 3,
                'placeholder': 'Ajoutez des informations sur les bailleurs ou ONG'
            }),
        }
        labels = {
            'type_acces': 'Type d\'accès',
            'electricite_disponible': 'Électricité disponible',
            'type_eau': 'Type d\'eau',
            'service_sante_disponible': 'Service de santé disponible',
            'type_service_sante': 'Type de service de santé',
            'mosquee_disponible': 'Mosquée disponible',
            'mahadra_disponible': 'Mahadra disponible',
            'bibliotheque_disponible': 'Bibliothèque disponible',
            'terrain_sport_disponible': 'Terrain de sport disponible',
            'autres_structures_animation': 'Autres structures d\'animation',
            'activites_dominantes': 'Activités économiques dominantes',
            'type_marche': 'Type de marché',
            'type_de_coperation': 'Type de coopération',
            'developpe_socio_économique': 'Développement socio-économique',
            'secteur_intervention': 'Secteur d\'intervention',
            'bailleurs_ong': 'Bailleurs ou ONG',
        }

    def clean_activites_dominantes(self):
        activites = self.cleaned_data.get('activites_dominantes')
        if activites.count() > 3:
            raise ValidationError("Vous ne pouvez sélectionner que trois activités économiques dominantes.")
        return activites


from django import forms
from .models import Local

class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = [
            'numero', 'affectation_du_local', 'dont', 'annee_mise_en_service', 
            'surface', 'nature_murs', 'etat_murs', 'nature_toit', 
            'etat_toit', 'nature_sol', 'etat_sol', 'etat_portes', 
            'etat_fenetres', 'source_financement', 'observations'
        ]
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numéro du local', 'min': '0'}),
            'affectation_du_local': forms.Select(attrs={'class': 'form-select'}),
            'dont': forms.Select(attrs={'class': 'form-select'}),
            'annee_mise_en_service': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex : 1995', 'min': '1900'}),
            'surface': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Surface en m²', 'min': '1'}),
            'nature_murs': forms.Select(attrs={'class': 'form-select'}),
            'etat_murs': forms.Select(attrs={'class': 'form-select'}),
            'nature_toit': forms.Select(attrs={'class': 'form-select'}),
            'etat_toit': forms.Select(attrs={'class': 'form-select'}),
            'nature_sol': forms.Select(attrs={'class': 'form-select'}),
            'etat_sol': forms.Select(attrs={'class': 'form-select'}),
            'etat_portes':forms.Select(attrs={'class': 'form-select'}),
            'etat_fenetres': forms.Select(attrs={'class': 'form-select'}),
            'source_financement': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'observations': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observations supplémentaires'}),
        }
        labels = {
            'numero': 'Numéro',
            'affectation_du_local': 'Affectation',
            'dont': 'Dont',
            'annee_mise_en_service': 'Année de mise en service',
            'surface': 'Surface (m²)',
            'nature_murs': 'Nature des murs',
            'etat_murs': 'État des murs',
            'nature_toit': 'Nature du toit',
            'etat_toit': 'État du toit',
            'nature_sol': 'Nature du sol',
            'etat_sol': 'État du sol',
            'etat_portes': 'État des portes',
            'etat_fenetres': 'État des fenêtres',
            'source_financement': 'Source de financement',
            'observations': 'Observations',
        }

    # Validation personnalisée
    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if not numero:
            raise forms.ValidationError("Le numéro est requis.")
        return numero

    def clean_surface(self):
        surface = self.cleaned_data.get('surface')
        if surface <= 0:
            raise forms.ValidationError("La surface doit être supérieure à zéro.")
        return surface

    def clean_annee_mise_en_service(self):
        annee = self.cleaned_data.get('annee_mise_en_service')
        if annee < 1900 or annee > 2100:
            raise forms.ValidationError("L'année doit être comprise entre 1900 et 2100.")
        return annee


# Formulaire pour Mobilier Collectif
class MobilierCollectifForm(forms.ModelForm):
    class Meta:
        model = MobilierCollectif
        fields = ['nom', 'etat', 'nombre']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex : Bureau du maître'}),
            'etat': forms.Select(attrs={'class': 'form-select'}),
            'nombre': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex : 10'}),
        }

# Formulaire pour Mobilier Élève
class MobilierEleveForm(forms.ModelForm):
    class Meta:
        model = MobilierEleve
        fields = ['type_table_banc', 'etat', 'nombre']
        widgets = {
            'type_table_banc': forms.Select(attrs={'class': 'form-select'}),
            'etat': forms.Select(attrs={'class': 'form-select'}),
            'nombre': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex : 30'}),
        }

from django import forms
from .models import EquipementDidactique

class EquipementDidactiqueForm(forms.ModelForm):
    class Meta:
        model = EquipementDidactique
        fields = ['nom', 'quantite']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Règle'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Entrez la quantité'}),
        }


class DotationEleveForm(forms.ModelForm):
    class Meta:
        model = DotationEleve
        fields = ['nombre_eleves_dotes']
        widgets = {
            'nombre_eleves_dotes': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre d\'élèves dotés'}),
        }

from django import forms
from .models import GuideEtManuel

class GuideEtManuelForm(forms.ModelForm):
    class Meta:
        model = GuideEtManuel
        fields = ['niveau', 'matiere', 'langue', 'guides', 'manuels']
        widgets = {
            'niveau': forms.Select(attrs={'class': 'form-select'}),
            'matiere': forms.Select(attrs={'class': 'form-select'}),
            'langue': forms.Select(attrs={'class': 'form-select'}),
            'guides': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de guides'}),
            'manuels': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de manuels'}),
        }
        labels = {
            'niveau': 'Niveau Scolaire',
            'matiere': 'Matière',
            'langue': 'Langue',
            'guides': 'Nombre de Guides',
            'manuels': 'Nombre de Manuels',
        }



class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = '__all__'  # Inclut tous les champs du modèle
        widgets = {
            'numero_ordre': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'N° ordre'}),
            'matricule_solde': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matricule/solde'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'annee_naissance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Année de naissance'}),
            'annee_recrutement': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Année de recrutement'}),
            'annee_arrivee_ecole': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Année d\'arrivée à l\'école'}),
            'statut': forms.Select(attrs={'class': 'form-select'}),
            'fonction': forms.Select(attrs={'class': 'form-select'}),
            'formation_initiale': forms.Select(attrs={'class': 'form-select'}),
            'formation_continue': forms.Select(attrs={'class': 'form-select'}),
            'langue_formation': forms.Select(attrs={'class': 'form-select'}),
            'langue_travail': forms.Select(attrs={'class': 'form-select'}),
            'peut_enseigner': forms.Select(attrs={'class': 'form-select'}),
            'nombre_inspections': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre d\'inspections'}),
            'present_ecole': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'numero_ordre': 'N° ordre',
            'matricule_solde': 'Matricule/solde',
            'genre': 'Genre',
            'annee_naissance': 'Année de naissance',
            'annee_recrutement': 'Année de recrutement',
            'annee_arrivee_ecole': 'Année d\'arrivée à l\'école',
            'statut': 'Statut',
            'fonction': 'Fonction',
            'formation_initiale': 'Formation professionnelle',
            'formation_continue': 'Formation continue',
            'langue_formation': 'Langue de formation',
            'langue_travail': 'Langue de travail',
            'peut_enseigner': 'Peut enseigner en',
            'nombre_inspections': 'Nombre d\'inspections l\'année passée',
            'present_ecole': 'Présent à l\'école',
        }

    def clean_annee_naissance(self):
        annee = self.cleaned_data.get('annee_naissance')
        if annee and annee > 2025:  # Par exemple, empêcher une date future
            raise forms.ValidationError("L'année de naissance doit être valide.")
        return annee

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('annee_recrutement') and cleaned_data.get('annee_naissance'):
            age_a_recrutement = cleaned_data['annee_recrutement'] - cleaned_data['annee_naissance']
            if age_a_recrutement < 18:
                raise forms.ValidationError("L'âge au recrutement doit être d'au moins 18 ans.")
        return cleaned_data



class NouveauxInscritsForm(forms.ModelForm):
    class Meta:
        model = NouveauxInscrits
        fields = ['situation_prescolaire', 'garcons', 'filles']
        widgets = {
            'situation_prescolaire': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Sélectionnez une situation préscolaire'
            }),
            'garcons': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de garçons'
            }),
            'filles': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de filles'
            }),
        }
        labels = {
            'situation_prescolaire': 'Situation préscolaire',
            'garcons': 'Garçons',
            'filles': 'Filles',
        }

    def clean_garcons(self):
        garcons = self.cleaned_data.get('garcons')
        if garcons < 0:
            raise forms.ValidationError("Le nombre de garçons ne peut pas être négatif.")
        return garcons

    def clean_filles(self):
        filles = self.cleaned_data.get('filles')
        if filles < 0:
            raise forms.ValidationError("Le nombre de filles ne peut pas être négatif.")
        return filles

    def clean(self):
        cleaned_data = super().clean()
        garcons = cleaned_data.get('garcons', 0)
        filles = cleaned_data.get('filles', 0)

        if garcons + filles == 0:
            raise forms.ValidationError("Le total des inscrits doit être supérieur à zéro.")
        return cleaned_data



class DivisionPedagogiqueForm(forms.ModelForm):
    class Meta:
        model = DivisionPedagogique
        fields = [
            'division_pedagogique', 'annee_etude', 'numero_salle_classe','type_classe', 'numero_enseignant_arabe',
            'numero_enseignant_francais', 'apres_oct_2008_moins_6', 'oct_2008_6_ans', 'oct_2007_7_ans',
            'oct_2006_8_ans', 'oct_2005_9_ans', 'oct_2004_10_ans', 'oct_2003_11_ans', 
            'oct_2002_12_ans', 'oct_2001_13_ans', 'oct_2000_14_ans', 'avant_2000_plus_14', 
            'dont_redoublants', 'redoublants_avec_cef'
        ]
        widgets = {
            'division_pedagogique': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Division pédagogique'}),
            'annee_etude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Année d\'étude'}),
            'numero_salle_classe': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'N° salle de classe'}),
            'type_classe': forms.Select(attrs={'class': 'form-select'}),
            'numero_enseignant_arabe': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numéro enseignant arabe'}),
            'numero_enseignant_francais': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numéro enseignant francais'}),
            
            'apres_oct_2008_moins_6': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Moins de 6 ans'}),
            'oct_2008_6_ans': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '6 ans'}),
            'oct_2007_7_ans': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '7 ans'}),
            'oct_2006_8_ans': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '8 ans'}),
            'oct_2005_9_ans': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '9 ans'}),
            'oct_2004_10_ans': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '10 ans'}),
            'oct_2003_11_ans': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '11 ans'}),
            'oct_2002_12_ans': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '12 ans'}),
            'oct_2001_13_ans': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '13 ans'}),
            'oct_2000_14_ans': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '14 ans'}),
            'avant_2000_plus_14': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Plus de 14 ans'}),
            'dont_redoublants': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Dont redoublants'}),
            'redoublants_avec_cef': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Redoublants avec CEF'}),
            
        }

from django import forms
from .models import AireRecrutement

class AireRecrutementForm(forms.ModelForm):
    class Meta:
        model = AireRecrutement
        fields = [
            'localite', 'distance',
            'g_1a', 'f_1a', 'g_2a', 'f_2a', 'g_3a', 'f_3a',
            'g_4a', 'f_4a', 'g_5a', 'f_5a', 'g_6a', 'f_6a',
        ]
        widgets = {
            'localite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Localité/Quartier'}),
            'distance': forms.Select(attrs={'class': 'form-select'}),
            'g_1a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Garçons 1A'}),
            'f_1a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Filles 1A'}),
            'g_2a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Garçons 2A'}),
            'f_2a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Filles 2A'}),
            'g_3a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Garçons 3A'}),
            'f_3a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Filles 3A'}),
            'g_4a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Garçons 4A'}),
            'f_4a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Filles 4A'}),
            'g_5a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Garçons 5A'}),
            'f_5a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Filles 5A'}),
            'g_6a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Garçons 6A'}),
            'f_6a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Filles 6A'}),
            # Continue avec les autres champs...
        }

from django import forms
from .models import StatistiqueGenerale

class StatistiqueGeneraleForm(forms.ModelForm):
    class Meta:
        model = StatistiqueGenerale
        fields = ['annee_scolaire', 'total_inscrits', 'total_redoublants']
        widgets = {
            'annee_scolaire': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ex : 2024/2025'
            }),
            'total_inscrits': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre total des inscrits'
            }),
            'total_redoublants': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre total des redoublants'
            }),
        }
        labels = {
            'annee_scolaire': 'Année Scolaire',
            'total_inscrits': 'Total des Inscrits',
            'total_redoublants': 'Total des Redoublants',
        }

    def clean(self):
        """Vérifie la cohérence entre les inscrits et les redoublants."""
        cleaned_data = super().clean()
        
        total_inscrits = cleaned_data.get('total_inscrits', 0)
        total_redoublants = cleaned_data.get('total_redoublants', 0)

        if total_redoublants > total_inscrits:
            raise forms.ValidationError(
                "Le total des redoublants ne peut pas être supérieur au total des inscrits."
            )
        
        return cleaned_data

from django import forms
from .models import MobiliteEleves

from django import forms
from .models import MobiliteEleves

class MobiliteElevesForm(forms.ModelForm):
    class Meta:
        model = MobiliteEleves
        fields = [
            'etablissement',
            'g_1a', 'f_1a', 'g_2a', 'f_2a', 'g_3a', 'f_3a',
            'g_4a', 'f_4a', 'g_5a', 'f_5a', 'g_6a', 'f_6a',
        ]
        widgets = {
            'etablissement': forms.Select(attrs={'class': 'form-select'}),
            'g_1a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Garçons 1A'}),
            'f_1a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Filles 1A'}),
            'g_2a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Garçons 2A'}),
            'f_2a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Filles 2A'}),
            'g_3a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Garçons 3A'}),
            'f_3a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Filles 3A'}),
            'g_4a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Garçons 4A'}),
            'f_4a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Filles 4A'}),
            'g_5a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Garçons 5A'}),
            'f_5a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Filles 5A'}),
            'g_6a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Garçons 6A'}),
            'f_6a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Filles 6A'}),
        }


class StructurePedagogiqueForm(forms.ModelForm):
    class Meta:
        model = StructurePedagogique
        fields = [
            'niveau', 
            'simples', 
            'multigrades', 
            'double_flux',
            'inscrits_garcons', 
            'inscrits_filles', 
            'redoublants_garcons', 
            'redoublants_filles'
        ]
        widgets = {
            'niveau': forms.Select(attrs={'class': 'form-control'}),
            'simples': forms.NumberInput(attrs={'class': 'form-control'}),
            'multigrades': forms.NumberInput(attrs={'class': 'form-control'}),
            'double_flux': forms.NumberInput(attrs={'class': 'form-control'}),
            'inscrits_garcons': forms.NumberInput(attrs={'class': 'form-control'}),
            'inscrits_filles': forms.NumberInput(attrs={'class': 'form-control'}),
            'redoublants_garcons': forms.NumberInput(attrs={'class': 'form-control'}),
            'redoublants_filles': forms.NumberInput(attrs={'class': 'form-control'}),
        }



class ContributionsForm(forms.ModelForm):
    class Meta:
        model = Contributions
        fields = ['contributions_reçues_familles', 'annee_precedente', 'annee_courante']
        labels = {
            'contributions_reçues_familles': "Catégorie de contribution",
            'annee_precedente': "Montant de l'année précédente (FCFA)",
            'annee_courante': "Montant de l'année en cours (FCFA)",
        }
        widgets = {
            'contributions_reçues_familles': forms.Select(attrs={
                'class': 'form-control',
                'aria-label': 'Sélectionnez la catégorie de contribution'
            }),
            'annee_precedente': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',  # Ensures precision for decimal inputs
                'min': '0'  # Prevents negative values
            }),
            'annee_courante': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
        }
class DonneeFinanciereForm(forms.ModelForm):
    class Meta:
        model = DonneeFinanciere
        fields = [
            'categorie',
            'budget_ecole',
            'collectivites',
            'ape',
            'autre',
            'projet_ecole',
            'nature_projet',
            'partenariat',
            'type_partenariat',
        ]
        labels = {
            'categorie': "Catégorie de dépense",
            'budget_ecole': "Budget école (FCFA)",
            'collectivites': "Contribution des collectivités (FCFA)",
            'ape': "Contribution de l'APE (FCFA)",
            'autre': "Autres contributions (FCFA)",
            'projet_ecole': "L'école a-t-elle un projet d'école ?",
            'nature_projet': "Nature du projet",
            'partenariat': "L'école a-t-elle des partenariats ?",
            'type_partenariat': "Type de partenariat",
        }
        widgets = {
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'budget_ecole': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00', 'step': '0.01'}),
            'collectivites': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00', 'step': '0.01'}),
            'ape': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00', 'step': '0.01'}),
            'autre': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00', 'step': '0.01'}),
            'projet_ecole': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nature_projet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Décrivez le projet'}),
            'partenariat': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'type_partenariat': forms.Select(attrs={'class': 'form-control'}),
        }

    
from django import forms
from .models import ObservationEventuelle

class ObservationEventuelleForm(forms.ModelForm):
    # Champ supplémentaire pour une personnalisation plus avancée (exemple)
    class Meta:
        model = ObservationEventuelle
        fields = '__all__'  # Inclut tous les champs du modèle
        widgets = {
            'observations': forms.Textarea(attrs={'placeholder': 'Ajoutez vos observations ici...', 'class': 'form-control'}),
            'directeur_nom': forms.TextInput(attrs={'placeholder': 'Nom du directeur', 'class': 'form-control'}),
            'directeur_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'inspection_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'direction_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
