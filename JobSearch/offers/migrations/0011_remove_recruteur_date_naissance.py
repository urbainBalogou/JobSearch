# Generated by Django 5.1.3 on 2025-02-07 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0010_recruteur_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruteur',
            name='date_naissance',
        ),
    ]
