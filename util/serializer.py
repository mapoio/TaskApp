from django.contrib.auth.models import Permission
from rest_framework import serializers
from guardian.models import GroupObjectPermission, UserObjectPermission
from rest_framework.permissions import IsAdminUser


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = ('id', 'content_type', 'codename', 'name')


class GuardianGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupObjectPermission
        fields = '__all__'


class GuardianUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserObjectPermission
        fields = '__all__'
