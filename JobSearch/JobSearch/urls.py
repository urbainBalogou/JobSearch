"""
URL configuration for JobSearch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import connexion_view

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from offers import views
from JobSearch import settings
from user.views import RegisterView  # Assure-toi que RegisterView est bien défini dans views.py
from jobsearch.views import connexion_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('categorie/', views.getCategorie,name="categorie"),
    path('categorie/<int:id>/', views.getOffre,name="offres"),
    path('user/', include('user.urls_user')),
    path('inscription/', RegisterView.as_view(), name="inscription"),
    path('connexion/', connexion_view, name='connexion'),  # URL pour la connexion

     path('connexion/', connexion_view, name='connexion'),
    # Ajoute ici les URL de redirection pour les comptes candidats et recruteurs

    #path('recruteur-inscription/', views.recruteur_registration, name='recruteur_registration'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .views import connexion_view  # Assure-toi que la vue est bien importée



