from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.

class UserLogin(TestCase):

    def setUp(self):
        test_user = User.objects.create(username='test', password="123test")

    def test_login(self):
        response = self.client.post(reverse('login'),
                                    {'username': 'test1',
                                     'password': '123test'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.post(reverse('register'),
                                    {'username': 'test',
                                     'email': 'test@hotmail.com',
                                     'password1': '123test',
                                     'password2': '123test'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.login(username='test', password='123test')
        self.client.logout()
        self.assertRaises(
            KeyError, lambda: self.client.session['_auth_user_id'])
