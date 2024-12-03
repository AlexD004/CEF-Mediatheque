from django.shortcuts import render
from mediathequePython.models.media import Media

def listemedias(request):
    medias = Media.objects.all()
    return render(request, 'lists.html',
                  {'medias': medias})