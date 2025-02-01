from django.shortcuts import render, get_object_or_404
from .models  import *

def index(request):
    return render(request, 'offers/index.html')


def getOffre(request,id):
    offres = Offre.objects.filter(categorie__id=id)
    return render(request,"offers/offre.html",{"offres":offres})

def getCategorie(request):
    categories = Categorie.objects.all()
    return render(request, "offers/categorie.html",{"categories":categories})