from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import CustomUser

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
            user_type='buyer'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('testpassword'))
        self.assertEqual(self.user.user_type, 'buyer')
