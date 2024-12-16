from django.db import models

"""
    primary_key
    unique
    default
    null
    blank

    CharField
    IntegerField
    DateField
    DateTimeField
    FloatField
    EmailField
    BooleanField

    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING)
"""

class Medias (models.Model):
    title = models.CharField(max_length = 100, unique = True)
    issue = models.DateField()
    dateLoan = models.DateField(null = True, blank = True)

class Livres (Medias):
    bookEditor = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    numPages = models.IntegerField()

class CDs (Medias):
    musicEditor = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)
    numPist = models.IntegerField()

class DVDs (Medias):
    studio = models.CharField(max_length = 100)
    filmDuration = models.IntegerField()
    director = models.CharField(max_length = 100)

class Jeux (models.Model):
    gameTitle = models.CharField(max_length = 100, unique = True)
    gameEditor = models.CharField(max_length = 100)
    numPlayer = models.IntegerField()
    gameDuration = models.IntegerField()
    issue = models.DateField()