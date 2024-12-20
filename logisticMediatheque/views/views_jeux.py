from django.shortcuts import render, get_object_or_404
from logisticMediatheque.models import Medias, Jeux
from logisticMediatheque.forms import addJeuxForm

""" READ methods """

def listJeux(request):
    return render(request, "logisticMediatheque/lists/listJeux.html", {"items": Jeux.objects.all()})

def jeuDetail(request, jeu_id):
    return render(request, "logisticMediatheque/itemDetails/jeuDetails.html", { "jeu": get_object_or_404( Jeux, pk = jeu_id )})

""" DELETE methods """

def removeJeu(request, item_id):
    jeu = Jeux.objects.get( pk = item_id )
    jeu.delete()
    medias = Medias.objects.all()
    return render(request, 'logisticMediatheque/lists/listMedias.html', {'items': medias})

""" CREATE methods """

def addJeu(request):
    action_type = 'Ajout'

    if request.method == 'POST':
            form = addJeuxForm(request.POST)

            if form.is_valid():
                form.save()
                medias = Medias.objects.all()
                return render(request, 'logisticMediatheque/lists/listMedias.html',{'items': medias})
    else:
        form = addJeuxForm()
        return render(request, 'logisticMediatheque/forms/addJeuxForm.html',{'form': form, 'actionType': action_type})

""" UPDATE methods """

def updateJeu(request, item_id):
    action_type = 'Modification'
    jeu = Jeux.objects.get( pk = item_id )

    if request.method == 'POST':
            form = addJeuxForm(request.POST, instance=jeu)

            if form.is_valid():
                form.save()
                medias = Medias.objects.all()
                return render(request, 'logisticMediatheque/lists/listMedias.html',{'items': medias})
    else:
        form = addJeuxForm(instance=jeu)
        return render(request, 'logisticMediatheque/forms/addJeuxForm.html',{'form': form, 'actionType': action_type})