from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class DashboardTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'password')
        self.staff_user = User.objects.create_user('staff', 'staff@example.com', 'password', is_staff=True)
        self.regular_user = User.objects.create_user('user', 'user@example.com', 'password')
        
    def test_login_redirect(self):
        response = self.client.get(reverse('dashboard:home'))
        self.assertEqual(response.status_code, 302)
        
    def test_admin_access(self):
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('dashboard:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/index.html')
        
    def test_staff_access(self):
        self.client.login(username='staff', password='password')
        response = self.client.get(reverse('dashboard:home'))
        self.assertEqual(response.status_code, 200)

    def test_regular_user_denied(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('dashboard:home'))
        # Expect 403 because UserPassesTestMixin usually returns 403 on failure
        # But UserPassesTestMixin defaults to 403 if raise_exception is True, or redirect to login.
        # Let's see how I implemented AdminRequiredMixin.
        self.assertEqual(response.status_code, 403)

    def test_user_list_htmx(self):
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('dashboard:users'), HTTP_HX_REQUEST='true')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/partials/user_list.html')
