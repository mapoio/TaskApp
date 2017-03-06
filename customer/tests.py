from django.test import TestCase
# from customer.models import Customer
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
#
#
# class UserLogout(APITestCase):
#     def setUp(self):
#         test1 = User.objects.create(username='123', password='123456')
#         Snippets.objects.create(code='13245', owner=test1)
#         Snippets.objects.create(code='1324', owner=test1)
#
#     def test_account_logout(self):
#         response = self.client.get('/')
#         self.assertEqual(403, response.status_code)

class CustomerTest(APIClient):
    def setUp(self):
        self.kok = 403

    def test_one(self):
        self.assertEqual(403, self.kok)
