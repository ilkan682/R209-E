from django.forms import ModelForm
from .models import Recette, Ingredient


class RecetteForm(ModelForm):

    class Meta:
        model = Recette

        fields = ['titre', 'createur', 'temps_preparation', 'description']


class IngredientForm(ModelForm):

    class Meta:
        model = Ingredient

        fields = ['recette', 'nom', 'quantite']