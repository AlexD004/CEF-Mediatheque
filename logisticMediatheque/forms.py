from django import forms
from .models import Livres, CDs, DVDs, Jeux, Membres, Author, Editor, Label, GroupOrSinger, Director, GameEditor, Medias

class addLivreForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), to_field_name="name", label = "Auteur")
    editor = forms.ModelChoiceField(queryset=Editor.objects.all(), label = "Éditeur")
    class Meta:
        model = Livres
        fields = ['title','author','editor','issue','numPages']
        labels = {'title':'Titre','issue':'Date de sortie','numPages':'Nombre de pages'} 

class addCDForm(forms.ModelForm):
    label = forms.ModelChoiceField(queryset=Label.objects.all(), label = "Label")
    artist = forms.ModelChoiceField(queryset=GroupOrSinger.objects.all(), label = "Artiste")
    class Meta:
        model = CDs
        fields = ['title','label','artist','issue','numPist']
        labels = {'title':'Titre','issue':'Date de sortie','numPist':'Nombre de morceaux'} 


class addDVDForm(forms.ModelForm):
    director = forms.ModelChoiceField(queryset=Director.objects.all(), label = "Réalisateur")
    class Meta:
        model = DVDs
        fields = ['title','director','issue','filmDuration']
        labels = {'title':'Titre','issue':'Date de sortie','filmDuration':'Durée'} 
        

class addJeuxForm(forms.ModelForm):
    gameEditor = forms.ModelChoiceField(queryset=GameEditor.objects.all(), label = "Éditeur")
    class Meta:
        model = Jeux
        fields = ['gameTitle','gameEditor','issue','numPlayer','gameDuration']
        labels = {'title':'Titre','issue':'Date de sortie','numPlayer':'Nombre de joueur','gameDuration':'Temps de jeu'} 

class addMembreForm(forms.ModelForm):
    class Meta:
        model = Membres
        fields = ['firstname','lastname','email']
        labels = {'firstname':'Prénom','lastname':'Nom','email':'Adresse e-mail'} 

class addLoanForm(forms.Form): 
    membre = forms.ModelChoiceField(queryset=Membres.objects.all().filter(numLoan__lt=3, canLoan=True), label = "Membre emprunteur")
    media = forms.ModelChoiceField(queryset=Medias.objects.all().filter(dateLoan__isnull=True), label = "Média")