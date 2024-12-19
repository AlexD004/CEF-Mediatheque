from django import forms
from .models import Livres, CDs, DVDs, Jeux

class addLivreForm(forms.ModelForm):
    class Meta:
        model = Livres
        fields = ['title','mediaType','issue','numPages']
        labels = {'title':'Titre','mediaType':'Type de média','issue':'Date de sortie','numPages':'Nombre de pages'} 


class addCDForm(forms.ModelForm):
    class Meta:
        model = CDs
        fields = ['title','mediaType','issue','numPist']
        labels = {'title':'Titre','mediaType':'Type de média','issue':'Date de sortie','numPist':'Nombre de morceaux'} 


class addDVDForm(forms.ModelForm):
    class Meta:
        model = DVDs
        fields = ['title','mediaType','issue','filmDuration']
        labels = {'title':'Titre','mediaType':'Type de média','issue':'Date de sortie','filmDuration':'Durée'} 
        

class addJeuxForm(forms.ModelForm):
    class Meta:
        model = Jeux
        fields = ['gameTitle','issue','numPlayer','gameDuration']
        labels = {'title':'Titre','issue':'Date de sortie','numPlayer':'Nombre de joueur','gameDuration':'Temps de jeu'} 