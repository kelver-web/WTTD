from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Kelver Alves', cpf='12345678901',
                    email='kelverwt@gmail.com', phone='84996068403')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'kelverwt@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['kelverwt@gmail.com', 'kelverwt@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Kelver Alves', '12345678901', 'kelverwt@gmail.com', '84996068403']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)


