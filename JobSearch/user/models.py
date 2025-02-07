from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models




class Account(AbstractUser):

    CHOICES = (
        ('candidat', 'Candidat'),
        ('recruteur', 'Recruteur'),
    )
    type = models.CharField(max_length=10, choices=CHOICES)

    def __str__(self):
        return self.type
