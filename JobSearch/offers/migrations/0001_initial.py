# Generated by Django 5.1.3 on 2025-02-01 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('renumeration_min', models.PositiveIntegerField()),
                ('renumeration_max', models.PositiveIntegerField()),
                ('niveau_requis', models.CharField(max_length=128)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.categorie')),
            ],
        ),
    ]
