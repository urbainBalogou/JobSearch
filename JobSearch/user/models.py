from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


class Account(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="account_users",  # Change ici le nom
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="account_users_permissions",  # Change ici le nom
        blank=True
    )
    CHOICES = (
        ('candidat', 'Candidat'),
        ('recruteur', 'Recruteur'),
    )
    type = models.CharField(max_length=10, choices=CHOICES)

    def __str__(self):
        return self.type
