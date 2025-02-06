from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import UserTypeForm
from .forms import RegisterForm


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

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from .forms import RegisterForm

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
        return render(request, 'register.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm
from .models import Account

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = Account.objects.get(email=email)  # Trouver l'utilisateur avec l'email
                user = authenticate(request, username=user.username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('home')  # Redirection après connexion réussie
                else:
                    form.add_error(None, "Email ou mot de passe incorrect.")

            except Account.DoesNotExist:
                form.add_error(None, "Cet email n'existe pas.")

    else:
        form = LoginForm()

    return render(request, 'user/connexion.html', {'form': form})
from django.shortcuts import render

def connexion_view(request):
    return render(request, 'user/connexion.html')  # Vérifie que le chemin est correct
