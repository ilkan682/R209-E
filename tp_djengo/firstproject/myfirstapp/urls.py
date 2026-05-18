from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path("ajout/", views.ajout, name='ajout'),
    path('traitement/', views.traitement, name='traitement'), # Ajout du name
    path('affiche/<int:id>/', views.read, name='affiche'),
    path('update/<int:id>/', views.traitementupdate, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]