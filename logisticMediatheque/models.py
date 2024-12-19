from django.db import models

""" Class for Members """

class Membres (models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    canLoan = models.BooleanField(default=True)
    numLoan = models.IntegerField(default=0)


""" Class for Medias Details and Informations """

class Author (models.Model):
    name = models.CharField(max_length = 100, default = "Inconnu")

class Editor (models.Model):
    name = models.CharField(max_length = 100, default = "Inconnu")

class Label (models.Model):
    name = models.CharField(max_length = 100, default = "Inconnu")

class GroupOrSinger (models.Model):
    name = models.CharField(max_length = 100, default = "Inconnu")

class Director (models.Model):
    name = models.CharField(max_length = 100, default = "Inconnu")

class GameEditor (models.Model):
    name = models.CharField(max_length = 100, default = "Inconnu")

""" Class for Medias """

class Medias (models.Model):
    title = models.CharField(max_length = 100, unique = True)
    issue = models.DateField()
    borrower = models.ForeignKey(Membres, on_delete= models.DO_NOTHING, null=True)
    dateLoan = models.DateField(null = True, blank = True)
    MEDIATYPES = [
        ("livre", "Livre"),
        ("cd", "CD"),
        ("dvd", "DVD")
    ]
    mediaType = models.CharField(choices=MEDIATYPES, max_length=5, default="livre")

class Livres (Medias):
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING, null = True)
    editor = models.ForeignKey(Editor, on_delete = models.DO_NOTHING, null = True)
    numPages = models.IntegerField()

class CDs (Medias):
    label = models.ForeignKey(Label, on_delete = models.DO_NOTHING, null = True)
    artist = models.ForeignKey(GroupOrSinger, on_delete = models.DO_NOTHING, null = True)
    numPist = models.IntegerField()

class DVDs (Medias):
    director = models.ForeignKey(Director, on_delete = models.DO_NOTHING, null = True)
    filmDuration = models.IntegerField()

""" Class for Games """

class Jeux (models.Model):
    gameTitle = models.CharField(max_length = 100, unique = True)
    gameEditor = models.ForeignKey(GameEditor, on_delete = models.DO_NOTHING, null = True)
    numPlayer = models.CharField(max_length = 10)
    gameDuration = models.IntegerField()
    issue = models.DateField()