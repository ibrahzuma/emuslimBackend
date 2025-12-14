from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class AuthTests(APITestCase):
    def test_register_user(self):
        url = reverse('register')
        data = {'username': 'testuser', 'password': 'testpassword123', 'email': 'test@example.com'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_login_user(self):
        user = User.objects.create_user(username='testuser', password='testpassword123')
        url = reverse('token_obtain_pair')
        data = {'username': 'testuser', 'password': 'testpassword123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

class UserListTests(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', password='password')
        self.user = User.objects.create_user(username='user', password='password')
        self.url = reverse('user_list')

    def test_list_users_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_list_users_forbidden(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
