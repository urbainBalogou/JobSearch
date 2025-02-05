from django import forms
from .models import Account
from offers.models import Candidat

class UserTypeForm(forms.Form):
    user_type = forms.ChoiceField(choices=Account.CHOICES, label="Choisissez votre type de compte", widget=forms.RadioSelect)


class CandidatForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")

    class Meta:
        model = Candidat
        fields = ['nom', 'prenom', 'email', 'date_naissance', 'niveau_d_etude', 'specialite', 'cv_ou_attestation', 'password']

    def save(self, commit=True):
        user = Account.objects.create_user(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        candidat = super().save(commit=False)
        candidat.user = user
        if commit:
            candidat.save()
        return candidat