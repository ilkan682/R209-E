from django.urls import path
from . import views

urlpatterns = [

    path('index/', views.index, name='index'),

    path('recette/list/', views.recette_list, name='recette_list'),

    path('recette/add/', views.recette_form, name='recette_add'),

    path('ingredient/add/', views.ingredient_form, name='ingredient_form'),

    path('recette/<int:pk>/', views.recette_detail, name='recette_detail'),

    path('recette/<int:pk>/delete/', views.recette_confirm_delete, name='recette_delete'),
]