from django.shortcuts import render

def historique(request):
    return render(request, "logisticMediatheque/historique.html", {"historique": "Liste des logs"})