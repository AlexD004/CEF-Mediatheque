from django.shortcuts import render, get_object_or_404
from .models import Medias, Livres, CDs, DVDs, Jeux

""" Connected home page """

def dashboard(request):
    context = {
        "livres": Livres.objects.all(),
        "cds": CDs.objects.all(),
        "dvds": DVDs.objects.all(),
        "jeux": Jeux.objects.all()
    }
    return render(request, "logisticMediatheque/lists.html", context)

""" Lists by item type """

def listLivres(request):
    context = {"medias": Livres.objects.all()}
    return render(request, "logisticMediatheque/lists.html", context)

def listCDs(request):
    context = {"medias": CDs.objects.all()}
    return render(request, "logisticMediatheque/lists.html", context)

def listDVDs(request):
    context = {"medias": DVDs.objects.all()}
    return render(request, "logisticMediatheque/lists.html", context)

def listJeux(request):
    context = {"jeux": Jeux.objects.all()}
    return render(request, "logisticMediatheque/lists.html", context)

""" Items details page """

def livreDetail(request, livre_id):
    context = { "livre": get_object_or_404( Livres, pk = livre_id )}
    return render(request, "logisticMediatheque/itemDetails/livreDetails.html", context)

def cdDetail(request, cd_id):
    context = { "cd": get_object_or_404( CDs, pk = cd_id )}
    return render(request, "logisticMediatheque/itemDetails/cdDetails.html", context)

def dvdDetail(request, dvd_id):
    context = { "dvd": get_object_or_404( DVDs, pk = dvd_id )}
    return render(request, "logisticMediatheque/itemDetails/dvdDetails.html", context)

def jeuDetail(request, jeu_id):
    context = { "jeu": get_object_or_404( Jeux, pk = jeu_id )}
    return render(request, "logisticMediatheque/itemDetails/jeuDetails.html", context)

""" Other pages """

def listMembres(request):
    context = {"membres": "Liste des membres"}
    return render(request, "logisticMediatheque/listMembers.html", context)

def historique(request):
    context = {"historique": "Liste des logs"}
    return render(request, "logisticMediatheque/historique.html", context)