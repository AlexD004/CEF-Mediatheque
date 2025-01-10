from django.shortcuts import render, get_object_or_404
from logisticMediatheque.models import Medias, Membres
from logisticMediatheque.forms import addLoanForm
import datetime
import logging

logging.basicConfig(
    filename="logging.log",
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y%H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

""" CREATE methods """

def addLoan(request):
    if request.method == 'POST':
            form = addLoanForm(request.POST)

            if form.is_valid():
                membre = form.cleaned_data['membre']
                media = form.cleaned_data['media']

                membreLoaning = Membres.objects.get( pk = membre.id )
                mediaLoaned = Medias.objects.get( pk = media.id )

                membreLoaning.numLoan += 1 
                mediaLoaned.borrower = membre
                mediaLoaned.dateLoan = datetime.datetime.now()

                membreLoaning.save()
                mediaLoaned.save()

                mediaLoans = Medias.objects.all().filter(borrower = membre.id)

                logger.info("Ajout Emprunt " + request.user.username + " | Nom du membre : " + membre.lastname + " " + membre.firstname + " / Nom du médias : " + media.title )

                return render(
                    request,
                    "logisticMediatheque/itemDetails/membreDetails.html",
                    { 
                        "membre": get_object_or_404( Membres, pk = membre.id ),
                        'mediaLoans': mediaLoans
                    }
                )
    else:
        form = addLoanForm()
        return render(request, 'logisticMediatheque/forms/addLoanForm.html',{'form': form})

""" DELETE methods """

def removeLoan(request, item_id, membre_id):  
    media = Medias.objects.get( pk = item_id )
    membre = Membres.objects.get( pk = membre_id )

    membre.numLoan -= 1
    media.dateLoan = None
    media.borrower = None

    membre.save()
    media.save()

    mediaLoans = Medias.objects.all().filter(borrower = membre_id)

    logger.info("Suppression Emprunt " + request.user.username + " | Nom du membre : " + membre.lastname + " " + membre.firstname + " / Nom du médias : " + media.title )

    return render(
        request,
        "logisticMediatheque/itemDetails/membreDetails.html",
        { 
            "membre": get_object_or_404( Membres, pk = membre_id ),
            'mediaLoans': mediaLoans
        })