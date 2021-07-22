"""Test Models for the Core app."""
from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    """Test class for the Models."""

    def test_create_user_with_email_successfully(self):
        """Test creating a new use with an email is successful."""
        email = "test@gnramsay.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that the email for a new user is normalized."""
        email = "Test@GNRAMSAY.COM"
        user = get_user_model().objects.create_user(email, "test123")

        name, domain = email.split("@")
        self.assertEqual(user.email, f"{name}@{domain.lower()}")

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """Test creating a new superuser."""
        user = get_user_model().objects.create_superuser(
            "test@gnramsay.com", "password123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
