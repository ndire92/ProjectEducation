# Generated by Django 5.1.7 on 2025-03-13 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_ecole_identification_ancien_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Do',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EtatFenetre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EtatMur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EtatPorte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EtatSol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EtatToit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NatureMur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NatureSol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NatureToit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SourceFinancement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='local',
            name='affectation',
        ),
        migrations.RemoveField(
            model_name='local',
            name='etat_fenetres',
        ),
        migrations.RemoveField(
            model_name='local',
            name='etat_murs',
        ),
        migrations.RemoveField(
            model_name='local',
            name='etat_portes',
        ),
        migrations.RemoveField(
            model_name='local',
            name='etat_sol',
        ),
        migrations.RemoveField(
            model_name='local',
            name='etat_toit',
        ),
        migrations.RemoveField(
            model_name='local',
            name='nature_murs',
        ),
        migrations.RemoveField(
            model_name='local',
            name='nature_sol',
        ),
        migrations.RemoveField(
            model_name='local',
            name='nature_toit',
        ),
        migrations.AlterField(
            model_name='local',
            name='numero',
            field=models.IntegerField(unique=True),
        ),
        migrations.RemoveField(
            model_name='local',
            name='source_financement',
        ),
        migrations.AlterField(
            model_name='local',
            name='surface',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='local',
            name='affectation_du_local',
            field=models.ManyToManyField(related_name='locaux', to='app.affec'),
        ),
        migrations.AddField(
            model_name='local',
            name='dont',
            field=models.ManyToManyField(related_name='locaux', to='app.do'),
        ),
        migrations.AddField(
            model_name='local',
            name='etat_fenetres',
            field=models.ManyToManyField(related_name='locaux', to='app.etatfenetre'),
        ),
        migrations.AddField(
            model_name='local',
            name='etat_murs',
            field=models.ManyToManyField(related_name='locaux', to='app.etatmur'),
        ),
        migrations.AddField(
            model_name='local',
            name='etat_portes',
            field=models.ManyToManyField(related_name='locaux', to='app.etatporte'),
        ),
        migrations.AddField(
            model_name='local',
            name='etat_sol',
            field=models.ManyToManyField(related_name='locaux', to='app.etatsol'),
        ),
        migrations.AddField(
            model_name='local',
            name='etat_toit',
            field=models.ManyToManyField(related_name='locaux', to='app.etattoit'),
        ),
        migrations.AddField(
            model_name='local',
            name='nature_murs',
            field=models.ManyToManyField(related_name='locaux', to='app.naturemur'),
        ),
        migrations.AddField(
            model_name='local',
            name='nature_sol',
            field=models.ManyToManyField(related_name='locaux', to='app.naturesol'),
        ),
        migrations.AddField(
            model_name='local',
            name='nature_toit',
            field=models.ManyToManyField(related_name='locaux', to='app.naturetoit'),
        ),
        migrations.AddField(
            model_name='local',
            name='source_financement',
            field=models.ManyToManyField(related_name='locaux', to='app.sourcefinancement'),
        ),
    ]
