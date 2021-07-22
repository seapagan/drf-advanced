"""Test for admin site."""
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Class to test the Admin Site."""

    def setUp(self):
        """Common setup function for all tests in this class."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@gnramsay.com", password="password123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@gnramsay.com",
            password="password123",
            name="Test user full name",
        )

    def test_users_listed(self):
        """Test that users are listed on user page."""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works."""
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works."""
        url = reverse("admin:core_user_add")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
