from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class UserModelManagerTest(TestCase):

    def test_create_user(self):
        UserModel = get_user_model()
        email_address = "first_user@aestation.ca"
        password = 'password'
        user = UserModel.objects.create_user(email=email_address, password=password)
        self.assertEqual(user.email, email_address)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            print("#Success,user.username is none.")
        
        with self.assertRaises(TypeError):
            UserModel.objects.create_user()

    def test_create_superuser(self):
        UserModel = get_user_model()
        email_address = "admin@admin.com"
        password = 'password'
        user = UserModel.objects.create_superuser(email=email_address, password=password)
        self.assertEqual(user.email, email_address)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        UserModel.objects.create_superuser(email=email_address, password=password, is_superuser=False)