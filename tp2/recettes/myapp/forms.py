from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models



class RecetteForm(ModelForm):

    class Meta:
        model = models.Recette

        fields = ('titre', 'createur', 'temps_preparation', 'description')

        labels = {
            'titre': _('titre'),
            'createur': _('createur'),
            'temps_preparation': _('temps_preparation'),
            'description': _('description'),
        }


class IngredientForm(ModelForm):

    class Meta:
        model = models.Ingredient

        fields = ['recette', 'nom', 'quantite']