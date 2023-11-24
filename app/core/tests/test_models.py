"""
Test for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test models."""

    def test_create_uuser_with_email_successul(self):
        """ Successful test user created """
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
