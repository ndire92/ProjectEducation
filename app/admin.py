from django.contrib import admin


from .models import (
    Activite, Activite_APE, Contributions, CustomUser, Ecole_identification,LocaliteRurale, Ecole, Local
    , EquipementDidactique, GuideEtManuel,Personnel, 
    NouveauxInscrits, DivisionPedagogique, AireRecrutement, Source_F, StatistiqueGenerale, 
    MobiliteEleves, StructurePedagogique,ObservationEventuelle, 
    MobilierCollectif,DonneeFinanciere
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

#
@admin.register(MobilierCollectif)
class MobilierCollectifAdmin(admin.ModelAdmin):
    list_display = ['nom', 'etat', 'nombre']

admin.site.register(Local)

@admin.register(MobiliteEleves)
class MobiliteElevesAdmin(admin.ModelAdmin):
    # Colonnes affichées
    list_display = (
        'etablissement', 'total_garcons', 'total_filles', 
        'g_1a', 'f_1a', 'g_2a', 'f_2a', 'g_3a', 'f_3a',
        'g_4a', 'f_4a', 'g_5a', 'f_5a', 'g_6a', 'f_6a'
    )
    
    # Filtres latéraux
    list_filter = ('etablissement',)
    
    # Recherche
    search_fields = ('etablissement',)
    
    # Organisation des champs dans des sections
    fieldsets = (
        ('Informations sur l’établissement', {
            'fields': ('etablissement',)
        }),
        ('Répartition des élèves', {
            'fields': (
                ('g_1a', 'f_1a'), ('g_2a', 'f_2a'), 
                ('g_3a', 'f_3a'), ('g_4a', 'f_4a'),
                ('g_5a', 'f_5a'), ('g_6a', 'f_6a')
            )
        }),
        ('Totaux calculés', {
            'fields': ('total_garcons', 'total_filles')
        }),
    )
    
    # Champs en lecture seule
    readonly_fields = ('total_garcons', 'total_filles')

# Modèle EquipementDidactique
@admin.register(EquipementDidactique)
class EquipementDidactiqueAdmin(admin.ModelAdmin):
    list_display = ['nom', 'quantite']  # Utilisez des champs existants du modèle
    list_filter = ['nom']

# Modèle GuideEtManuel
@admin.register(GuideEtManuel)
class GuideEtManuelAdmin(admin.ModelAdmin):
    list_display = ('niveau', 'matiere', 'langue', 'guides', 'manuels')
    search_fields = ('niveau', 'matiere', 'langue')
    list_filter = ('niveau', 'matiere', 'langue')

# Modèle Personnel
@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('numero_ordre', 'matricule_solde', 'genre', 'statut', 'fonction', 'present_ecole')
    list_filter = ('genre', 'statut', 'fonction', 'present_ecole')
    search_fields = ('matricule_solde', 'numero_ordre')

# Modèle NouveauxInscrits
@admin.register(NouveauxInscrits)
class NouveauxInscritsAdmin(admin.ModelAdmin):
    list_display = ('situation_prescolaire', 'nombre_garcons', 'nombre_filles', 'total_inscrits')

    def nombre_garcons(self, obj):
        return obj.garcons  # Retourne la valeur du champ "garcons"

    def nombre_filles(self, obj):
        return obj.filles  # Retourne la valeur du champ "filles"

    def total_inscrits(self, obj):
        return obj.total_inscrits()  # Utilise la méthode `total_inscrits` du modèle

    # Optionnel : Ajoutez des titres conviviaux
    nombre_garcons.short_description = 'Garçons'
    nombre_filles.short_description = 'Filles'
    total_inscrits.short_description = 'Total Inscrits'

# Modèle DivisionPedagogique
@admin.register(DivisionPedagogique)
class DivisionPedagogiqueAdmin(admin.ModelAdmin):
    list_display = (
        'division_pedagogique', 'annee_etude', 'type_classe', 'numero_enseignant_arabe',
        'numero_enseignant_francais', 'total_eleves', 'dont_redoublants', 'avant_2000_plus_14'
    )
    list_filter = ('type_classe', 'numero_enseignant_arabe', 'annee_etude')
    search_fields = ('division_pedagogique', 'annee_etude', 'numero_enseignant_arabe')
    ordering = ('division_pedagogique', 'annee_etude')

    fieldsets = (
        ('Informations de base', {
            'fields': ('division_pedagogique', 'annee_etude', 'type_classe', 'numero_enseignant_arabe', 'numero_enseignant_francais')
        }),
        ('Répartition des âges', {
            'fields': (
                'apres_oct_2008_moins_6', 'oct_2008_6_ans', 'oct_2007_7_ans', 
                'oct_2006_8_ans', 'oct_2005_9_ans', 'oct_2004_10_ans', 
                'oct_2003_11_ans', 'oct_2002_12_ans', 'oct_2001_13_ans', 
                'oct_2000_14_ans', 'avant_2000_plus_14'
            )
        }),
        ('Statistiques supplémentaires', {
            'fields': ('total_eleves', 'dont_redoublants', 'redoublants_avec_cef', 'numero_salle_classe')
        }),
    )
    readonly_fields = ('total_eleves',)  # Champs calculés automatiquement, ne doivent pas être modifiables


# Modèle AireRecrutement
@admin.register(AireRecrutement)
class AireRecrutementAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = (
        'localite', 'distance', 'total_garcons', 'total_filles',
        'g_1a', 'f_1a', 'g_2a', 'f_2a', 'g_3a', 'f_3a',
        'g_4a', 'f_4a', 'g_5a', 'f_5a', 'g_6a', 'f_6a'
    )
    
    # Filtres sur le côté droit
    list_filter = ('distance',)
    
    # Recherche dans les champs
    search_fields = ('localite',)
    
    # Organisation des champs dans des sections
    fieldsets = (
        ('Informations générales', {
            'fields': ('localite', 'distance')
        }),
        ('Répartition des élèves', {
            'fields': (
                ('g_1a', 'f_1a'), ('g_2a', 'f_2a'), ('g_3a', 'f_3a'),
                ('g_4a', 'f_4a'), ('g_5a', 'f_5a'), ('g_6a', 'f_6a')
            )
        }),
        ('Totaux', {
            'fields': ('total_garcons', 'total_filles')
        }),
    )
    
    # Champs en lecture seule
    readonly_fields = ('total_garcons', 'total_filles')

# Modèle StatistiqueGenerale
@admin.register(StatistiqueGenerale)
class StatistiqueGeneraleAdmin(admin.ModelAdmin):
    list_display = ('annee_scolaire', 'total_inscrits', 'total_redoublants')
    search_fields = ('annee_scolaire',)
    list_filter = ('annee_scolaire',)




# Modèle StructurePedagogique

@admin.register(StructurePedagogique)
class StructurePedagogiqueAdmin(admin.ModelAdmin):
    list_display = (
        'niveau',
        'simples',
        'multigrades',
        'double_flux',
        'get_divisions_total',
        'inscrits_garcons',
        'inscrits_filles',
        'get_eleves_total',
        'redoublants_garcons',
        'redoublants_filles',
        'get_redoublants_total'
    )

    list_filter = ('niveau',)  # Exemple pour filtrer par niveaux

    # Méthodes pour afficher les totaux calculés
    @admin.display(description='Total Divisions')
    def get_divisions_total(self, obj):
        return obj.divisions_total

    @admin.display(description='Total Inscrits')
    def get_eleves_total(self, obj):
        return obj.inscrits_total

    @admin.display(description='Total Redoublants')
    def get_redoublants_total(self, obj):
        return obj.redoublants_total
    
    
    


admin.site.register(DonneeFinanciere)
admin.site.register(Contributions)



# Modèle ObservationEventuelle
@admin.register(ObservationEventuelle)
class ObservationEventuelleAdmin(admin.ModelAdmin):
    list_display = ('directeur_nom', 'directeur_date', 'inspection_date', 'direction_date')
    list_filter = ('directeur_date', 'inspection_date', 'direction_date')
    search_fields = ('directeur_nom',)


admin.site.register(Activite)
admin.site.register(Activite_APE)


admin.site.register(Source_F)

