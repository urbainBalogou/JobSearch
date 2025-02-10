from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect
from .forms import UserTypeForm, LoginForm, OffreForm, PostOffreForm
from offers.models import *
User = get_user_model()


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
    if request.method == "POST":
        # Récupération des données du formulaire
        email = request.POST.get("email")
        mot_de_passe = request.POST.get("mot_de_passe")
        nom = request.POST.get("nom")
        specialite = request.POST.get("specialite")
        niveau = request.POST.get("niveau")
        prenom = request.POST.get("prenom")
        date_naissance = request.POST.get("date_naissance")
        cv = request.FILES.get("cv")

        # Création de l'utilisateur avec email et mot de passe
        try:
            user = User.objects.create_user(username=email, password=mot_de_passe,type="candidat")
            login(request,user)
        except Exception as e:
            messages.error(request, "Erreur lors de la création de l'utilisateur : " + str(e))
            return render(request, 'user/inscription_candidat.html')

        # Création de l'objet Candidat
        # Les champs "niveau_d_etude" et "specialite" sont laissés vides par défaut.
        candidat = Candidat(
            user=user,
            nom=nom,
            prenom=prenom,
            email=email,
            date_naissance=date_naissance,
            niveau_d_etude=niveau,  # Valeur par défaut
            specialite=specialite,  # Valeur par défaut
            cv_ou_attestation=cv
        )
        candidat.save()

        messages.success(request, "Votre inscription a bien été enregistrée.")
        return redirect('index')  # Remplacez 'home' par l'URL de redirection souhaitée

    return render(request, 'user/inscription_candidat.html')

def logout_user(request):
    logout(request)

    return redirect('/')

def login_view(request):
    if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")

            user = authenticate(request, username=email, password=password)  # username = email si personnalisé
            if user:
                login(request, user)
                messages.success(request,"Erreur lors de la connexion")
                return redirect("/")  # Redirige vers la page d'accueil
            else:
                messages.error(request, "Erreur lors de la connexion, identifiants incorrects")

    return render(request, "user/connexion.html")

def recruteur_registration(request):
    if request.method == "POST":
        # Récupération des données du formulaire
        nom_entreprise = request.POST.get("nom_entreprise_ou_recruteur")
        prenom = request.POST.get("prenom")
        domaine_ou_services = request.POST.get("domaine_service")
        situation_geographique = request.POST.get("situation_geographique")
        coordonne_localisation = request.POST.get("coordonne_localisation")
        mot_de_passe = request.POST.get("mdp")
        email = request.POST.get("mail")


        # Création de l'utilisateur avec email et mot de passe
        try:
            user = User.objects.create_user(username=email, password=mot_de_passe, type='recruteur'  )
            print(user)
            login(request,user)
        except Exception as e:
            messages.error(request, "Erreur lors de la création de l'utilisateur : " + str(e))
            return render(request, 'user/inscription_recruteur.html')

        # Création de l'objet Candidat
        # Les champs "niveau_d_etude" et "specialite" sont laissés vides par défaut.
        recruteur = Recruteur(
            user = user,
            nom_entreprise_ou_recruteur=nom_entreprise,
            prenom=prenom,
            email=email,
            domaine_ou_services=domaine_ou_services,  # Valeur par défaut
            situation_geographique=situation_geographique,  # Valeur par défaut
            coordonne_localisation=coordonne_localisation
        )

        recruteur.save()

        messages.success(request, "Votre inscription a bien été enregistrée.")
        return redirect('dashboard_recruteur')  # Remplacez 'home' par l'URL de redirection souhaitée
    return render(request, 'user/inscription_recruteur.html')


@login_required
def dashboard_recruteur(request):
    """
    Tableau de bord qui affiche toutes les offres créées par le recruteur connecté,
    ainsi que les candidatures (PostOffre) associées à chaque offre.
    """
    # On suppose que request.user est lié à un recruteur via request.user.recruteur
    recruteur_id = request.user.recruteur.id

    print("recruteur_id: ",recruteur_id)
    # Récupérer toutes les offres créées par ce recruteur
    offres = Offre.objects.filter(recruteur=recruteur_id).prefetch_related('postoffre_set')

    context = {
        'offres': offres,
    }
    return render(request, 'user/recruteur_dashboard.html', context)


@login_required
def create_offre(request):
    try:
        recruteur = Recruteur.objects.get(user=request.user)  # Récupère l'instance du recruteur
    except Recruteur.DoesNotExist:
        return render(request, 'error.html', {'message': "Vous devez être un recruteur pour créer une offre."})

    if request.method == "POST":
        form = OffreForm(request.POST)
        if form.is_valid():
            offre = form.save(commit=False)  # Ne pas enregistrer tout de suite
            offre.recruteur = recruteur  # Associer le recruteur connecté
            offre.save()  # Enregistrer l'offre
            return redirect('dashboard_recruteur')  # Rediriger après succès
    else:
        form = OffreForm()

    return render(request, 'user/create_offre.html', {'form': form})


@login_required
def postuler_offre(request, offre_id):

    if request.user.type != 'candidat':  # Remplace 'role' et 'recruteur' par tes propres noms de champ et valeur
        return render(request, 'user/error.html', {'message': "Les recruteurs ne peuvent pas postuler à cette offre."})
    print(request.user.type)
    candidat = get_object_or_404(Candidat, user=request.user)  # Vérifie si l'utilisateur est un candidat
    offre = get_object_or_404(Offre, id=offre_id)
    print(request.user.type)
    # Vérifie si l'utilisateur est un recruteur


    # Vérifie si le candidat a déjà postulé à cette offre
    if PostOffre.objects.filter(candidat=candidat, offre=offre).exists():
        return render(request, 'user/error.html', {'message': "Vous avez déjà postulé à cette offre."})

    if request.method == "POST":
        form = PostOffreForm(request.POST)
        if form.is_valid():
            try:
                post_offre = form.save(commit=False)
                post_offre.candidat = candidat  # Associe le candidat connecté
                post_offre.offre = offre  # Associe l'offre concernée
                post_offre.deja_poste = True  # Marque la candidature comme envoyée
                post_offre.save()
                messages.success(request, "Votre candidature est soumis avec succès")
                  # Redirige vers la liste des offres après candidature
            except Exception as e:
                # Capture l'exception spécifique si nécessaire
                return render(request, 'user/error.html', {'message': f"Erreur lors de la candidature : {str(e)}"})
        else:
            return render(request, 'user/error.html', {'message': "Le formulaire est invalide."})

    else:
        form = PostOffreForm()


    return render(request, 'offers/offre_detail.html', {'form': form, 'offre': offre})
