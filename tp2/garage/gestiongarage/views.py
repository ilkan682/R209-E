from django.shortcuts import render
from .models import Voiture  # On importe notre modèle


def index(request):
    # On récupère toutes les voitures de la base de données
    listevoitures = Voiture.objects.all()

    # On les passe au template HTML via un dictionnaire (le "context")
    return render(request, 'index.html', {'voitures': listevoitures})