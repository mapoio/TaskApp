from django.shortcuts import render
from rest_framework import viewsets,permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from django.contrib.auth.models import User
from .serializer import ProfileSerializer,UserSerializer
from util.handler import Error
# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

