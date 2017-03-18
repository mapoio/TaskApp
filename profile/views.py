from django.shortcuts import render
from rest_framework import viewsets,permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializer import ProfileSerializer
# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer