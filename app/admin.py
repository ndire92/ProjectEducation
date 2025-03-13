from django.contrib import admin
from .models import (
    Activite, Activite_APE, CustomUser, Ecole_identification, LocaliteRurale, Ecole, Local, 
    MobilierEtEquipements, EquipementDidactique, GuideEtManuel, Personnel, 
    NouveauxInscrits, DivisionPedagogique, AireRecrutement, StatistiqueGenerale, 
    MobiliteEleves, StructurePedagogique, FinancesEcole, ObservationEventuelle, 
    SignatureEtCachet
)


# Enregistrement du modèle CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    filter_horizontal = ('groups', 'user_permissions')

# Enregistrement du modèle Ecole_identification
@admin.register(Ecole_identification)
class EcoleIdentificationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'nouveau_code', 'date_creation', 'statut', 'zone')
    search_fields = ('nom', 'nouveau_code', 'ancien_nom')
    list_filter = ('statut', 'zone', 'date_creation')

# Enregistrement du modèle LocaliteRurale
@admin.register(LocaliteRurale)
class LocaliteRuraleAdmin(admin.ModelAdmin):
    list_display = ('type_acces', 'electricite_disponible', 'type_eau', 'service_sante_disponible')
    search_fields = ('type_acces', 'activites_dominantes')
    list_filter = ('electricite_disponible', 'type_eau', 'type_marche')

# Enregistrement du modèle Ecole
from django.contrib import admin
from .models import Ecole

@admin.register(Ecole)
class EcoleAdmin(admin.ModelAdmin):
    # Définir les champs à afficher dans la liste
    list_display = ('nom', 'info_ecole', 'accessible_toute_annee', 'eau_disponible', 'electricite_disponible')

    # Définir les champs à inclure dans la recherche
    search_fields = ('nom', 'type_eau', 'info_ecole')

    # Définir les filtres à afficher dans la barre latérale
    list_filter = ('info_ecole', 'accessible_toute_annee', 'eau_disponible', 'electricite_disponible')

# Modèle Local
@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('numero', 'affectation', 'annee_mise_en_service', 'surface', 'etat_murs', 'etat_toit')
    search_fields = ('affectation', 'numero')
    list_filter = ('etat_murs', 'etat_toit')

# Modèle MobilierEtEquipements
@admin.register(MobilierEtEquipements)
class MobilierEtEquipementsAdmin(admin.ModelAdmin):
    list_display = ('tables_maitre', 'bureaux_maitre', 'ordinateurs', 'bon_etat', 'mauvais_etat')
    search_fields = ('tables_maitre', 'ordinateurs')
    list_filter = ('bon_etat', 'mauvais_etat')

# Modèle EquipementDidactique
@admin.register(EquipementDidactique)
class EquipementDidactiqueAdmin(admin.ModelAdmin):
    list_display = ('regles', 'rapporteurs', 'cartes', 'bon_etat', 'mauvais_etat')
    search_fields = ('regles', 'rapporteurs', 'cartes')
    list_filter = ('bon_etat', 'mauvais_etat')

# Modèle GuideEtManuel
@admin.register(GuideEtManuel)
class GuideEtManuelAdmin(admin.ModelAdmin):
    list_display = ('niveau', 'matiere', 'langue', 'guides', 'manuels')
    search_fields = ('niveau', 'matiere', 'langue')
    list_filter = ('niveau', 'matiere', 'langue')

# Modèle Personnel
@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'fonction', 'genre', 'age', 'niveau_formation', 'formation_continue')
    search_fields = ('nom', 'fonction')
    list_filter = ('genre', 'formation_continue')

# Modèle NouveauxInscrits
@admin.register(NouveauxInscrits)
class NouveauxInscritsAdmin(admin.ModelAdmin):
    list_display = ('situation_prescolaire', 'nombre_garcons', 'nombre_filles', 'total_inscrits')
    search_fields = ('situation_prescolaire',)
    list_filter = ('situation_prescolaire',)

# Modèle DivisionPedagogique
@admin.register(DivisionPedagogique)
class DivisionPedagogiqueAdmin(admin.ModelAdmin):
    list_display = ('niveau', 'numero_salle', 'vacation', 'multigrade', 'double_flux', 'total_eleves')
    search_fields = ('niveau', 'numero_salle')
    list_filter = ('vacation', 'multigrade', 'double_flux')

# Modèle AireRecrutement
@admin.register(AireRecrutement)
class AireRecrutementAdmin(admin.ModelAdmin):
    list_display = ('localite', 'distance_km', 'total_eleves', 'redoublants_garcons', 'redoublants_filles')
    search_fields = ('localite',)
    list_filter = ('distance_km',)

# Modèle StatistiqueGenerale
@admin.register(StatistiqueGenerale)
class StatistiqueGeneraleAdmin(admin.ModelAdmin):
    list_display = ('annee_scolaire', 'total_inscrits', 'total_redoublants')
    search_fields = ('annee_scolaire',)
    list_filter = ('annee_scolaire',)


# Modèle MobiliteEleves
@admin.register(MobiliteEleves)
class MobiliteElevesAdmin(admin.ModelAdmin):
    list_display = ('nom_etablissement', 'localite_origine', 'pays_origine', 'statut_scolarisation', 
                    'nombre_garcons', 'nombre_filles', 'total_redoublants', 'total_eleves')
    search_fields = ('nom_etablissement', 'localite_origine', 'pays_origine')
    list_filter = ('statut_scolarisation',)

# Modèle StructurePedagogique
@admin.register(StructurePedagogique)
class StructurePedagogiqueAdmin(admin.ModelAdmin):
    list_display = ('division', 'nombre_divisions', 'total_eleves', 
                    'redoublants_garcons', 'redoublants_filles', 'multigrade', 'double_flux')
    search_fields = ('division',)
    list_filter = ('multigrade', 'double_flux')

# Modèle FinancesEcole
@admin.register(FinancesEcole)
class FinancesEcoleAdmin(admin.ModelAdmin):
    list_display = ('contributions_familles', 'autres_contributions', 'activites_generatrices_revenus', 
                    'construction_batiments', 'renovation_batiments', 'achat_mobilier', 'salaires_personnel_enseignant')
    search_fields = ('contributions_familles', 'autres_contributions')
    list_filter = ('construction_batiments', 'renovation_batiments', 'achat_mobilier')

# Modèle ObservationEventuelle
@admin.register(ObservationEventuelle)
class ObservationEventuelleAdmin(admin.ModelAdmin):
    list_display = ('contenu', 'date_creation')
    search_fields = ('contenu',)
    list_filter = ('date_creation',)

# Modèle SignatureEtCachet
@admin.register(SignatureEtCachet)
class SignatureEtCachetAdmin(admin.ModelAdmin):
    list_display = ('nom_signataire', 'fonction_signataire', 'date_signature', 'cachet_present')
    search_fields = ('nom_signataire', 'fonction_signataire')
    list_filter = ('fonction_signataire', 'cachet_present')

admin.site.register(Activite)
admin.site.register(Activite_APE)