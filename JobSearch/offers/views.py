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
