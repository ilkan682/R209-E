from django.db import models

# Create your models here.
from django.db import models

class Voiture(models.Model):
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    immatriculation = models.CharField(max_length=15, unique=True)
    annee = models.IntegerField()
    en_reparation = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.immatriculation})"