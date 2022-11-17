from django.core import mail
from django.test import TestCase
from subscriptions.forms import SubscriptionForm
from subscriptions.models import Subscription
# from django import unittest


class TestSubscribeGet(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """Get /inscricao/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use subscription/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Html must contain input tag"""
        tags = (
            ('<form', 1),
            ('<input', 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Kelver Alves', cpf='12345678901',
                    email='kelverwt@gmail.com', phone='84996068403')
        self.response = self.client.post('/inscricao/', data)

    def test_post(self):
        """Valid POST should redirect to /inscricao/1/"""
        #self.assertEqual(302, self.response.status_code)
        self.assertRedirects(self.response, '/inscricao/1/')

    def test_subscription_send_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/', {})

    def test_post(self):
        """Invalid POST should not redirect /inscricao/"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Render teplate corret"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_erros(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())

# @unittest.skip('To be removed')
# class SubscribeSuccessMessage(TestCase):
#     def test_message(self):
#         data = dict(name='Kelver Alves', cpf='12345678901',
#                     email='kelverwt@gmail.com', phone='84996068403')
#         response = self.client.post('/inscricao/', data, follow=True)
#         self.assertContains(response, 'Inscrição realizada com sucesso!')


