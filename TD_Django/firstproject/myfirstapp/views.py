from django.shortcuts import render

#create your views here.
def index(request):
    return render(request, 'myfirstapp/index.html')
def formulaire(requests):
    return render(requests, "myfirstapp/formulaire.html")
