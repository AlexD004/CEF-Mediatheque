from django.test import TestCase
from logisticMediatheque.models import Jeux
import datetime

class Test_Create_Jeux(TestCase):
    def setUp(self):
        self.jeux = Jeux.objects.create(
            gameTitle = 'JeuName',
            issue = datetime.datetime(2025,9,23).strftime('%Y-%m-%d'),
            numPlayer = 2,
            gameDuration = 30
        )

    def test_create_jeux(self):
        self.assertEqual(self.jeux.gameTitle, 'JeuName')
        self.assertEqual(self.jeux.issue, '2025-09-23') 
        self.assertEqual(self.jeux.numPlayer, 2) 
        self.assertEqual(self.jeux.gameDuration, 30) 