from djoser.views import RegistrationView
from djoser import serializers, settings, utils,signals
from TaskApp.settings import DEBUG
from rest_framework.response import Response
from rest_framework import generics, permissions, status, response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from profile.models import Profile
# from djoser.serializers import UserRegistrationSerializer
from profile.serializer import UserRegistrationSerializer
User = get_user_model()


# class CustomRegistrationView(generics.CreateAPIView):
#     """
#     Use this endpoint to register new user.
#     """
#     serializer_class = UserRegistrationSerializer
#     permission_classes = (
#         permissions.AllowAny,
#     )
#
#     def perform_create(self, serializer):
#         user = serializer.save()
#         signals.user_registered.send(sender=self.__class__, user=user, request=self.request)
#         # if 1:
#         self.send_activation_email(user)
#         # elif settings.get('SEND_CONFIRMATION_EMAIL'):
#         #     self.send_confirmation_email(user)
#
#     def send_activation_email(self, user):
#         email_factory = utils.UserActivationEmailFactory.from_request(self.request, user=user)
#         email = email_factory.create()
#         email.send()
#
#     def send_confirmation_email(self, user):
#         email_factory = utils.UserConfirmationEmailFactory.from_request(self.request, user=user)
#         email = email_factory.create()
#         email.send()

class CustomRegistrationView(RegistrationView):
    '''
    这是用于DEBUG时没有设置邮件服务器，将会通过控制台打印邮件内容，来进行测试
    实际过程中不会调用，注意，在激活地址中是由前台来控制的，参数是直接在最后两个字段，
    由前端调用，用来激活
    '''

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
        if DEBUG:
            print(email.body)
        email.send()

    def send_confirmation_email(self, user):
        email_factory = utils.UserConfirmationEmailFactory.from_request(self.request, user=user)
        email = email_factory.create()
        if DEBUG:
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