from django.shortcuts import render, get_object_or_404
from .models import Livres

def index(request):
    context = {"livres": Livres.objects.all()}
    return render(request, "logisticMediatheque/index.html", context)

def livreDetail(request, livre_id):
    context = {"livre": get_object_or_404( Livres, pk = livre_id )}
    return render(request, "logisticMediatheque/livreDetail.html", context)