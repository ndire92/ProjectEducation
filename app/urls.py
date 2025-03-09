from django.urls import path
from .views import (
    gestion_ecole, identi_ecole, supprimer_ecole, supprimer_identification,
    gestion_localites, supprimer_localite, gestion_locaux, supprimer_local,
    gestion_mobilier, supprimer_mobilier, gestion_equipements, supprimer_equipement,
    gestion_guides, supprimer_guide, gestion_personnel, supprimer_personnel,
    gestion_inscriptions, supprimer_inscription, gestion_divisions, supprimer_division,
    gestion_aires, supprimer_aire
)
from . import views  # Ajout pour gérer les statistiques et la mobilité

urlpatterns = [
    # Gestion des écoles
    path('ecoles/', gestion_ecole, name='gestion_ecole'),
    path('ecoles/<int:pk>/', gestion_ecole, name='gestion_ecole'),
    path('ecoles/supprimer/<int:pk>/', supprimer_ecole, name='supprimer_ecole'),

    # Identification des écoles
    path('identification_ecoles/', identi_ecole, name='identification'),
    path('identification_/<int:pk>/', identi_ecole, name='identification'),
    path('identification_ecoles/supprimer/<int:pk>/', supprimer_identification, name='supprimer_identification'),

    # Gestion des localités
    path('localites/', gestion_localites, name='gestion_localites'),
    path('localites/<int:pk>/', gestion_localites, name='gestion_localites'),
    path('localites/supprimer/<int:pk>/', supprimer_localite, name='supprimer_localite'),

    # Gestion des locaux
    path('locaux/', gestion_locaux, name='gestion_locaux'),
    path('locaux/<int:pk>/', gestion_locaux, name='gestion_locaux'),
    path('locaux/supprimer/<int:pk>/', supprimer_local, name='supprimer_local'),

    # Gestion du mobilier
    path('mobilier/', gestion_mobilier, name='gestion_mobilier'),
    path('mobilier/<int:pk>/', gestion_mobilier, name='gestion_mobilier'),
    path('mobilier/supprimer/<int:pk>/', supprimer_mobilier, name='supprimer_mobilier'),

    # Gestion des équipements
    path('equipements/', gestion_equipements, name='gestion_equipements'),
    path('equipements/<int:pk>/', gestion_equipements, name='gestion_equipements'),
    path('equipements/supprimer/<int:pk>/', supprimer_equipement, name='supprimer_equipement'),

    # Gestion des guides
    path('guides/', gestion_guides, name='gestion_guides'),
    path('guides/<int:pk>/', gestion_guides, name='gestion_guides'),
    path('guides/supprimer/<int:pk>/', supprimer_guide, name='supprimer_guide'),

    # Gestion du personnel
    path('personnel/', gestion_personnel, name='gestion_personnel'),
    path('personnel/<int:pk>/', gestion_personnel, name='gestion_personnel'),
    path('personnel/supprimer/<int:pk>/', supprimer_personnel, name='supprimer_personnel'),

    # Gestion des inscriptions
    path('inscriptions/', gestion_inscriptions, name='gestion_inscriptions'),
    path('inscriptions/<int:pk>/', gestion_inscriptions, name='gestion_inscriptions'),
    path('inscriptions/supprimer/<int:pk>/', supprimer_inscription, name='supprimer_inscription'),

    # Gestion des divisions
    path('divisions/', gestion_divisions, name='gestion_divisions'),
    path('divisions/<int:pk>/', gestion_divisions, name='gestion_divisions'),
    path('divisions/supprimer/<int:pk>/', supprimer_division, name='supprimer_division'),

    # Gestion des aires
    path('aires/', gestion_aires, name='gestion_aires'),
    path('aires/<int:pk>/', gestion_aires, name='gestion_aires'),
    path('aires/supprimer/<int:pk>/', supprimer_aire, name='supprimer_aire'),

    # Statistiques
    path('statistiques/', views.gestion_statistiques, name='gestion_statistiques'),
    path('statistiques/<int:pk>/', views.gestion_statistiques, name='gestion_statistiques'),
    path('statistiques/supprimer/<int:pk>/', views.supprimer_statistique, name='supprimer_statistique'),

    # Mobilité
    path('mobilite/', views.gestion_mobilite, name='gestion_mobilite'),
    path('mobilite/<int:pk>/', views.gestion_mobilite, name='gestion_mobilite'),
    path('mobilite/supprimer/<int:pk>/', views.supprimer_mobilite, name='supprimer_mobilite'),


    path('structures/', views.gestion_structures, name='gestion_structures'),
    path('structures/<int:pk>/', views.gestion_structures, name='gestion_structures'),
    path('structures/supprimer/<int:pk>/', views.supprimer_structure, name='supprimer_structure'),
   
   
    path('finances/', views.gestion_finances, name='gestion_finances'),
    path('finances/<int:pk>/', views.gestion_finances, name='gestion_finances'),
    path('finances/supprimer/<int:pk>/', views.supprimer_finance, name='supprimer_finance'),

    path('observations/', views.gestion_observations, name='gestion_observations'),
    path('observations/<int:pk>/', views.gestion_observations, name='gestion_observations'),
    path('observations/supprimer/<int:pk>/', views.supprimer_observation, name='supprimer_observation'),
   
   
   
    path('signatures/', views.gestion_signatures, name='gestion_signatures'),
    path('signatures/<int:pk>/', views.gestion_signatures, name='gestion_signatures'),
    path('signatures/supprimer/<int:pk>/', views.supprimer_signature, name='supprimer_signature'),





]











