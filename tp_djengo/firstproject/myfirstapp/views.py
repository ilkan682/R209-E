from django.shortcuts import render, get_object_or_404, redirect  # Importations ajoutées ici
from django.http import HttpResponseRedirect
from .forms import LivreForm
from . import models

# Crée un nouveau livre
def ajout(request):
    if request.method == "POST":
        form = LivreForm(request.POST)
        if form.is_valid():
            Livre = form.save()
            return render(request, "myfirstapp/affiche.html", {"Livre": Livre})
        else:
            return render(request, "myfirstapp/ajout.html", {"form": form})
    else:
        form = LivreForm()
        return render(request, "myfirstapp/ajout.html", {"form": form})

# Ancienne fonction de traitement (gardée si utilisée ailleurs, sinon tu peux la supprimer)
def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save()
        return render(request, "myfirstapp/affiche.html", {"Livre": Livre})
    else:
        return render(request, "myfirstapp/ajout.html", {"form": lform})

# Affiche un livre spécifique
def read(request, id):
    Livre = models.Livre.objects.get(pk=id)
    return render(request, "myfirstapp/affiche.html", {"Livre": Livre})

# Gère l'affichage ET la modification d'un livre (GET et POST)
def traitementupdate(request, id):
    # On récupère le livre ou on renvoie une vraie erreur 404 proprement si l'ID n'existe pas
    livre = get_object_or_404(models.Livre, pk=id)

    if request.method == "POST":
        # On lie le formulaire aux données envoyées (POST) et au livre existant (instance)
        lform = LivreForm(request.POST, instance=livre)
        if lform.is_valid():
            lform.save()  # Met à jour le livre existant
            return redirect('index')  # Redirige vers la page d'accueil
        else:
            return render(request, "myfirstapp/update.html", {"form": lform, "id": id})
    else:
        # Requête GET : On pré-remplit le formulaire avec les données du livre
        lform = LivreForm(instance=livre)
        return render(request, "myfirstapp/update.html", {"form": lform, "id": id})

# Affiche la liste de tous les livres
def index(request):
    tous_les_livres = list(models.Livre.objects.all())
    return render(request, "myfirstapp/index.html", {"liste": tous_les_livres})

# Supprime un livre
def delete(request, id):
    livre = models.Livre.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("/myfirstapp/")