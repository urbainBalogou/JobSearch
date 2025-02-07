from django.shortcuts import render

# Vue pour la page de connexion


def connexion_view(request):
    return render(request, 'user/connexion.html')  # Utiliser 'user/connexion.html'
