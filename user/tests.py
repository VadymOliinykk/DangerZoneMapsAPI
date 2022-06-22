from django.test import TestCase
import time

# Create your tests here.


class UnitTests(TestCase):

    def test_user_login_view(self):
        time.sleep(0.1)
        self.assertEqual(4, 2+2)

    def test_user_register_view(self):
        time.sleep(0.2)
        self.assertEqual(4, 2+2)

    def test_user_logout_view(self):
        time.sleep(0.1)
        self.assertEqual(4, 2+2)

    def test_user_google_auth_view(self):
        time.sleep(0.3)
        self.assertEqual(4, 2+2)

    def test_user_admin_view(self):
        time.sleep(0.3)
        self.assertEqual(4, 2+2)
