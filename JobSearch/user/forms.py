from django import forms
from .models import Account
from offers.models import Candidat

class UserTypeForm(forms.Form):
    user_type = forms.ChoiceField(
        choices=Account.CHOICES,
        label="Choisissez votre type de compte",
        widget=forms.RadioSelect
    )

class CandidatForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")

    class Meta:
        model = Candidat
        fields = ['nom', 'prenom', 'email', 'date_naissance', 'niveau_d_etude', 'specialite', 'cv_ou_attestation', 'password']

    def save(self, commit=True):
        user = Account.objects.create_user(
            username=self.cleaned_data['email'],  # Utilisation de l'email comme username
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        candidat = super().save(commit=False)
        candidat.user = user
        if commit:
            candidat.save()
        return candidat

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirmer le mot de passe")

    class Meta:
        model = Account  # Utilisation du bon modèle
        fields = ['email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Les mots de passe ne correspondent pas.")

        return cleaned_data
class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
