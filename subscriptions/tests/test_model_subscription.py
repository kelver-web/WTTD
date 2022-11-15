from django.test import TestCase
from subscriptions.models import Subscription
from datetime import datetime


class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name = 'Kelve Alves', 
            cpf = '12345678901', 
            email = 'kelverwt@gmail.com', 
            phone = '84990909876',
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)


