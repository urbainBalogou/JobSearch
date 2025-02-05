from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import UserTypeForm


def choose_account_type(request):
    if request.method == 'POST':
       form = UserTypeForm(request.POST)
       if form.is_valid():
           user_type = form.cleaned_data['user_type']
           # Rediriger vers la page spécifique en fonction du type de compte
           if user_type == 'candidat':
               return redirect('candidat_registration')  # Remplacer par l'URL pour l'inscription candidat
           elif user_type == 'recruteur':
               return redirect('recruteur_registration') # Remplacer par l'URL pour l'inscription recruteur
    else:
        form = UserTypeForm()

    return render(request, 'user/choix_compte.html', {'form': form})

def candidat_registration(request):
    return render(request, 'user/inscription_candidat.html')

def recruteur_registration(request):
    return render(request, 'user/inscription_recruteur.html')

