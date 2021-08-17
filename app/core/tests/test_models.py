from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@example.com'
        password = 'Password1'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """Test the email for a new user is normalised"""
        email = 'test@EXAMPLE.COM'
        user = get_user_model().objects.create_user(email, 'Password1')

        self.assertEqual(user.email, 'test@example.com')

    def test_new_user_invalid_email(self):
        """Test creating new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Password1')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'superuser@example.com',
            'Password1'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
