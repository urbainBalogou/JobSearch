from django import forms
from .models import Account
from offers.models import *

class UserTypeForm(forms.Form):
    user_type = forms.ChoiceField(choices=Account.CHOICES, label="Choisissez votre type de compte", widget=forms.RadioSelect)


class CandidatForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")

    class Meta:
        model = Candidat
        fields = ['nom', 'prenom', 'email', 'date_naissance', 'niveau_d_etude', 'specialite', 'cv_ou_attestation', 'password']



class OffreForm(forms.ModelForm):
    class Meta:
        model = Offre
        fields = [
            'categorie',
            'nom',
            'description',
            'renumeration_min',
            'renumeration_max',
            'type_de_contrat',
            'niveau_requis',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'type_de_contrat': forms.Select(),
            'categorie': forms.Select(),
        }


class PostOffreForm(forms.ModelForm):
    class Meta:
        model = PostOffre
        fields = []  # Seul le statut est modifiable (le reste est automatique)
        widgets = {
            'status': forms.Select(),
        }


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))