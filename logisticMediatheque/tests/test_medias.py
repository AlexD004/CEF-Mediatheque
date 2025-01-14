from django.test import TestCase
from logisticMediatheque.models import Medias, Livres, CDs, DVDs
import datetime

class Test_Create_Medias(TestCase):
    def setUp(self):
        self.media = Medias.objects.create(
            title = 'MediaName',
            issue = datetime.datetime(2025,9,23).strftime('%Y-%m-%d')
        )

    def test_create_media(self):
        self.assertEqual(self.media.title, 'MediaName')
        self.assertEqual(self.media.issue, '2025-09-23') 


class Test_Create_Livres(TestCase):
    def setUp(self):
        self.livre = Livres.objects.create(
            title = 'LivreName',
            issue = datetime.datetime(2025,9,23).strftime('%Y-%m-%d'),
            numPages = 100 
        )

    def test_create_livre(self):
        self.assertEqual(self.livre.title, 'LivreName')
        self.assertEqual(self.livre.issue, '2025-09-23') 
        self.assertEqual(self.livre.numPages, 100) 


class Test_Create_CDs(TestCase):
    def setUp(self):
        self.cd = CDs.objects.create(
            title = 'LivreName',
            issue = datetime.datetime(2025,9,23).strftime('%Y-%m-%d'),
            numPist = 12 
        )

    def test_create_cd(self):
        self.assertEqual(self.cd.title, 'LivreName')
        self.assertEqual(self.cd.issue, '2025-09-23') 
        self.assertEqual(self.cd.numPist, 12) 


class Test_Create_DVDs(TestCase):
    def setUp(self):
        self.dvd = DVDs.objects.create(
            title = 'LivreName',
            issue = datetime.datetime(2025,9,23).strftime('%Y-%m-%d'),
            filmDuration = 120
        )

    def test_create_dvd(self):
        self.assertEqual(self.dvd.title, 'LivreName')
        self.assertEqual(self.dvd.issue, '2025-09-23') 
        self.assertEqual(self.dvd.filmDuration, 120) 