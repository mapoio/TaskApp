# TODO 测试未过
# from django.contrib.auth import get_user_model
# from djet import assertions
# from rest_framework import status
# from .models import Company, Department
# from django.urls import reverse
# from rest_framework.test import APITestCase, APIClient
#
#
# # Create your tests here.
#
# def create_user(**kwargs):
#     data = {
#         'username': 'admin',
#         'password': 'password123',
#         'email': 'john@beatles.com',
#         'is_superuser': True,
#         'is_active': True,
#         'is_staff': True,
#     }
#     data.update(kwargs)
#     user = get_user_model().objects.create_user(**data)
#     user.raw_password = data['password']
#     return user
#
#
# class CompanyViewTest(APITestCase,
#                       assertions.StatusCodeAssertionsMixin):
#     def setUp(self):
#         user = create_user()
#         self.user = user
#
#     def test_get_context_should_data(self):
#         url = reverse('company-list')
#         response = self.client.get(url)
#
#         self.assert_status_equal(response, status.HTTP_200_OK)
#         self.assertEqual(0, response.data['count'])
#
#     def test_post_un_login_should_403(self):
#         url = reverse('company-list')
#         response = self.client.post(url)
#
#         self.assert_status_equal(response, status.HTTP_403_FORBIDDEN)
#
#     def test_post_admin_should_create_company(self):
#         self.client = APIClient(enforce_csrf_checks=True)
#         self.client.force_authenticate(user=self.user, token=None)
#         url = reverse('company-list')
#         data = {
#             'name': 'test',
#             'info': 'test'
#         }
#         response = self.client.post(url, data, format='json')
#
#         self.assert_status_equal(response, status.HTTP_201_CREATED)
#         self.assertEqual('test', response.data['name'])
#         self.assertEqual('test', response.data['info'])
#
#     def test_get_company_retrieve_should_data(self):
#         Company.objects.create(name='test', info='test')
#         pk = 1
#         url = reverse('company-detail', args=[pk])
#         response = self.client.get(url)
#
#         self.assert_status_equal(response, status.HTTP_200_OK)
#         self.assertEqual('test', response.data['name'])
#
#     def test_post_un_login_create_company_department_should_403(self):
#         Company.objects.create(name='test', info='test')
#         pk = 1
#         url = reverse('company-detail', args=[pk])
#         data = {
#             'name': 'test',
#             'info': 'test'
#         }
#         response = self.client.post(url, data, format='json')
#
#         self.assert_status_equal(response, status.HTTP_403_FORBIDDEN)
#
#     def test_post_admin_create_company_department_should_success(self):
#         Company.objects.create(name='test', info='test')
#         pk = 1
#         self.client = APIClient(enforce_csrf_checks=True)
#         self.client.force_authenticate(user=self.user, token=None)
#         url = reverse('company-detail', args=[pk])
#         data = {
#             'name': 'test',
#             'info': 'test'
#         }
#         response = self.client.post(url, data, format='json')
#
#         self.assert_status_equal(response, status.HTTP_201_CREATED)
#         self.assertEqual('department created success', response.data['status'])
#
#     def test_put_admin_should_update_company(self):
#         pk = 1
#         self.company = Company.objects.create(name='test', info='test')
#         self.client = APIClient(enforce_csrf_checks=True)
#         self.client.force_authenticate(user=self.user, token=None)
#         url = reverse('company-detail', args=[pk])
#         data = {
#             'name': 'update',
#             'info': 'test'
#         }
#         response = self.client.put(url, data, format='json')
#
#         self.assert_status_equal(response, status.HTTP_200_OK)
#         self.assertEqual('update', response.data['name'])
#         self.assertEqual('test', response.data['info'])
#
#     def test_delete_admin_create_company_department_should_success(self):
#         Company.objects.create(name='test', info='test')
#         pk = 1
#         self.client = APIClient(enforce_csrf_checks=True)
#         self.client.force_authenticate(user=self.user, token=None)
#         url = reverse('company-detail', args=[pk])
#         response = self.client.delete(url, format='json')
#
#         self.assert_status_equal(response, status.HTTP_204_NO_CONTENT)
#
#
# class DepartmentViewTest(APITestCase,
#                          assertions.StatusCodeAssertionsMixin):
#     def setUp(self):
#         user = create_user()
#         self.user = user
#         self.company = Company.objects.create(name='test', info='test')
#         self.data = {
#             "name": "test-department",
#             "info": 'info',
#             "company": 1
#         }
#         Department.objects.create(company=self.company, name='test-department')
#         Department.objects.create(company=self.company, name='test-department')
#
#     def test_get_department_should_data(self):
#         url = reverse('department-list')
#         response = self.client.get(url)
#
#         self.assert_status_equal(response, status.HTTP_200_OK)
#         self.assertEqual(2, response.data['count'])
#
#     def test_post_un_login_should_403(self):
#         url = reverse('department-list')
#         response = self.client.post(url)
#
#         self.assert_status_equal(response, status.HTTP_403_FORBIDDEN)
#
#     def test_post_admin_should_create_department(self):
#         self.client = APIClient(enforce_csrf_checks=True)
#         self.client.force_authenticate(user=self.user, token=None)
#         url = reverse('department-list')
#         response = self.client.post(url, self.data, format='json')
#
#         self.assert_status_equal(response, status.HTTP_201_CREATED)
#         self.assertEqual('department created success', response.data['status'])
#
#     def test_put_admin_should_update_department(self):
#         pk = 1
#         Department.objects.create(name='test', info='test', company=self.company)
#         self.client = APIClient(enforce_csrf_checks=True)
#         self.client.force_authenticate(user=self.user, token=None)
#         url = reverse('department-detail', args=[pk])
#         data = {
#             'name': 'update',
#             'info': 'test'
#         }
#         response = self.client.put(url, data, format='json')
#
#         self.assert_status_equal(response, status.HTTP_200_OK)
#         self.assertEqual('update', response.data['name'])
#         self.assertEqual('test', response.data['info'])
#
#     def test_delete_admin_create_company_department_should_success(self):
#         Company.objects.create(name='test', info='test')
#         pk = 1
#         self.client = APIClient(enforce_csrf_checks=True)
#         self.client.force_authenticate(user=self.user, token=None)
#         url = reverse('department-detail', args=[pk])
#         response = self.client.delete(url, format='json')
#
#         self.assert_status_equal(response, status.HTTP_204_NO_CONTENT)
