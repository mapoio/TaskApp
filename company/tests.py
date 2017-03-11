from unittest import skipIf
import django
from django.conf import settings
from django.contrib.auth import get_user_model, user_logged_in, user_login_failed, user_logged_out
from django.contrib.auth.tokens import default_token_generator
from django.core import mail
from django.test.utils import override_settings
from django.test.testcases import SimpleTestCase
from djet import assertions, utils, restframework
from rest_framework import status, authtoken
from .models import Company,Department
# Create your tests here.

def create_user(**kwargs):
    data = {
        'username': 'admin',
        'password': 'password123',
        'email': 'john@beatles.com',
        'is_superuser': True,
        'is_active': True,
        'is_staff': True,
    }
    data.update(kwargs)
    user = get_user_model().objects.create_user(**data)
    user.raw_password = data['password']
    return user

