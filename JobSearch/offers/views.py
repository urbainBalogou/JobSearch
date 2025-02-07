from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Offre, Categorie

def index(request):
    return render(request, 'offers/index.html')

def getOffre(request, id):
    offres = Offre.objects.filter(categorie__id=id)
    paginator = Paginator(offres, 4)  # 4 offres par page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "offers/offre.html", {"page_obj": page_obj})

def getCategorie(request):
    categories = Categorie.objects.all()
    paginator = Paginator(categories, 4)  # 4 catégories par page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "offers/categorie.html", {"page_obj": page_obj})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django import forms


class ConnexionForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Votre email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Votre mot de passe'}))


def connexion_view(request):
    form = ConnexionForm()

    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email,
                                password=password)  # Attention : Django utilise "username" par défaut

            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige vers la page d'accueil
            else:
                form.add_error(None, "Email ou mot de passe incorrect.")

    return render(request, 'connexion.html', {'form': form})
