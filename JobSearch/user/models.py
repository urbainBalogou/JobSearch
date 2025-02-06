from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

class Account(AbstractUser):
    email = models.EmailField(unique=True)  # Utilisation de l'email comme identifiant
    username = None  # Supprime le username

    groups = models.ManyToManyField(
        Group,
        related_name="account_users",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="account_users_permissions",
        blank=True
    )

    CHOICES = (
        ('candidat', 'Candidat'),
        ('recruteur', 'Recruteur'),
    )
    type = models.CharField(max_length=10, choices=CHOICES)

    USERNAME_FIELD = 'email'  # Authentification avec email
    REQUIRED_FIELDS = []  # Supprime username des champs obligatoires

    def __str__(self):
        return self.email  # Affiche l'email au lieu du type
