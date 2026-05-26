from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Recette, Ingredient

admin.site.register(Recette)
admin.site.register(Ingredient)