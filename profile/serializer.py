from rest_framework import serializers
from .models import Profile,Tag
from django.contrib.auth.models import User,Group
from company.models import Department
from TaskApp.settings import DJOSER
from django.db import transaction


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','data','created')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id','name','company')


class ProfileSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=True,read_only=True)
    tag = TagSerializer(many=True,required=False,allow_null=True)

    class Meta:
        model = Profile
        fields = ('id','nickname','sex','phone','tag','department')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id','username','email','is_active','profile','groups')

    #应该编写一个update函数来更新
    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     user = User.objects.create(**validated_data)
    #     profile_data['user'] = user
    #     profile = Profile(nickname=profile_data['nickname'], sex=profile_data['sex'], phone=profile_data['phone'],
    #                       user=user, user_id=user.id)
    #     profile.save()
    #     return user
    # 模型应当绑定为User，通过User来轻松创建


class UserRegistrationSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(allow_null=True,required=False)
    password = serializers.CharField(style={'input_type': 'password'},
                                     write_only=True,
                                     validators=DJOSER['PASSWORD_VALIDATORS'])

    class Meta:
        model = User
        fields = ('id','username','email','password','profile')


    def user_create(self,validated_data):
        """
        此处还要添加检查email的参数
        :param validated_data:
        :return:
        """
        profile_data = {
            'nickname':'',
            'sex':1,
            'phone':'',
            'tag':[]
        }
        if 'profile' in validated_data:
            profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        profile_data.pop('tag')
        profile = Profile(user=user,**profile_data)
        profile.save()
        user.set_password(user.password)
        return user

    def create(self, validated_data):
        if DJOSER['SEND_ACTIVATION_EMAIL']:
            with transaction.atomic():
                user = self.user_create(validated_data)
                user.is_active = False
                user.save(update_fields=['is_active','password'])
        else:
            user = self.user_create(validated_data)
            user.save(update_fields=['password'])
        return user