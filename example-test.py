# 这是一个tests.py的实例文件，保存下来，留用
# This is a tests.py for example

# from snippets.models import Snippets
# from rest_framework.test import APITestCase, APIClient
# from django.contrib.auth.models import User
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
#
#     def test_access_snippet_list(self):
#         response = self.client.get('/snippet/')
#         self.assertEqual(200, response.status_code)
#         self.assertEqual(2, response.data['count'])
#
#     def test_access_user(self):
#         response = self.client.get('/user/')
#         self.assertEqual(403, response.status_code)
#
#     def test_access_user_detail(self):
#         response = self.client.get('/user/1/')
#         self.assertEqual(403, response.status_code)
#
#     def test_access_snippet_highlight(self):
#         response = self.client.get('/snippet/1/highlight/')
#         self.assertEqual(200, response.status_code)
#
#     def test_assess_snippet_detail(self):
#         response = self.client.get('/snippet/1/')
#         self.assertEqual(200, response.status_code)
#
#
# class UserLogin2(APITestCase):
#     def setUp(self):
#         User.objects.create(username='mac', password='zengjiean', is_superuser=True, is_staff=True)
#         self.user = User.objects.get(username='mac')
#         self.client = APIClient(enforce_csrf_checks=True)
#         self.client.force_authenticate(user=self.user, token=None)
#         test1 = User.objects.create(username='123', password='123456')
#         Snippets.objects.create(code='13245', owner=test1)
#         Snippets.objects.create(code='1324', owner=test1)
#         response = self.client.get('/user/')
#         self.assertEqual(200, response.status_code)
#
#     def test_user_have_snippet(self):
#         request = self.client.get('/user/', format='json')
#         self.assertEqual(200, request.status_code)
#         self.assertEqual(2, len(request.data['results'][1]['snippets']))
#         self.assertEqual(0, len(request.data['results'][0]['snippets']))
#
#     def test_user_access_root(self):
#         request = self.client.get('/', format='json')
#         self.assertEqual(200, request.status_code)
#
#     def test_user_creat_user(self):
#         response = self.client.post('/user/', data={'username': 'dfh', 'password': '123456789'})
#         self.assertEqual(405, response.status_code)
#
