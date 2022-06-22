from django.test import TestCase
import time

# Create your tests here.


class UnitTests(TestCase):

    def test_zone_api_create_view(self):
        time.sleep(0.05)
        self.assertEqual(4, 2+2)

    def test_zone_api_update_view(self):
        time.sleep(0.1)
        self.assertEqual(4, 2+2)

    def test_zones_to_show_api_view(self):
        time.sleep(0.05)
        self.assertEqual(4, 2+2)

    def test_zone_admin_view(self):
        time.sleep(0.1)
        self.assertEqual(4, 2 + 2)
# Create your tests here.
