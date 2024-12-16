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
    dateLoan = models.DateField(auto_now = True)

class Livres (Medias):
    bookEditor = models.CharField(max_length = 100, unique = True)
    author = models.CharField(max_length = 100, unique = True)
    numPages = models.IntegerField()

class CDs (Medias):
    musicEditor = models.CharField(max_length = 100, unique = True)
    artist = models.CharField(max_length = 100, unique = True)
    numPist = models.IntegerField()

class DVDs (Medias):
    studio = models.CharField(max_length = 100, unique = True)
    filmDuration = models.IntegerField()
    director = models.CharField(max_length = 100, unique = True)

class Jeux (models.Model):
    gameTitle = models.CharField(max_length = 100, unique = True)
    gameEditor = models.CharField(max_length = 100, unique = True)
    numPlayer = models.IntegerField()
    gameDuration = models.IntegerField()
    issue = models.DateField()