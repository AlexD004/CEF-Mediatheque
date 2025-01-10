from django.shortcuts import render, get_object_or_404
from logisticMediatheque.models import Medias, Livres, CDs, DVDs
from logisticMediatheque.forms import addLivreForm, addCDForm, addDVDForm
import logging

logging.basicConfig(
    filename="logging.log",
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y%H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


""" READ methods """

def listMedias(request):
    return render(request, "logisticMediatheque/lists/listMedias.html", {"items": Medias.objects.all() })

def listMediasByType(request, item_type):
    return render(request, "logisticMediatheque/lists/listMedias.html", {
        "items": Medias.objects.all().filter( mediaType = item_type),
        "type": item_type
    })

def mediaDetail(request, item_type, item_id ):
    if item_type == 'livre':
        context = { "item": get_object_or_404( Livres, pk = item_id ) }
    elif item_type == 'cd':
        context = { "item": get_object_or_404( CDs, pk = item_id ) }
    elif item_type == 'dvd':
        context = { "item": get_object_or_404( DVDs, pk = item_id ) }
    return render(request, "logisticMediatheque/itemDetails/mediaDetails.html", context)

""" DELETE methods """

def removeMedia(request, item_id):
    media = Medias.objects.get( pk = item_id )
    media.delete()
    medias = Medias.objects.all()

    logger.info("Suppression Livre par " + request.user.username + " | Titre du livre : " + media.title )

    return render(request, 'logisticMediatheque/lists/listMedias.html', {'items': medias})

""" CREATE methods """

def addMedia(request, media_type):
    action_type = 'Ajout'
    templateForm = 'logisticMediatheque/forms/addMediaForm.html'
    templateRedirect = 'logisticMediatheque/lists/listMedias.html'

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

                logger.info("Ajout Livre par " + request.user.username + " | Titre du livre : " + newLivre.title )

                return render(request, templateRedirect,{'items': medias})
        else:
            form = addLivreForm()
            return render(request, templateForm, {'form': form, 'mediaType': media_type, 'actionType': action_type})
        

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

                logger.info("Ajout CD par " + request.user.username + " | Titre du CD : " + newCD.title )

                return render(request, templateRedirect,{'items': medias})
        else:
            form = addCDForm()
            return render(request, templateForm,{'form': form, 'mediaType': media_type, 'actionType': action_type})


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

                logger.info("Ajout DVD par " + request.user.username + " | Titre du DVD : " + newDVD.title )

                return render(request, templateRedirect,{'items': medias})
        else:
            form = addDVDForm()
            return render(request, templateForm,{'form': form, 'mediaType': media_type, 'actionType': action_type})
        
""" UPDATE methods """
       
def updateMedia(request, media_type, item_id):
    action_type = 'Modification'
    templateForm = 'logisticMediatheque/forms/addMediaForm.html'
    templateRedirect = 'logisticMediatheque/lists/listMedias.html'
    media = Medias.objects.get( pk = item_id )

    if media_type == 'livre':
        if request.method == 'POST':
            form = addLivreForm(request.POST, instance=media)

            if form.is_valid():
                form.save()
                medias = Medias.objects.all()

                logger.info("MaJ Livre par " + request.user.username + " | Titre du Livre : " + media.title )

                return render(request, templateRedirect,{'items': medias})
        else:
            form = addLivreForm(instance=media)
            return render(request, templateForm,{'form': form, 'mediaType': media_type, 'actionType': action_type})
        

    if media_type == 'cd':
        if request.method == 'POST':
            form = addCDForm(request.POST, instance=media)

            if form.is_valid():
                form.save()
                medias = Medias.objects.all()

                logger.info("MaJ CD par " + request.user.username + " | Titre du CD : " + media.title )

                return render(request, templateRedirect,{'items': medias})
        else:
            form = addCDForm(instance=media)
            return render(request, templateForm,{'form': form, 'mediaType': media_type, 'actionType': action_type})


    if media_type == 'dvd':
        if request.method == 'POST':
            form = addDVDForm(request.POST, instance=media)

            if form.is_valid():
                form.save()
                medias = Medias.objects.all()

                logger.info("MaJ DVD par " + request.user.username + " | Titre du DVD : " + media.title )

                return render(request, templateRedirect,{'items': medias})
        else:
            form = addDVDForm(instance=media)
            return render(request, templateForm,{'form': form, 'mediaType': media_type, 'actionType': action_type})