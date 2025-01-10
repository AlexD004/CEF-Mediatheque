from django.shortcuts import render, get_object_or_404
from logisticMediatheque.models import Medias, Membres
from logisticMediatheque.forms import addMembreForm
import logging

logging.basicConfig(
    filename="logging.log",
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y%H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

""" READ methods """

def listMembres(request):
    return render(request, "logisticMediatheque/lists/listMembres.html", {"membres": Membres.objects.all()})

def membreDetail(request, membre_id):
    mediaLoans = Medias.objects.all().filter(borrower = membre_id)
    return render(
        request,
        "logisticMediatheque/itemDetails/membreDetails.html",
        { 
            "membre": get_object_or_404( Membres, pk = membre_id ),
            "mediaLoans": mediaLoans
        }
    )

""" DELETE methods """

def removeMembre(request, item_id):
    membre = Membres.objects.get( pk = item_id )
    membre.delete()
    membres = Membres.objects.all()

    logger.info("Suppression Membre par " + request.user.username + " | Nom du membre : " + membre.lastname + " " + membre.firstname )

    return render(request, 'logisticMediatheque/lists/listMembres.html', {'membres': membres})

""" CREATE methods """

def addMembre(request):
    action_type = 'Ajout'

    if request.method == 'POST':
            form = addMembreForm(request.POST)

            if form.is_valid():
                form.save()
                membres = Membres.objects.all()

                logger.info("Ajout Membre par " + request.user.username + " | Nom du membre : " + request.POST.get('lastname') + " " + request.POST.get('firstname'))

                return render(request, 'logisticMediatheque/lists/listMembres.html',{'membres': membres})
    else:
        form = addMembreForm()
        return render(request, 'logisticMediatheque/forms/addMembreForm.html',{'form': form, 'actionType': action_type})

""" UPDATE methods """

def updateMembre(request, item_id):
    action_type = 'Modification'
    jeu = Membres.objects.get( pk = item_id )

    if request.method == 'POST':
            form = addMembreForm(request.POST, instance=jeu)

            if form.is_valid():
                form.save()
                membres = Membres.objects.all()

                logger.info("MaJ Membre par " + request.user.username + " | Nom du membre : " + request.POST.get('lastname') + " " + request.POST.get('firstname'))

                return render(request, 'logisticMediatheque/lists/listMembres.html',{'membres': membres})
    else:
        form = addMembreForm(instance=jeu)
        return render(request, 'logisticMediatheque/forms/addMembreForm.html',{'form': form, 'actionType': action_type})