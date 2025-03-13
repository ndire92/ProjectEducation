from django import forms
from .models import AireRecrutement, DivisionPedagogique, Ecole, Ecole_identification, EquipementDidactique, FinancesEcole, GuideEtManuel, Local, LocaliteRurale,MobilierEtEquipements, MobiliteEleves, NouveauxInscrits, ObservationEventuelle, Personnel, SignatureEtCachet, StatistiqueGenerale, StructurePedagogique

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
            'cantine_fonctionnelle', 'nb_rationnaires', 'nb_de_fille_beneficiaires', 'source_financement',
            'laves_mains_disponibles', 'nb_laves_mains', 'domaine_cloture', 'superficie_cloture', 'type_cloture',
            'espace_recreation_disponible', 'superficie_recreation', 'jardin_scolaire', 'utilisation_de_la_produit',
            'nb_total_latrines', 'nb_latrines_filles', 'nb_latrines_garcons', 'nb_latrines_mixt',
            'ape_existe', 'femmes_ape', 'hommes_ape', 'activites_ape', 'presidence_ape',
            'comite_gestion_existe', 'femmes_comite', 'hommes_comite', 'presidence_comite',
            'distance_centre_sante', 'apport_en_vitamine_A', 'boite_pharmacie_disponible',
            'visite_médicale_année_dernière', 'campagne_de_déparasitage',
            'campagne_de_sensibilisation_au_VIH', 'campagne_de_sensibilisation_au_palu', 'association_eleve'
        ]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'info_ecole': forms.Select(attrs={'class': 'form-control'}),
            'accessible_toute_annee': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'eau_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'type_eau': forms.Select(attrs={'class': 'form-control'}),
            'nb_postes_eau': forms.NumberInput(attrs={'class': 'form-control'}),
            'electricite_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nb_classes_electrifiees': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantine_fonctionnelle': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nb_rationnaires': forms.NumberInput(attrs={'class': 'form-control'}),
            'nb_de_fille_beneficiaires': forms.NumberInput(attrs={'class': 'form-control'}),
            'source_financement': forms.Select(attrs={'class': 'form-control'}),
            'laves_mains_disponibles': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nb_laves_mains': forms.NumberInput(attrs={'class': 'form-control'}),
            'domaine_cloture': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'superficie_cloture': forms.NumberInput(attrs={'class': 'form-control'}),
            'type_cloture': forms.Select(attrs={'class': 'form-control'}),
            'espace_recreation_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'superficie_recreation': forms.NumberInput(attrs={'class': 'form-control'}),
            'jardin_scolaire': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'utilisation_de_la_produit': forms.Select(attrs={'class': 'form-control'}),
            'nb_total_latrines': forms.NumberInput(attrs={'class': 'form-control'}),
            'nb_latrines_filles': forms.NumberInput(attrs={'class': 'form-control'}),
            'nb_latrines_garcons': forms.NumberInput(attrs={'class': 'form-control'}),
            'nb_latrines_mixt': forms.NumberInput(attrs={'class': 'form-control'}),
            'ape_existe': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'femmes_ape': forms.NumberInput(attrs={'class': 'form-control'}),
            'hommes_ape': forms.NumberInput(attrs={'class': 'form-control'}),
            'activites_ape': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'presidence_ape': forms.Select(attrs={'class': 'form-control'}),
            'comite_gestion_existe': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'femmes_comite': forms.NumberInput(attrs={'class': 'form-control'}),
            'hommes_comite': forms.NumberInput(attrs={'class': 'form-control'}),
            'presidence_comite': forms.Select(attrs={'class': 'form-control'}),
            'distance_centre_sante': forms.NumberInput(attrs={'class': 'form-control'}),
            'apport_en_vitamine_A': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'boite_pharmacie_disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'visite_médicale_année_dernière': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'campagne_de_déparasitage': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'campagne_de_sensibilisation_au_VIH': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'campagne_de_sensibilisation_au_palu': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'association_eleve': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_activites_ape(self):
        activites = self.cleaned_data.get('activites_ape', [])
        if len(activites) > 3:
            raise forms.ValidationError("Vous ne pouvez sélectionner que trois activités.")
        return activites

    def clean(self):
        cleaned_data = super().clean()
        total_latrines = cleaned_data.get('nb_total_latrines', 0)
        latrines_filles = cleaned_data.get('nb_latrines_filles', 0)
        latrines_garcons = cleaned_data.get('nb_latrines_garcons', 0)
        latrines_mixt = cleaned_data.get('nb_latrines_mixt', 0)

        if (latrines_filles or latrines_garcons or latrines_mixt) and \
                (latrines_filles + latrines_garcons + latrines_mixt > total_latrines):
            self.add_error('nb_total_latrines', "La somme des latrines pour filles, garçons et mixtes ne peut pas dépasser le nombre total de latrines.")

        return cleaned_data


class EcoleIdentificationForm(forms.ModelForm):
    class Meta:
        model = Ecole_identification
        fields = [
            'ancien_code', 'nouveau_code', 'nom', 'ancien_nom',
            'date_creation', 'statut', 'zone', 'Localisation_administrative', 
            'Localisation_scolaire'
        ]
        widgets = {
            'ancien_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez l\'ancien code'}),
            'nouveau_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nouveau code'}),
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


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = [
            'numero', 'affectation', 'annee_mise_en_service', 
            'surface', 'nature_murs', 'etat_murs', 'nature_toit', 
            'etat_toit', 'nature_sol', 'etat_sol', 'etat_portes', 
            'etat_fenetres', 'source_financement', 'observations'
        ]
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numéro du local'}),
            'affectation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex : Salle de classe, magasin'}),
            'annee_mise_en_service': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex : 1995'}),
            'surface': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Surface en m²'}),
            'nature_murs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex : En dur, semi-dur'}),
            'etat_murs': forms.Select(attrs={'class': 'form-select'}),
            'nature_toit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex : Tôle, chaume'}),
            'etat_toit': forms.Select(attrs={'class': 'form-select'}),
            'nature_sol': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex : Ciment, terre'}),
            'etat_sol': forms.Select(attrs={'class': 'form-select'}),
            'etat_portes': forms.Select(attrs={'class': 'form-select'}),
            'etat_fenetres': forms.Select(attrs={'class': 'form-select'}),
            'source_financement': forms.Select(attrs={'class': 'form-select'}),
            'observations': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observations supplémentaires'}),
        }
        labels = {
            'numero': 'Numéro',
            'affectation': 'Affectation',
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
    


class MobilierEtEquipementsForm(forms.ModelForm):
    class Meta:
        model = MobilierEtEquipements
        fields = [
            'tables_maitre', 'bureaux_maitre', 'chaises_maitre', 
            'tableaux_noirs', 'tableaux_chevalets', 'armoires_bibliotheques', 
            'machines_a_ecrire', 'projecteurs_diapos', 'ordinateurs', 
            'calculatrices', 'bon_etat', 'mauvais_etat', 
            'tables_bancs_1_place', 'tables_bancs_2_places', 
            'tables_bancs_4_places', 'besoins_places_assises'
        ]
        widgets = {
            'tables_maitre': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de tables pour les maîtres'}),
            'bureaux_maitre': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de bureaux'}),
            'chaises_maitre': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de chaises'}),
            'tableaux_noirs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de tableaux noirs'}),
            'tableaux_chevalets': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de tableaux chevalets'}),
            'armoires_bibliotheques': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre d\'armoires/bibliothèques'}),
            'machines_a_ecrire': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de machines à écrire'}),
            'projecteurs_diapos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de projecteurs'}),
            'ordinateurs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre d\'ordinateurs'}),
            'calculatrices': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de calculatrices'}),
            'bon_etat': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre en bon état'}),
            'mauvais_etat': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre en mauvais état'}),
            'tables_bancs_1_place': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de tables-bancs 1 place'}),
            'tables_bancs_2_places': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de tables-bancs 2 places'}),
            'tables_bancs_4_places': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de tables-bancs 4 places'}),
            'besoins_places_assises': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de places assises nécessaires'}),
        }
        labels = {
            'tables_maitre': 'Tables pour maîtres',
            'bureaux_maitre': 'Bureaux pour maîtres',
            'chaises_maitre': 'Chaises pour maîtres',
            'tableaux_noirs': 'Tableaux noirs',
            'tableaux_chevalets': 'Tableaux chevalets',
            'armoires_bibliotheques': 'Armoires/Bibliothèques',
            'machines_a_ecrire': 'Machines à écrire',
            'projecteurs_diapos': 'Projecteurs de diapositives',
            'ordinateurs': 'Ordinateurs',
            'calculatrices': 'Calculatrices',
            'bon_etat': 'Équipements en bon état',
            'mauvais_etat': 'Équipements en mauvais état',
            'tables_bancs_1_place': 'Tables-bancs 1 place',
            'tables_bancs_2_places': 'Tables-bancs 2 places',
            'tables_bancs_4_places': 'Tables-bancs 4 places',
            'besoins_places_assises': 'Besoins en places assises',
        }


from django import forms
from .models import EquipementDidactique

class EquipementDidactiqueForm(forms.ModelForm):
    class Meta:
        model = EquipementDidactique
        fields = [
            'regles', 'rapporteurs', 'cartes', 'bandes_dessinees', 'planches',
            'compas', 'equerres', 'globes', 'litres', 'bon_etat',
            'mauvais_etat', 'eleves_dotes'
        ]
        widgets = {
            'regles': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de règles'}),
            'rapporteurs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de rapporteurs'}),
            'cartes': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de cartes'}),
            'bandes_dessinees': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de bandes dessinées'}),
            'planches': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de planches'}),
            'compas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de compas'}),
            'equerres': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre d\'équerres'}),
            'globes': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de globes terrestres'}),
            'litres': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de litres'}),
            'bon_etat': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre en bon état'}),
            'mauvais_etat': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre en mauvais état'}),
            'eleves_dotes': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre d\'élèves dotés'}),
        }
        labels = {
            'regles': 'Règles',
            'rapporteurs': 'Rapporteurs',
            'cartes': 'Cartes',
            'bandes_dessinees': 'Bandes dessinées',
            'planches': 'Planches',
            'compas': 'Compas',
            'equerres': 'Équerres',
            'globes': 'Globes terrestres',
            'litres': 'Objets pour les mesures (litres)',
            'bon_etat': 'Équipements en bon état',
            'mauvais_etat': 'Équipements en mauvais état',
            'eleves_dotes': 'Élèves dotés',
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
        fields = [
            'nom', 'genre', 'age', 'fonction', 
            'niveau_formation', 'formation_continue'
        ]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Âge'}),
            'fonction': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fonction (Ex : enseignant, directeur)'}),
            'niveau_formation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Niveau de formation'}),
            'formation_continue': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nom': 'Nom',
            'genre': 'Genre',
            'age': 'Âge',
            'fonction': 'Fonction',
            'niveau_formation': 'Niveau de Formation',
            'formation_continue': 'Formation Continue',
        }


from django import forms
from .models import NouveauxInscrits

class NouveauxInscritsForm(forms.ModelForm):
    class Meta:
        model = NouveauxInscrits
        fields = ['situation_prescolaire', 'nombre_garcons', 'nombre_filles', 'total_inscrits']
        widgets = {
            'situation_prescolaire': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex : Garderie, Jardin d\'enfants'}),
            'nombre_garcons': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de garçons'}),
            'nombre_filles': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de filles'}),
            'total_inscrits': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'placeholder': 'Calculé automatiquement'}),
        }
        labels = {
            'situation_prescolaire': 'Situation Préscolaire',
            'nombre_garcons': 'Nombre de Garçons',
            'nombre_filles': 'Nombre de Filles',
            'total_inscrits': 'Total des Inscrits',
        }


from django import forms
from .models import DivisionPedagogique
import json

class DivisionPedagogiqueForm(forms.ModelForm):
    class Meta:
        model = DivisionPedagogique
        fields = [
            'niveau', 'numero_salle', 'vacation', 'multigrade', 
            'double_flux', 'age_6_ans', 'age_7_ans', 'age_8_ans', 
            'total_eleves', 'redoublants'
        ]
        widgets = {
            'niveau': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex : CP, CE1'}),
            'numero_salle': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de salle'}),
            'vacation': forms.Select(attrs={'class': 'form-select'}),
            'multigrade': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'double_flux': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'age_6_ans': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': '{"garcons": 5, "filles": 4}'}),
            'age_7_ans': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': '{"garcons": 7, "filles": 6}'}),
            'age_8_ans': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': '{"garcons": 4, "filles": 5}'}),
            'total_eleves': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'placeholder': 'Calculé automatiquement'}),
            'redoublants': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de redoublants'}),
        }
        labels = {
            'niveau': 'Niveau',
            'numero_salle': 'Numéro de salle',
            'vacation': 'Type de vacation',
            'multigrade': 'Classe multigrade',
            'double_flux': 'Classe à double flux',
            'age_6_ans': 'Répartition des élèves de 6 ans',
            'age_7_ans': 'Répartition des élèves de 7 ans',
            'age_8_ans': 'Répartition des élèves de 8 ans',
            'total_eleves': 'Total des élèves',
            'redoublants': 'Nombre de redoublants',
        }

    def clean(self):
        """Calcul automatique du total des élèves à partir des champs JSON."""
        cleaned_data = super().clean()
        
        ages = ['age_6_ans', 'age_7_ans', 'age_8_ans']  # Tu peux ajouter plus d'âges ici
        total_eleves = 0

        for age_field in ages:
            try:
                data = json.loads(cleaned_data.get(age_field, '{}'))
                total_eleves += data.get("garcons", 0) + data.get("filles", 0)
            except (TypeError, ValueError):
                raise forms.ValidationError(f"Le champ {age_field} doit contenir un JSON valide.")
        
        cleaned_data['total_eleves'] = total_eleves
        return cleaned_data


from django import forms
from .models import AireRecrutement

class AireRecrutementForm(forms.ModelForm):
    class Meta:
        model = AireRecrutement
        fields = [
            'localite', 'distance_km', 'nombre_eleves_garcons', 
            'nombre_eleves_filles', 'total_eleves', 
            'redoublants_garcons', 'redoublants_filles'
        ]
        widgets = {
            'localite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la localité ou du quartier'}),
            'distance_km': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Distance estimée (en km)'}),
            'nombre_eleves_garcons': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de garçons'}),
            'nombre_eleves_filles': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de filles'}),
            'total_eleves': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'placeholder': 'Calculé automatiquement'}),
            'redoublants_garcons': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de garçons redoublants'}),
            'redoublants_filles': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de filles redoublantes'}),
        }
        labels = {
            'localite': 'Localité/Quartier',
            'distance_km': 'Distance (km)',
            'nombre_eleves_garcons': 'Nombre d\'élèves garçons',
            'nombre_eleves_filles': 'Nombre d\'élèves filles',
            'total_eleves': 'Total des élèves',
            'redoublants_garcons': 'Garçons redoublants',
            'redoublants_filles': 'Filles redoublantes',
        }

    def clean(self):
        """Calcul automatique du total des élèves en fonction du nombre de garçons et filles."""
        cleaned_data = super().clean()

        # Récupération des données des champs
        garcons = cleaned_data.get('nombre_eleves_garcons', 0)
        filles = cleaned_data.get('nombre_eleves_filles', 0)
        total = garcons + filles

        # Mise à jour automatique du champ 'total_eleves'
        cleaned_data['total_eleves'] = total

        # Vérification de cohérence
        if total < 0:
            raise forms.ValidationError("Le total des élèves ne peut pas être négatif.")

        return cleaned_data


from django import forms
from .models import AireRecrutement

class AireRecrutementForm(forms.ModelForm):
    class Meta:
        model = AireRecrutement
        fields = [
            'localite', 'distance_km', 'nombre_eleves_garcons', 
            'nombre_eleves_filles', 'total_eleves', 
            'redoublants_garcons', 'redoublants_filles'
        ]
        widgets = {
            'localite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la localité ou du quartier'}),
            'distance_km': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Distance estimée (en km)'}),
            'nombre_eleves_garcons': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de garçons'}),
            'nombre_eleves_filles': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de filles'}),
            'total_eleves': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'placeholder': 'Calculé automatiquement'}),
            'redoublants_garcons': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de garçons redoublants'}),
            'redoublants_filles': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de filles redoublantes'}),
        }
        labels = {
            'localite': 'Localité/Quartier',
            'distance_km': 'Distance (km)',
            'nombre_eleves_garcons': 'Nombre d\'élèves garçons',
            'nombre_eleves_filles': 'Nombre d\'élèves filles',
            'total_eleves': 'Total des élèves',
            'redoublants_garcons': 'Garçons redoublants',
            'redoublants_filles': 'Filles redoublantes',
        }

    def clean(self):
        """Calcul automatique du total des élèves en fonction du nombre de garçons et filles."""
        cleaned_data = super().clean()

        # Récupération des données des champs
        garcons = cleaned_data.get('nombre_eleves_garcons', 0)
        filles = cleaned_data.get('nombre_eleves_filles', 0)
        total = garcons + filles

        # Mise à jour automatique du champ 'total_eleves'
        cleaned_data['total_eleves'] = total

        # Vérification de cohérence
        if total < 0:
            raise forms.ValidationError("Le total des élèves ne peut pas être négatif.")

        return cleaned_data

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

class MobiliteElevesForm(forms.ModelForm):
    class Meta:
        model = MobiliteEleves
        fields = [
            'nom_etablissement', 'localite_origine', 'pays_origine', 
            'statut_scolarisation', 'nombre_garcons', 'nombre_filles', 
            'total_redoublants', 'total_eleves'
        ]
        widgets = {
            'nom_etablissement': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nom de l\'établissement fréquenté'
            }),
            'localite_origine': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Localité ou commune d\'origine'
            }),
            'pays_origine': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Pays d\'origine (laisser vide si non applicable)'
            }),
            'statut_scolarisation': forms.Select(attrs={
                'class': 'form-select'
            }),
            'nombre_garcons': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre de garçons'
            }),
            'nombre_filles': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre de filles'
            }),
            'total_redoublants': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre total de redoublants'
            }),
            'total_eleves': forms.NumberInput(attrs={
                'class': 'form-control', 
                'readonly': 'readonly', 
                'placeholder': 'Calculé automatiquement'
            }),
        }
        labels = {
            'nom_etablissement': 'Nom de l\'établissement',
            'localite_origine': 'Localité d\'origine',
            'pays_origine': 'Pays d\'origine',
            'statut_scolarisation': 'Statut de scolarisation',
            'nombre_garcons': 'Nombre de garçons',
            'nombre_filles': 'Nombre de filles',
            'total_redoublants': 'Total des redoublants',
            'total_eleves': 'Total des élèves',
        }

    def clean(self):
        """Calculer automatiquement le total des élèves et valider les données."""
        cleaned_data = super().clean()
        nombre_garcons = cleaned_data.get('nombre_garcons', 0)
        nombre_filles = cleaned_data.get('nombre_filles', 0)
        total_eleves = nombre_garcons + nombre_filles

        cleaned_data['total_eleves'] = total_eleves

        # Validation : redoublants ne peuvent pas excéder le total des élèves
        total_redoublants = cleaned_data.get('total_redoublants', 0)
        if total_redoublants > total_eleves:
            raise forms.ValidationError(
                "Le total des redoublants ne peut pas être supérieur au total des élèves."
            )

        return cleaned_data


from django import forms
from .models import StructurePedagogique

class StructurePedagogiqueForm(forms.ModelForm):
    class Meta:
        model = StructurePedagogique
        fields = [
            'division', 'nombre_divisions', 'nombre_eleves_garcons', 
            'nombre_eleves_filles', 'total_eleves', 'redoublants_garcons', 
            'redoublants_filles', 'total_redoublants', 'multigrade', 'double_flux'
        ]
        widgets = {
            'division': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ex : CP, CE1'
            }),
            'nombre_divisions': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre de divisions pédagogiques'
            }),
            'nombre_eleves_garcons': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre d\'élèves garçons'
            }),
            'nombre_eleves_filles': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre d\'élèves filles'
            }),
            'total_eleves': forms.NumberInput(attrs={
                'class': 'form-control', 
                'readonly': 'readonly', 
                'placeholder': 'Calculé automatiquement'
            }),
            'redoublants_garcons': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre de garçons redoublants'
            }),
            'redoublants_filles': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre de filles redoublantes'
            }),
            'total_redoublants': forms.NumberInput(attrs={
                'class': 'form-control', 
                'readonly': 'readonly', 
                'placeholder': 'Calculé automatiquement'
            }),
            'multigrade': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'double_flux': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'division': 'Division Pédagogique',
            'nombre_divisions': 'Nombre de Divisions',
            'nombre_eleves_garcons': 'Nombre d\'élèves garçons',
            'nombre_eleves_filles': 'Nombre d\'élèves filles',
            'total_eleves': 'Total des élèves',
            'redoublants_garcons': 'Nombre de garçons redoublants',
            'redoublants_filles': 'Nombre de filles redoublantes',
            'total_redoublants': 'Total des redoublants',
            'multigrade': 'Classe multigrade',
            'double_flux': 'Classe à double flux',
        }

    def clean(self):
        """Validation et calcul automatique des champs dérivés."""
        cleaned_data = super().clean()
        nombre_eleves_garcons = cleaned_data.get('nombre_eleves_garcons', 0)
        nombre_eleves_filles = cleaned_data.get('nombre_eleves_filles', 0)
        redoublants_garcons = cleaned_data.get('redoublants_garcons', 0)
        redoublants_filles = cleaned_data.get('redoublants_filles', 0)

        # Calcul des totaux
        total_eleves = nombre_eleves_garcons + nombre_eleves_filles
        total_redoublants = redoublants_garcons + redoublants_filles

        cleaned_data['total_eleves'] = total_eleves
        cleaned_data['total_redoublants'] = total_redoublants

        # Validation cohérente
        if total_redoublants > total_eleves:
            raise forms.ValidationError(
                "Le total des redoublants ne peut pas être supérieur au total des élèves."
            )

        return cleaned_data


from django import forms
from .models import FinancesEcole

class FinancesEcoleForm(forms.ModelForm):
    class Meta:
        model = FinancesEcole
        fields = '__all__'  # Inclut automatiquement tous les champs du modèle
        widgets = {  # Ajout de widgets pour personnaliser l'affichage
            'contributions_familles': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Contributions des familles'}),
            'autres_contributions': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Autres contributions'}),
            'activites_generatrices_revenus': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Revenus issus d\'activités'}),
            'construction_batiments': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Dépenses de construction'}),
            'renovation_batiments': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Dépenses de rénovation'}),
            'achat_mobilier': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Achat de mobilier'}),
            'renovation_mobilier': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rénovation du mobilier'}),
            'achat_equipements_pedagogiques': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Équipements pédagogiques'}),
            'logement_enseignants': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Logement pour enseignants'}),
            'salaires_personnel_enseignant': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salaires enseignants'}),
            'salaires_personnel_autre': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Autres salaires'}),
            'cantine_scolaire': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Budget cantine'}),
            'financement_projets': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Financements projets'}),
        }
        labels = {  # Ajout d'étiquettes lisibles
            'contributions_familles': 'Contributions des familles',
            'autres_contributions': 'Autres contributions',
            'activites_generatrices_revenus': 'Revenus générés',
            'construction_batiments': 'Construction des bâtiments',
            'renovation_batiments': 'Rénovation des bâtiments',
            'achat_mobilier': 'Achat de mobilier',
            'renovation_mobilier': 'Rénovation de mobilier',
            'achat_equipements_pedagogiques': 'Achat d’équipements pédagogiques',
            'logement_enseignants': 'Logement des enseignants',
            'salaires_personnel_enseignant': 'Salaires du personnel enseignant',
            'salaires_personnel_autre': 'Salaires du personnel autre',
            'cantine_scolaire': 'Budget pour la cantine',
            'financement_projets': 'Financement des projets',
        }


from django import forms
from .models import ObservationEventuelle

class ObservationEventuelleForm(forms.ModelForm):
    # Champ supplémentaire pour une personnalisation plus avancée (exemple)
    commentaire_supplementaire = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Ajoutez un commentaire si nécessaire',
            'rows': 3
        }),
        label='Commentaire supplémentaire'
    )

    class Meta:
        model = ObservationEventuelle
        fields = ['contenu']  # Inclut uniquement les champs souhaités du modèle
        widgets = {
            'contenu': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez vos observations détaillées ici...',
                'rows': 6
            }),
        }
        labels = {
            'contenu': 'Observations principales',
        }
from django import forms
from .models import SignatureEtCachet

class SignatureEtCachetForm(forms.ModelForm):
    class Meta:
        model = SignatureEtCachet
        fields = '__all__'  # Inclut tous les champs du modèle
        widgets = {
            'observation': forms.Select(attrs={'class': 'form-control'}),  # Menu déroulant pour lier une observation existante
            'nom_signataire': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom du signataire'
            }),
            'fonction_signataire': forms.Select(attrs={'class': 'form-control'}),  # Menu déroulant pour les choix de fonction
            'date_signature': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'YYYY-MM-DD'
            }),
            'cachet_present': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Case à cocher
        }
        labels = {
            'observation': 'Observation liée',
            'nom_signataire': 'Nom du signataire',
            'fonction_signataire': 'Fonction du signataire',
            'date_signature': 'Date de signature',
            'cachet_present': 'Cachet apposé',
        }
