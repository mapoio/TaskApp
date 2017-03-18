from djoser.views import RegistrationView
from djoser import serializers, settings, utils,signals
from TaskApp import settings
from rest_framework.response import Response
from rest_framework import generics, permissions, status, response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from profile.models import Profile
from djoser.serializers import UserRegistrationSerializer
from profile.serializer import ProfileSerializer
User = get_user_model()

class CustomRegistrationView(RegistrationView):
    '''
    这是用于DEBUG时没有设置邮件服务器，将会通过控制台打印邮件内容，来进行测试
    实际过程中不会调用，注意，在激活地址中是由前台来控制的，参数是直接在最后两个字段，
    由前端调用，用来激活
    '''
    def create(self, request, *args, **kwargs):
        nickname = request.data['nickname'] if False else ' '
        sex= request.data['sex'] if False else 1
        phone = request.data['phone'] if False else ' '
        data = {
            'email': request.data['email'],
            'username': request.data['username'],
            'password': request.data['password']
        }
        # 这里还要添加验证模型的东西
        # user = User(email = data['email'],username = data['username'],password = data['password'],is_active = 0)

        try:
            users = UserRegistrationSerializer(data=data)
            users.is_valid()
            users.save()
            user = User.objects.get(username = data['username'])
            profile_data = {
                'nickname': nickname,
                'sex': sex,
                'phone': phone,
            }
            profile = Profile(nickname=profile_data['nickname'], sex=profile_data['sex'], phone=profile_data['phone'], user=user,user_id=user.id)
        # profile = ProfileSerializer(data=profile_data)
        # profile.is_valid()
            profile.save()
            signals.user_registered.send(sender=self.__class__, user=user, request=self.request)
            if 1:
                self.send_activation_email(user)
            elif settings.get('SEND_CONFIRMATION_EMAIL'):
                self.send_confirmation_email(user)
            return Response({'status': 'User created success'},
                            status=status.HTTP_201_CREATED)
        except:
            return Response(users.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        user = serializer.save()
        signals.user_registered.send(sender=self.__class__, user=user, request=self.request)
        if settings.get('SEND_ACTIVATION_EMAIL'):
            self.send_activation_email(user)
        elif settings.get('SEND_CONFIRMATION_EMAIL'):
            self.send_confirmation_email(user)

    def send_activation_email(self, user):
        email_factory = utils.UserActivationEmailFactory.from_request(self.request, user=user)
        email = email_factory.create()
        if settings.EMAIL_BACKEND:
            print(email.body)
        email.send()

    def send_confirmation_email(self, user):
        email_factory = utils.UserConfirmationEmailFactory.from_request(self.request, user=user)
        email = email_factory.create()
        if settings.EMAIL_BACKEND:
            print(email.body)
        email.send()


class CustomPasswordResetView(utils.ActionViewMixin, generics.GenericAPIView):
    '''
    这是用于DEBUG时没有设置邮件服务器，将会通过控制台打印邮件内容，来进行测试
    实际过程中不会调用，注意，在激活地址中是由前台来控制的，参数是直接在最后两个字段，
    由前端调用，用来激活
    '''
    serializer_class = serializers.serializers_manager.get('password_reset')
    permission_classes = (
        permissions.AllowAny,
    )

    _users = None

    def get_users(self, email):
        if self._users is None:
            active_users = User._default_manager.filter(
                email__iexact=email,
                is_active=True,
            )
            self._users = [u for u in active_users if u.has_usable_password()]
        return self._users

    def _action(self, serializer):
        for user in self.get_users(serializer.data['email']):
            self.send_password_reset_email(user)
        return response.Response(status=status.HTTP_204_NO_CONTENT)


    def send_password_reset_email(self, user):
        email_factory = utils.UserPasswordResetEmailFactory.from_request(self.request, user=user)
        email = email_factory.create()
        print(email.body)
        email.send()