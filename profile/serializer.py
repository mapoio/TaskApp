from rest_framework import serializers
from .models import Profile,Tag
from django.contrib.auth.models import User,Group
from company.models import Department

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','data')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id','name','company')


class ProfileSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    phone = serializers.CharField(source='profile.phone',read_only=True)
    department = DepartmentSerializer(many=True)
    username = serializers.CharField(source='profile.user.username',read_only=True)
    email = serializers.CharField(source='profile.user.email',read_only=True)
    is_active = serializers.BooleanField(source='profile.user.is_active',read_only=True)

    class Meta:
        model = Profile
        fields = ('id','username','nickname','email','phone','sex','groups','department','tag','is_active')