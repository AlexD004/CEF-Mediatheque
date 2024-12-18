from django.shortcuts import render, get_object_or_404
from .models import Medias, Livres, CDs, DVDs, Jeux

""" Connected home page """

def dashboard(request):
    context = {"items": Medias.objects.all() }
    return render(request, "logisticMediatheque/lists.html", context)

""" Lists by item type """

def listMedias(request, sortBy):
    if sortBy == 'livre':
        context = {
            "items": Livres.objects.all(),
            "type":"medias"
        }
    elif sortBy == 'cd':
        context = {
            "items": CDs.objects.all(),
            "type":"medias"
        }
    elif sortBy == 'dvd':
        context = {
            "items": DVDs.objects.all(),
            "type":"medias"
        }
    elif sortBy == 'jeu':
        context = {
            "items": Jeux.objects.all(),
            "type":"jeux"
        }
    return render(request, "logisticMediatheque/lists.html", context)

""" Items details page """

def mediaDetail(request, item_type, item_id ):

    if item_type == 'LIVRE':
        context = { "item": get_object_or_404( Livres, pk = item_id ) }
    elif item_type == 'CD':
        context = { "item": get_object_or_404( CDs, pk = item_id ) }
    elif item_type == 'DVD':
        context = { "item": get_object_or_404( DVDs, pk = item_id ) }
    else:
        context = { "item": get_object_or_404( Medias, pk = item_id ) }

    return render(request, "logisticMediatheque/itemDetails/mediaDetails.html", context)

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