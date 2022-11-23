from django.test import TestCase
from subscriptions.models import Subscription
from datetime import datetime


class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name = 'Kelver Alves', 
            cpf = '12345678901', 
            email = 'kelverwt@gmail.com', 
            phone = '84990909876',
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Kelver Alves', str(self.obj))

    def test_paid_default_to_False(self):
        """By default paid must be False"""
        self.assertEqual(False, self.obj.paid)

