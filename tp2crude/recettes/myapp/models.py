from django.db import models

from django.db import models


class Recette(models.Model):

    titre = models.CharField(max_length=100)

    createur = models.CharField(max_length=100)

    temps_preparation = models.IntegerField()

    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.titre} créée par {self.createur}"


class Ingredient(models.Model):

    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)

    nom = models.CharField(max_length=100)

    quantite = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} ({self.quantite})"
