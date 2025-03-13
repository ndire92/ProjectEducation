# Generated by Django 5.1.7 on 2025-03-13 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_localiterurale_activites_dominantes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecole',
            name='activites_ape',
            field=models.ManyToManyField(help_text="Sélectionnez jusqu'à trois activités.", related_name='ecoles', to='app.activite_ape'),
        ),
        migrations.AlterField(
            model_name='localiterurale',
            name='activites_dominantes',
            field=models.ManyToManyField(help_text="Sélectionnez jusqu'à trois activités économiques dominantes.", related_name='localites', to='app.activite'),
        ),
    ]
