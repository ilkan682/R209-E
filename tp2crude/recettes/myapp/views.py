from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .forms import IngredientForm, RecetteForm
from .models import Recette


def index(request):
    return render(request, 'myapp/index.html')


def recette_list(request):
    recettes = Recette.objects.all()

    return render(request, 'myapp/recette_list.html', {
        'recettes': recettes
    })


def recette_detail(request, pk):
    recette = get_object_or_404(Recette, pk=pk)

    return render(request, 'myapp/recette_detail.html', {
        'recette': recette
    })


def recette_form(request):

    if request.method == "POST":

        form = RecetteForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('recette_list')

    else:
        form = RecetteForm()

    return render(request, 'myapp/recette_form.html', {
        'form': form
    })


def ingredient_form(request):

    if request.method == "POST":

        form = IngredientForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('ingredient_form')

    else:
        form = IngredientForm()

    return render(request, 'myapp/ingredient_form.html', {
        'form': form
    })


def recette_confirm_delete(request, pk):

    recette = get_object_or_404(Recette, pk=pk)

    if request.method == "POST":

        recette.delete()

        return redirect('recette_list')

    return render(request, 'myapp/recette_confirm_delete.html', {
        'recette': recette
    })