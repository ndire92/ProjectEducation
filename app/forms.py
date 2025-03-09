from django import forms
from .models import AireRecrutement, DivisionPedagogique, Ecole, Ecole_identification, EquipementDidactique, FinancesEcole, GuideEtManuel, Local, LocaliteRurale,MobilierEtEquipements, MobiliteEleves, NouveauxInscrits, ObservationEventuelle, Personnel, SignatureEtCachet, StatistiqueGenerale, StructurePedagogique

class EcoleForm(forms.ModelForm):
    class Meta:
        model = Ecole
        fields = '__all__'

class EcoleIdentificationForm(forms.ModelForm):
    class Meta:
        model = Ecole_identification
        fields = '__all__'
        widgets = {
            'date_creation': forms.DateInput(attrs={'type': 'date'}),
            'statut': forms.RadioSelect(choices=[('public', 'Public'), ('prive', 'Privé')]),
            'zone': forms.RadioSelect(choices=[('rurale', 'Rurale'), ('urbaine', 'Urbaine')]),
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
        fields = '__all__'  # Inclure tous les champs
        widgets = {
            'type_acces': forms.Select(attrs={'class': 'form-select'}),
            'type_eau': forms.Select(attrs={'class': 'form-select'}),
            'type_service_sante': forms.Select(attrs={'class': 'form-select'}),
            'type_marche': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_activites_dominantes(self):
        activites = self.cleaned_data.get('activites_dominantes')
        if len(activites.split(',')) > 3:
            raise forms.ValidationError("Veuillez limiter à trois activités dominantes, séparées par des virgules.")
        return activites


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = '__all__'  # Inclure tous les champs
        widgets = {
            'etat_murs': forms.Select(attrs={'class': 'form-select'}),
            'etat_toit': forms.Select(attrs={'class': 'form-select'}),
            'etat_sol': forms.Select(attrs={'class': 'form-select'}),
            'etat_portes': forms.Select(attrs={'class': 'form-select'}),
            'etat_fenetres': forms.Select(attrs={'class': 'form-select'}),
            'source_financement': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if numero <= 0:
            raise forms.ValidationError("Le numéro doit être un entier positif.")
        return numero
    
    


class MobilierEtEquipementsForm(forms.ModelForm):
    class Meta:
        model = MobilierEtEquipements
        fields = '__all__'  # Inclure tous les champs
        widgets = {
            'tables_maitre': forms.NumberInput(attrs={'class': 'form-control'}),
            'bureaux_maitre': forms.NumberInput(attrs={'class': 'form-control'}),
            'chaises_maitre': forms.NumberInput(attrs={'class': 'form-control'}),
            'ordinateurs': forms.NumberInput(attrs={'class': 'form-control'}),
            'besoins_places_assises': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_bon_etat(self):
        bon_etat = self.cleaned_data.get('bon_etat')
        if bon_etat < 0:
            raise forms.ValidationError("Le nombre d'éléments en bon état ne peut pas être négatif.")
        return bon_etat



class EquipementDidactiqueForm(forms.ModelForm):
    class Meta:
        model = EquipementDidactique
        fields = '__all__'
        widgets = {
            'regles': forms.NumberInput(attrs={'class': 'form-control'}),
            'rapporteurs': forms.NumberInput(attrs={'class': 'form-control'}),
            'bon_etat': forms.NumberInput(attrs={'class': 'form-control'}),
            'mauvais_etat': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class GuideEtManuelForm(forms.ModelForm):
    class Meta:
        model = GuideEtManuel
        fields = '__all__'
        widgets = {
            'niveau': forms.Select(attrs={'class': 'form-select'}),
            'matiere': forms.Select(attrs={'class': 'form-select'}),
            'langue': forms.Select(attrs={'class': 'form-select'}),
            'guides': forms.NumberInput(attrs={'class': 'form-control'}),
            'manuels': forms.NumberInput(attrs={'class': 'form-control'}),
        }



class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'fonction': forms.TextInput(attrs={'class': 'form-control'}),
            'niveau_formation': forms.TextInput(attrs={'class': 'form-control'}),
            'formation_continue': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class NouveauxInscritsForm(forms.ModelForm):
    class Meta:
        model = NouveauxInscrits
        fields = '__all__'
        widgets = {
            'situation_prescolaire': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_garcons': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_filles': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_inscrits': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class DivisionPedagogiqueForm(forms.ModelForm):
    class Meta:
        model = DivisionPedagogique
        fields = '__all__'
        widgets = {
            'niveau': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_salle': forms.NumberInput(attrs={'class': 'form-control'}),
            'vacation': forms.Select(attrs={'class': 'form-select'}),
            'multigrade': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'double_flux': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'age_6_ans': forms.Textarea(attrs={'class': 'form-control'}),
            'total_eleves': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class AireRecrutementForm(forms.ModelForm):
    class Meta:
        model = AireRecrutement
        fields = '__all__'
        widgets = {
            'localite': forms.TextInput(attrs={'class': 'form-control'}),
            'distance_km': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_eleves_garcons': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_eleves_filles': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_eleves': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class StatistiqueGeneraleForm(forms.ModelForm):
    class Meta:
        model = StatistiqueGenerale
        fields = '__all__'
        widgets = {
            'annee_scolaire': forms.TextInput(attrs={'class': 'form-control'}),
            'total_inscrits': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_redoublants': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class MobiliteElevesForm(forms.ModelForm):
    class Meta:
        model = MobiliteEleves
        fields = '__all__'
        widgets = {
            'nom_etablissement': forms.TextInput(attrs={'class': 'form-control'}),
            'localite_origine': forms.TextInput(attrs={'class': 'form-control'}),
            'pays_origine': forms.TextInput(attrs={'class': 'form-control'}),
            'statut_scolarisation': forms.Select(attrs={'class': 'form-select'}),
            'nombre_garcons': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_filles': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_redoublants': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_eleves': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class StructurePedagogiqueForm(forms.ModelForm):
    class Meta:
        model = StructurePedagogique
        fields = '__all__'
        widgets = {
            'division': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_divisions': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_eleves_garcons': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_eleves_filles': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_eleves': forms.NumberInput(attrs={'class': 'form-control'}),
            'multigrade': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class FinancesEcoleForm(forms.ModelForm):
    class Meta:
        model = FinancesEcole
        fields = '__all__'
        widgets = {
            'contributions_familles': forms.NumberInput(attrs={'class': 'form-control'}),
            'autres_contributions': forms.NumberInput(attrs={'class': 'form-control'}),
            'construction_batiments': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantine_scolaire': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ObservationEventuelleForm(forms.ModelForm):
    class Meta:
        model = ObservationEventuelle
        fields = '__all__'
        widgets = {
            'contenu': forms.Textarea(attrs={'class': 'form-control'}),
        }

class SignatureEtCachetForm(forms.ModelForm):
    class Meta:
        model = SignatureEtCachet
        fields = '__all__'
        widgets = {
            'nom_signataire': forms.TextInput(attrs={'class': 'form-control'}),
            'fonction_signataire': forms.Select(attrs={'class': 'form-select'}),
            'date_signature': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cachet_present': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
