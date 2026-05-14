from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LivreForm
from . import models

def ajout(request):
    if request.method == "POST":
        form = LivreForm(request.POST)
        if form.is_valid():
             Livre = form.save()
             return render(request,"myfirstapp/affiche.html",{"Livre" : Livre})

        else:
            return render(request,"myfirstapp/ajout.html",{"form": form})
    else :
        form = LivreForm()
        return render(request,"myfirstapp/ajout.html",{"form" : form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save()
        return render(request,"myfirstapp/affiche.html",{"Livre" : Livre})
    else:
        return render(request,"myfirstapp/ajout.html",{"form": lform})

def read(request, id):
        Livre = models.Livre.objects.get(pk=id)

        return render(request,"myfirstapp/affiche.html",{"Livre": Livre})

def update(request, id):
    livre = models.Livre.objects.get(pk=id)

    form = LivreForm(instance=livre)
    return render(request, "myfirstapp/update.html", {"form": form, "id": id})

def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save(commit=False)
        Livre.id = id;
        Livre.save()
        return HttpResponseRedirect("/myfirstapp/")

    else:
        return render(request, "myfirstapp/update.html", {"form": lform, "id": id})


# Affiche la liste de tous les livres (Vue "All")
def index(request):
    tous_les_livres = list(models.Livre.objects.all())
    return render(request, "myfirstapp/index.html", {"liste": tous_les_livres})

# Supprime un livre
def delete(request, id):
    livre = models.Livre.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("/myfirstapp/")


