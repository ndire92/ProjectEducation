# Generated by Django 5.1.7 on 2025-03-16 01:27

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(choices=[('cultures_vivrières', 'Cultures vivrières'), ('elevage', 'Élevage'), ('cultures_maraîchères', 'Cultures maraîchères'), ('peche', 'Pêche'), ('cultures_fruitières', 'Cultures fruitières'), ('artisanat', 'Artisanat'), ('cultures_industrielles', 'Cultures industrielles'), ('autres', 'Autres')], max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Activite_APE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(choices=[('construction', 'Construction'), ('réhabilitation', 'Réhabilitation'), ('suivi_présence_des_enseignants', 'Suivi présence des enseignants'), ('Activités_de_sensibilisation', 'Activités de sensibilisation'), ('cantine', 'Cantine'), ('autres', 'Autres')], max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Affectation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AireRecrutement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localite', models.CharField(max_length=100, verbose_name='Localité/Quartier')),
                ('distance', models.CharField(choices=[('moins_de_1km', '<1 km'), ('entre_1_et_3km', '1-3 km'), ('entre_3_et_5km', '3-5 km'), ('plus_de_5km', '>5 km'), ('indetermine', 'Indéterminée')], max_length=20, verbose_name="Distance de l'école")),
                ('g_1a', models.PositiveIntegerField(default=0, verbose_name='Garçons 1A')),
                ('f_1a', models.PositiveIntegerField(default=0, verbose_name='Filles 1A')),
                ('g_2a', models.PositiveIntegerField(default=0, verbose_name='Garçons 2A')),
                ('f_2a', models.PositiveIntegerField(default=0, verbose_name='Filles 2A')),
                ('g_3a', models.PositiveIntegerField(default=0, verbose_name='Garçons 3A')),
                ('f_3a', models.PositiveIntegerField(default=0, verbose_name='Filles 3A')),
                ('g_4a', models.PositiveIntegerField(default=0, verbose_name='Garçons 4A')),
                ('f_4a', models.PositiveIntegerField(default=0, verbose_name='Filles 4A')),
                ('g_5a', models.PositiveIntegerField(default=0, verbose_name='Garçons 5A')),
                ('f_5a', models.PositiveIntegerField(default=0, verbose_name='Filles 5A')),
                ('g_6a', models.PositiveIntegerField(default=0, verbose_name='Garçons 6A')),
                ('f_6a', models.PositiveIntegerField(default=0, verbose_name='Filles 6A')),
                ('total_garcons', models.PositiveIntegerField(default=0, verbose_name='Total Garçons')),
                ('total_filles', models.PositiveIntegerField(default=0, verbose_name='Total Filles')),
            ],
        ),
        migrations.CreateModel(
            name='Contributions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contributions_reçues_familles', models.CharField(choices=[('montant_global', "Montant GLOBAL annuel de la cotisation de l'Association des Parents d'Elèves"), ('cotisations_parents', "Autres cotisations des parents d'élèves"), ('frais_inscription', "Montant GLOBAL des frais d'inscription (pour le privé)"), ('autres_contributions', 'Autres contributions (ONG, Individus, etc.)'), ('activites_generatrices_revenus', 'Activités génératrices de revenus')], max_length=50, verbose_name='Catégorie de contribution')),
                ('annee_precedente', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('annee_courante', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'verbose_name': 'Contribution financière',
                'verbose_name_plural': 'Contributions financières',
            },
        ),
        migrations.CreateModel(
            name='DivisionPedagogique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division_pedagogique', models.CharField(max_length=100, verbose_name='Division pédagogique')),
                ('annee_etude', models.CharField(max_length=50, verbose_name="Année d'étude/Niveau")),
                ('numero_salle_classe', models.PositiveIntegerField(verbose_name='N°  salle de classe')),
                ('type_classe', models.CharField(choices=[('simple', 'Simple vacation'), ('double', 'Double vacation'), ('multigrad', 'Multi-grade')], max_length=10, verbose_name='Type de classe')),
                ('numero_enseignant_arabe', models.PositiveIntegerField(verbose_name='N° ordre arabe')),
                ('numero_enseignant_francais', models.PositiveIntegerField(verbose_name='N° ordre francais')),
                ('apres_oct_2008_moins_6', models.PositiveIntegerField(default=0, verbose_name='Moins de 6 ans (après octobre 2008)')),
                ('oct_2008_6_ans', models.PositiveIntegerField(default=0, verbose_name='6 ans (Oct-08)')),
                ('oct_2007_7_ans', models.PositiveIntegerField(default=0, verbose_name='7 ans (Oct-07)')),
                ('oct_2006_8_ans', models.PositiveIntegerField(default=0, verbose_name='8 ans (Oct-06)')),
                ('oct_2005_9_ans', models.PositiveIntegerField(default=0, verbose_name='9 ans (Oct-05)')),
                ('oct_2004_10_ans', models.PositiveIntegerField(default=0, verbose_name='10 ans (Oct-04)')),
                ('oct_2003_11_ans', models.PositiveIntegerField(default=0, verbose_name='11 ans (Oct-03)')),
                ('oct_2002_12_ans', models.PositiveIntegerField(default=0, verbose_name='12 ans (Oct-02)')),
                ('oct_2001_13_ans', models.PositiveIntegerField(default=0, verbose_name='13 ans (Oct-01)')),
                ('oct_2000_14_ans', models.PositiveIntegerField(default=0, verbose_name='14 ans (Oct-00)')),
                ('avant_2000_plus_14', models.PositiveIntegerField(default=0, verbose_name='Plus de 14 ans (Avant 2000)')),
                ('total_eleves', models.PositiveIntegerField(default=0, verbose_name='Total')),
                ('dont_redoublants', models.PositiveIntegerField(default=0, verbose_name='Dont redoublants')),
                ('redoublants_avec_cef', models.PositiveIntegerField(default=0, verbose_name='Redoublants 6ème année avec CEF')),
            ],
        ),
        migrations.CreateModel(
            name='DonneeFinanciere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(choices=[('construction_batiments', 'Construction bâtiments'), ('renovation_batiments', 'Rénovation bâtiments'), ('achat_mobilier', 'Achat de mobilier'), ('renovation_mobilier', 'Rénovation de mobilier'), ('achat_equipements_pedagogiques', 'Achat équipements pédagogiques'), ('achat_manuels_scolaires', 'Achat de manuels scolaires'), ('logements_enseignants', 'Logements des enseignants'), ('factures_eau', "Factures d'eau"), ('factures_electricite', "Factures d'électricité"), ('factures_telephone', 'Factures de téléphone'), ('salaire_enseignants', 'Salaire personnel enseignant'), ('salaire_personnel_autre', 'Salaire personnel autre'), ('cantines_scolaires', 'Cantines scolaires')], max_length=50, verbose_name='Catégorie de dépense')),
                ('budget_ecole', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Budget école')),
                ('collectivites', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Collectivités')),
                ('ape', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='APE')),
                ('autre', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='AUTRE')),
                ('projet_ecole', models.BooleanField(default=False, verbose_name="L'école envisage-t-elle un projet d'école ?")),
                ('nature_projet', models.CharField(blank=True, help_text='Décrivez le projet si applicable', max_length=255, null=True, verbose_name='Nature du projet')),
                ('partenariat', models.BooleanField(default=False, verbose_name="L'école a-t-elle établi un ou des partenariats ?")),
                ('type_partenariat', models.CharField(blank=True, choices=[('jumelage', 'Jumelage'), ('ong', 'ONG'), ('prive', 'Privé')], max_length=20, null=True, verbose_name='Type de partenariat')),
            ],
        ),
        migrations.CreateModel(
            name='Dont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DotationEleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_eleves_dotes', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ecole_identification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ancien_code', models.CharField(blank=True, max_length=16, null=True)),
                ('nouveau_code', models.CharField(blank=True, max_length=16, null=True)),
                ('nom', models.CharField(max_length=200)),
                ('ancien_nom', models.CharField(blank=True, max_length=200, null=True)),
                ('date_creation', models.DateField(blank=True, null=True)),
                ('statut', models.CharField(blank=True, choices=[('public', 'Public'), ('prive', 'Privé')], max_length=20, null=True)),
                ('Localisation_administrative', models.CharField(blank=True, choices=[('wilaya', 'Wilaya'), ('moughataa', 'Moughataa'), ('commune', 'Commune'), ('localite', 'Localite')], max_length=20, null=True)),
                ('Localisation_scolaire', models.CharField(blank=True, choices=[('dren', 'dren'), ('iden', 'iden')], max_length=20, null=True)),
                ('zone', models.CharField(blank=True, choices=[('rurale', 'Rurale'), ('urbaine', 'Urbaine')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EquipementDidactique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('quantite', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EtatFenetre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EtatMurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EtatPortes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EtatSol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EtatToit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GuideEtManuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau', models.CharField(choices=[('1A', '1ère Année'), ('2A', '2ème Année'), ('3A', '3ème Année'), ('4A', '4ème Année'), ('5A', '5ème Année'), ('6A', '6ème Année')], max_length=10)),
                ('matiere', models.CharField(choices=[('lecture', 'Lecture'), ('calcul', 'Calcul'), ('science', 'Science'), ('histoire', 'Histoire'), ('geographie', 'Géographie'), ('education_islamique', 'Éducation Islamique'), ('instruction_civique', 'Instruction Civique')], max_length=100)),
                ('langue', models.CharField(choices=[('arabe', 'Arabe'), ('francais', 'Français')], max_length=50)),
                ('guides', models.IntegerField(blank=True, null=True)),
                ('manuels', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MobilierCollectif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('etat', models.CharField(choices=[('bon_acceptable', 'Bon / acceptable'), ('mauvais', 'Mauvais')], max_length=20)),
                ('nombre', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MobilierEleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_table_banc', models.CharField(choices=[('1_place', '1 place'), ('2_places', '2 places'), ('4_places', '4 places')], max_length=10)),
                ('etat', models.CharField(choices=[('bon_acceptable', 'Bon / acceptable'), ('mauvais', 'Mauvais')], max_length=20)),
                ('nombre', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MobiliteEleves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etablissement', models.CharField(choices=[('meme_ecole', 'Même école'), ('ecole_meme_moughataa', 'École fondamentale de la même Moughataa'), ('ecole_autre_moughataa', "École d'une autre Moughataa, même Wilaya"), ('ecole_autre_wilaya', "École fondamentale d'une autre Wilaya"), ('ecole_etranger', "École d'un pays étranger"), ('prescolaire', 'Préscolaire'), ('mahadra', 'Mahadra'), ('non_scolarise', 'Non scolarisés'), ('origine_inconnue', 'Origine non connue')], max_length=50, verbose_name='Établissement fréquenté')),
                ('g_1a', models.PositiveIntegerField(default=0, verbose_name='Garçons 1A')),
                ('f_1a', models.PositiveIntegerField(default=0, verbose_name='Filles 1A')),
                ('g_2a', models.PositiveIntegerField(default=0, verbose_name='Garçons 2A')),
                ('f_2a', models.PositiveIntegerField(default=0, verbose_name='Filles 2A')),
                ('g_3a', models.PositiveIntegerField(default=0, verbose_name='Garçons 3A')),
                ('f_3a', models.PositiveIntegerField(default=0, verbose_name='Filles 3A')),
                ('g_4a', models.PositiveIntegerField(default=0, verbose_name='Garçons 4A')),
                ('f_4a', models.PositiveIntegerField(default=0, verbose_name='Filles 4A')),
                ('g_5a', models.PositiveIntegerField(default=0, verbose_name='Garçons 5A')),
                ('f_5a', models.PositiveIntegerField(default=0, verbose_name='Filles 5A')),
                ('g_6a', models.PositiveIntegerField(default=0, verbose_name='Garçons 6A')),
                ('f_6a', models.PositiveIntegerField(default=0, verbose_name='Filles 6A')),
                ('total_garcons', models.PositiveIntegerField(default=0, editable=False, verbose_name='Total Garçons')),
                ('total_filles', models.PositiveIntegerField(default=0, editable=False, verbose_name='Total Filles')),
            ],
        ),
        migrations.CreateModel(
            name='NatureMurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NatureSol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NatureToit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NouveauxInscrits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situation_prescolaire', models.CharField(choices=[('garderie', 'Garderie'), ('jardin_enfants', "Jardins d'enfants"), ('ecole_coraniques', 'Ecoles coraniques'), ('aucun_enseignement', 'Aucun enseignement'), ('origine_non_connu', 'Origine non connue')], max_length=50, verbose_name='Situation préscolaire')),
                ('garcons', models.IntegerField(default=0, verbose_name='Garçons')),
                ('filles', models.IntegerField(default=0, verbose_name='Filles')),
            ],
        ),
        migrations.CreateModel(
            name='ObservationEventuelle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observations', models.TextField(blank=True, null=True, verbose_name='Observations éventuelles')),
                ('directeur_nom', models.CharField(blank=True, max_length=255, null=True, verbose_name="Nom du directeur de l'école")),
                ('directeur_date', models.DateField(blank=True, null=True, verbose_name="Date (Directeur de l'école)")),
                ('directeur_signature', models.BooleanField(default=False, verbose_name="Signature et cachet (Directeur de l'école)")),
                ('inspection_date', models.DateField(blank=True, null=True, verbose_name='Date (Inspection départementale)')),
                ('inspection_signature', models.BooleanField(default=False, verbose_name='Signature et cachet (Inspection départementale)')),
                ('direction_date', models.DateField(blank=True, null=True, verbose_name='Date (Direction régionale)')),
                ('direction_signature', models.BooleanField(default=False, verbose_name='Signature et cachet (Direction régionale)')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ordre', models.IntegerField(verbose_name='N° ordre du fonctionnaire')),
                ('matricule_solde', models.CharField(max_length=50, verbose_name='Matricule/solde')),
                ('genre', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme')], max_length=1, verbose_name='Genre')),
                ('annee_naissance', models.IntegerField(verbose_name='Année de naissance')),
                ('annee_recrutement', models.IntegerField(verbose_name='Année de recrutement')),
                ('annee_arrivee_ecole', models.IntegerField(verbose_name="Année d'arrivée à l'école")),
                ('statut', models.CharField(choices=[('Instituteur adjoint', 'Instituteur adjoint'), ('Instituteur', 'Instituteur'), ('Moniteur', 'Moniteur'), ('Contractuel', 'Contractuel'), ('Stagiaire', 'Stagiaire'), ('Autre', 'Autre')], max_length=50, verbose_name='Statut')),
                ('fonction', models.CharField(choices=[('Directeur', 'Directeur'), ('Enseignant classe', 'Enseignant classe'), ('Suppléant', 'Suppléant'), ("Personnel d'appui", "Personnel d'appui"), ('ENI-Normal', 'ENI-Normal'), ('ENI-Adaptée', 'ENI-Adaptée'), ('Autres', 'Autres')], max_length=50, verbose_name='Fonction')),
                ('formation_initiale', models.CharField(choices=[('normal', 'ENI-Normal'), ('accéléré', ' ENI- Accéléré'), ('autres', 'Autres'), ('sans', 'Sans')], max_length=20, verbose_name='Formation professionnelle')),
                ('formation_continue', models.CharField(choices=[('Multigrade', 'Multigrade'), (' Double-flux', 'Double-flux'), ('APC', 'APC'), ('langueFranc_ou_Arab', 'Langue (Franc ou Arab.)'), (' gestion_pédagogique', 'Gestion pédagogique'), ('Gestion_cantine', 'Gestion cantine'), ('vih', 'VIH')], max_length=20, verbose_name='Formation continue')),
                ('langue_formation', models.CharField(choices=[('Arabe', 'Arabe'), ('Français', 'Français')], max_length=20, verbose_name='Langue de formation')),
                ('langue_travail', models.CharField(choices=[('Arabe', 'Arabe'), ('Français', 'Français'), ('Anglais', 'Anglais')], max_length=20, verbose_name='Langue de travail')),
                ('peut_enseigner', models.CharField(choices=[('Arabe', 'Arabe'), ('Français', 'Français'), ('Anglais', 'Anglais')], max_length=20, verbose_name='Peut enseigner en')),
                ('nombre_inspections', models.IntegerField(verbose_name="Nombre d'inspections l'année passée")),
                ('present_ecole', models.BooleanField(default=True, verbose_name="Effectivement présent dans l'école")),
            ],
        ),
        migrations.CreateModel(
            name='SourceFinancement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StatistiqueGenerale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee_scolaire', models.CharField(max_length=10)),
                ('total_inscrits', models.IntegerField(default=0)),
                ('total_redoublants', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StructurePedagogique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau', models.CharField(choices=[('1A', '1A'), ('2A', '2A'), ('3A', '3A'), ('4A', '4A'), ('5A', '5A'), ('6A', '6A')], max_length=2, unique=True)),
                ('simples', models.PositiveIntegerField(default=0, verbose_name='Divisions simples')),
                ('multigrades', models.PositiveIntegerField(default=0, verbose_name='Divisions multigrades')),
                ('double_flux', models.PositiveIntegerField(default=0, verbose_name='Divisions double flux')),
                ('inscrits_garcons', models.PositiveIntegerField(default=0, verbose_name='Élèves garçons inscrits')),
                ('inscrits_filles', models.PositiveIntegerField(default=0, verbose_name='Élèves filles inscrites')),
                ('redoublants_garcons', models.PositiveIntegerField(default=0, verbose_name='Redoublants garçons')),
                ('redoublants_filles', models.PositiveIntegerField(default=0, verbose_name='Redoublants filles')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customuser_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ecole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('info_ecole', models.CharField(blank=True, choices=[('ouverte', 'ouverte'), ('veilleuse', 'Veilleuse')], max_length=20, null=True)),
                ('accessible_toute_annee', models.BooleanField()),
                ('eau_disponible', models.BooleanField()),
                ('type_eau', models.CharField(blank=True, choices=[('robiet', 'Robiet'), ('citerne', 'Citerne'), ('puits_avec_cloture', 'Puits avec cloture'), ('puits_avec_margelle', 'Puits avec margelle')], max_length=20, null=True)),
                ('nb_postes_eau', models.IntegerField(blank=True, null=True)),
                ('electricite_disponible', models.BooleanField()),
                ('nb_classes_electrifiees', models.IntegerField(blank=True, null=True)),
                ('cantine_fonctionnelle', models.BooleanField()),
                ('nb_rationnaires', models.IntegerField(blank=True, null=True)),
                ('nb_de_fille_beneficiaires', models.IntegerField(blank=True, null=True)),
                ('source_financement', models.CharField(blank=True, choices=[('gvt', 'GVT'), ('pam', 'PAM'), ('autres', 'Autres')], max_length=20, null=True)),
                ('laves_mains_disponibles', models.BooleanField()),
                ('nb_laves_mains', models.IntegerField(blank=True, null=True)),
                ('domaine_cloture', models.BooleanField()),
                ('superficie_cloture', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('type_cloture', models.CharField(blank=True, choices=[('dur', 'Dur'), ('banco', 'Banco'), ('haie', 'Haie'), ('grillage', 'Grillage'), ('semi_dur', 'Semi-dur')], max_length=20, null=True)),
                ('espace_recreation_disponible', models.BooleanField()),
                ('superficie_recreation', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('jardin_scolaire', models.BooleanField()),
                ('utilisation_de_la_produit', models.CharField(blank=True, choices=[('vendu', 'Vendu'), ('distribue', 'Distribue'), ('cantine', 'Cantine')], max_length=20, null=True)),
                ('nb_latrines_filles', models.IntegerField(blank=True, default=0, null=True)),
                ('nb_latrines_garcons', models.IntegerField(blank=True, default=0, null=True)),
                ('nb_latrines_mixt', models.IntegerField(blank=True, default=0, null=True)),
                ('nb_total_latrines', models.IntegerField(blank=True, default=0, null=True)),
                ('ape_existe', models.BooleanField()),
                ('femmes_ape', models.IntegerField(blank=True, null=True)),
                ('hommes_ape', models.IntegerField(blank=True, null=True)),
                ('presidence_ape', models.CharField(blank=True, choices=[('homme', 'Homme'), ('femme', 'Femme')], max_length=20, null=True)),
                ('comite_gestion_existe', models.BooleanField()),
                ('femmes_comite', models.IntegerField(blank=True, null=True)),
                ('hommes_comite', models.IntegerField(blank=True, null=True)),
                ('presidence_comite', models.CharField(blank=True, choices=[('homme', 'Homme'), ('femme', 'Femme')], max_length=20, null=True)),
                ('distance_centre_sante', models.IntegerField(blank=True, null=True)),
                ('apport_en_vitamine_A', models.BooleanField()),
                ('boite_pharmacie_disponible', models.BooleanField()),
                ('visite_médicale_année_dernière', models.BooleanField()),
                ('campagne_de_déparasitage', models.BooleanField()),
                ('campagne_de_sensibilisation_au_VIH', models.BooleanField()),
                ('campagne_de_sensibilisation_au_palu', models.BooleanField()),
                ('association_eleve', models.BooleanField()),
                ('activites_ape', models.ManyToManyField(help_text="Sélectionnez jusqu'à trois activités.", related_name='ecoles', to='app.activite_ape')),
            ],
        ),
        migrations.CreateModel(
            name='LocaliteRurale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_acces', models.CharField(choices=[('route_goudronnee', 'Route goudronnée'), ('route_bitumee', 'Route bitumée'), ('accessible_tous_vehicules', 'Piste accessible à tous véhicules'), ('vehicule_tout_terrain', 'Piste accessible véhicule tout terrain'), ('uniquement_pied', 'Accessible uniquement à pied'), ('autre', 'Autre accès (à préciser)')], max_length=100)),
                ('electricite_disponible', models.BooleanField()),
                ('type_eau', models.CharField(choices=[('robinets', 'Robinets'), ('puits_cloture', 'Puits clôturés ou avec margelle'), ('puits_non_cloture', 'Puits non clôturés sans margelle'), ('citerne', 'Citerne'), ('eaux_surface', 'Fleuve, mare, marigot'), ('forage', 'Forage')], max_length=100)),
                ('service_sante_disponible', models.BooleanField()),
                ('type_service_sante', models.CharField(blank=True, choices=[('poste', 'Poste de santé'), ('unite_base', 'Unité de santé de base'), ('autres', 'Autres services de santé')], max_length=100, null=True)),
                ('mosquee_disponible', models.BooleanField()),
                ('mahadra_disponible', models.BooleanField()),
                ('bibliotheque_disponible', models.BooleanField()),
                ('terrain_sport_disponible', models.BooleanField()),
                ('autres_structures_animation', models.TextField(blank=True, null=True)),
                ('type_marche', models.CharField(choices=[('permanent', 'Permanent'), ('hebdomadaire', 'Hebdomadaire'), ('absent', 'Pas de marché')], max_length=100)),
                ('type_de_coperation', models.CharField(choices=[('agricole', 'Agricole'), ('pastoral', 'Pastoral'), ('artisanal', 'Artisanal'), ('autre', 'Autres')], max_length=100)),
                ('developpe_socio_économique', models.BooleanField()),
                ('secteur_intervention', models.CharField(blank=True, choices=[('agricole', 'Agricole'), ('pastoral', 'Pastoral'), ('hydraulique', 'Hydraulique'), ('sante', 'Santé'), ('educatif', 'Éducatif'), ('artisanal', 'Artisanal')], max_length=100, null=True)),
                ('bailleurs_ong', models.TextField(blank=True, null=True)),
                ('activites_dominantes', models.ManyToManyField(help_text="Sélectionnez jusqu'à trois activités économiques dominantes.", related_name='localites', to='app.activite')),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=100)),
                ('annee_mise_en_service', models.IntegerField()),
                ('surface', models.FloatField()),
                ('observations', models.TextField()),
                ('affectation_du_local', models.ManyToManyField(to='app.affectation')),
                ('dont', models.ManyToManyField(to='app.dont')),
                ('etat_fenetres', models.ManyToManyField(to='app.etatfenetre')),
                ('etat_murs', models.ManyToManyField(to='app.etatmurs')),
                ('etat_portes', models.ManyToManyField(to='app.etatportes')),
                ('etat_sol', models.ManyToManyField(to='app.etatsol')),
                ('etat_toit', models.ManyToManyField(to='app.etattoit')),
                ('nature_murs', models.ManyToManyField(to='app.naturemurs')),
                ('nature_sol', models.ManyToManyField(to='app.naturesol')),
                ('nature_toit', models.ManyToManyField(to='app.naturetoit')),
                ('source_financement', models.ManyToManyField(to='app.sourcefinancement')),
            ],
        ),
    ]
