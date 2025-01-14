from django.test import TestCase
from logisticMediatheque.models import Membres

class Test_Create_Membre(TestCase):
    def setUp(self):
        self.membre = Membres.objects.create(
            firstname = 'John',
            lastname = 'Doe',
            email = 'jdoe@gmail.com',
        )

    def test_create_membre(self):
        self.assertEqual(self.membre.firstname, 'John')
        self.assertEqual(self.membre.lastname, 'Doe')
        self.assertEqual(self.membre.email, 'jdoe@gmail.com')