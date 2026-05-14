from . import views
from django.urls import path
urlpatterns = [
    path('', views.index),
    path("ajout/", views.ajout),
    path('traitement', views.traitement),
    path('affiche/<int:id>/',views.read),
    path('update/<int:id>/',views.traitementupdate),
    path('delete/<int:id>/', views.delete),
]
