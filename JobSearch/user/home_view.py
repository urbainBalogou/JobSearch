from django.shortcuts import redirect

def home_view(request):
    return redirect('connexion')  # Redirige vers la page de connexion
