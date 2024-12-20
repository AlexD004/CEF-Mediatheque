from django.shortcuts import render, get_object_or_404
from .models import Medias, Livres, CDs, DVDs, Jeux, Membres
from .forms import addLivreForm, addCDForm, addDVDForm, addJeuxForm, addMembreForm, addLoanForm
import datetime

""" 
READ
METHODS 
"""

""" Home page """

def dashboard(request):
    return render(request, "logisticMediatheque/listMedias.html", {"items": Medias.objects.all() })

""" Lists by item type """

def listMedias(request, item_type):
    return render(request, "logisticMediatheque/listMedias.html", {
        "items": Medias.objects.all().filter( mediaType = item_type),
        "type": item_type
    })

def listJeux(request):
    return render(request, "logisticMediatheque/listJeux.html", {"items": Jeux.objects.all()})

""" Items details page """

def mediaDetail(request, item_type, item_id ):
    if item_type == 'livre':
        context = { "item": get_object_or_404( Livres, pk = item_id ) }
    elif item_type == 'cd':
        context = { "item": get_object_or_404( CDs, pk = item_id ) }
    elif item_type == 'dvd':
        context = { "item": get_object_or_404( DVDs, pk = item_id ) }
    return render(request, "logisticMediatheque/itemDetails/mediaDetails.html", context)

def jeuDetail(request, jeu_id):
    return render(request, "logisticMediatheque/itemDetails/jeuDetails.html", { "jeu": get_object_or_404( Jeux, pk = jeu_id )})

""" Other pages """

def listMembres(request):
    return render(request, "logisticMediatheque/listMembres.html", {"membres": Membres.objects.all()})

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

def historique(request):
    return render(request, "logisticMediatheque/historique.html", {"historique": "Liste des logs"})

""" 
DELETE
METHODS
"""

def removeMedia(request, item_id):
    media = Medias.objects.get( pk = item_id )
    media.delete()
    medias = Medias.objects.all()
    return render(request, 'logisticMediatheque/listMedias.html', {'items': medias})

def removeJeu(request, item_id):
    jeu = Jeux.objects.get( pk = item_id )
    jeu.delete()
    medias = Medias.objects.all()
    return render(request, 'logisticMediatheque/listMedias.html', {'items': medias})

def removeMembre(request, item_id):
    membre = Membres.objects.get( pk = item_id )
    membre.delete()
    membres = Membres.objects.all()
    return render(request, 'logisticMediatheque/listMembres.html', {'membres': membres})

"""
ADD
METHODS
"""

def addMedia(request, media_type):
    action_type = 'Ajout'

    if media_type == 'livre':
        if request.method == 'POST':
            form = addLivreForm(request.POST)

            if form.is_valid():
                newLivre = Livres()
                newLivre.title = form.cleaned_data['title']
                newLivre.mediaType = media_type
                newLivre.author = form.cleaned_data['author']
                newLivre.editor = form.cleaned_data['editor']
                newLivre.issue = form.cleaned_data['issue']
                newLivre.numPages = form.cleaned_data['numPages']
                newLivre.save()
                medias = Medias.objects.all()
                return render(request, 'logisticMediatheque/listMedias.html',{'items': medias})
        else:
            form = addLivreForm()
            return render(request, 'logisticMediatheque/forms/addMediaForm.html',{'form': form, 'mediaType': media_type, 'actionType': action_type})
        

    if media_type == 'cd':
        if request.method == 'POST':
            form = addCDForm(request.POST)

            if form.is_valid():
                newCD = CDs()
                newCD.title = form.cleaned_data['title']
                newCD.mediaType = media_type
                newCD.label = form.cleaned_data['label']
                newCD.artist = form.cleaned_data['artist']
                newCD.issue = form.cleaned_data['issue']
                newCD.numPist = form.cleaned_data['numPist']
                newCD.save()
                medias = Medias.objects.all()
                return render(request, 'logisticMediatheque/listMedias.html',{'items': medias})
        else:
            form = addCDForm()
            return render(request, 'logisticMediatheque/forms/addMediaForm.html',{'form': form, 'mediaType': media_type, 'actionType': action_type})


    if media_type == 'dvd':
        if request.method == 'POST':
            form = addDVDForm(request.POST)

            if form.is_valid():
                newDVD = DVDs()
                newDVD.title = form.cleaned_data['title']
                newDVD.mediaType = media_type
                newDVD.director = form.cleaned_data['director']
                newDVD.issue = form.cleaned_data['issue']
                newDVD.filmDuration = form.cleaned_data['filmDuration']
                newDVD.save()
                medias = Medias.objects.all()
                return render(request, 'logisticMediatheque/listMedias.html',{'items': medias})
        else:
            form = addDVDForm()
            return render(request, 'logisticMediatheque/forms/addMediaForm.html',{'form': form, 'mediaType': media_type, 'actionType': action_type})


def addJeu(request):
    action_type = 'Ajout'

    if request.method == 'POST':
            form = addJeuxForm(request.POST)

            if form.is_valid():
                form.save()
                medias = Medias.objects.all()
                return render(request, 'logisticMediatheque/listMedias.html',{'items': medias})
    else:
        form = addJeuxForm()
        return render(request, 'logisticMediatheque/forms/addJeuxForm.html',{'form': form, 'actionType': action_type})
    

def addMembre(request):
    action_type = 'Ajout'

    if request.method == 'POST':
            form = addMembreForm(request.POST)

            if form.is_valid():
                form.save()
                membres = Membres.objects.all()
                return render(request, 'logisticMediatheque/listMembres.html',{'membres': membres})
    else:
        form = addMembreForm()
        return render(request, 'logisticMediatheque/forms/addMembreForm.html',{'form': form, 'actionType': action_type})

"""
UPDATE
METHODS
"""

def updateMedia(request, media_type, item_id):
    action_type = 'Modification'
    media = Medias.objects.get( pk = item_id )

    if media_type == 'livre':
        if request.method == 'POST':
            form = addLivreForm(request.POST, instance=media)

            if form.is_valid():
                form.save()
                medias = Medias.objects.all()
                return render(request, 'logisticMediatheque/listMedias.html',{'items': medias})
        else:
            form = addLivreForm(instance=media)
            return render(request, 'logisticMediatheque/forms/addMediaForm.html',{'form': form, 'mediaType': media_type, 'actionType': action_type})
        

    if media_type == 'cd':
        if request.method == 'POST':
            form = addCDForm(request.POST, instance=media)

            if form.is_valid():
                form.save()
                medias = Medias.objects.all()
                return render(request, 'logisticMediatheque/listMedias.html',{'items': medias})
        else:
            form = addCDForm(instance=media)
            return render(request, 'logisticMediatheque/forms/addMediaForm.html',{'form': form, 'mediaType': media_type, 'actionType': action_type})


    if media_type == 'dvd':
        if request.method == 'POST':
            form = addDVDForm(request.POST, instance=media)

            if form.is_valid():
                form.save()
                medias = Medias.objects.all()
                return render(request, 'logisticMediatheque/listMedias.html',{'items': medias})
        else:
            form = addDVDForm(instance=media)
            return render(request, 'logisticMediatheque/forms/addMediaForm.html',{'form': form, 'mediaType': media_type, 'actionType': action_type})
        

def updateJeu(request, item_id):
    action_type = 'Modification'
    jeu = Jeux.objects.get( pk = item_id )

    if request.method == 'POST':
            form = addJeuxForm(request.POST, instance=jeu)

            if form.is_valid():
                form.save()
                medias = Medias.objects.all()
                return render(request, 'logisticMediatheque/listMedias.html',{'items': medias})
    else:
        form = addJeuxForm(instance=jeu)
        return render(request, 'logisticMediatheque/forms/addJeuxForm.html',{'form': form, 'actionType': action_type})
    

def updateMembre(request, item_id):
    action_type = 'Modification'
    jeu = Membres.objects.get( pk = item_id )

    if request.method == 'POST':
            form = addMembreForm(request.POST, instance=jeu)

            if form.is_valid():
                form.save()
                membres = Membres.objects.all()
                return render(request, 'logisticMediatheque/listMembres.html',{'membres': membres})
    else:
        form = addMembreForm(instance=jeu)
        return render(request, 'logisticMediatheque/forms/addMembreForm.html',{'form': form, 'actionType': action_type})
    

"""
METHODS
FOR LOAN
"""

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
    
def removeLoan(request, item_id, membre_id):  
    media = Medias.objects.get( pk = item_id )
    membre = Membres.objects.get( pk = membre_id )

    membre.numLoan -= 1
    media.dateLoan = None
    media.borrower = None

    membre.save()
    media.save()

    mediaLoans = Medias.objects.all().filter(borrower = membre_id)

    return render(
        request,
        "logisticMediatheque/itemDetails/membreDetails.html",
        { 
            "membre": get_object_or_404( Membres, pk = membre_id ),
            'mediaLoans': mediaLoans
        })