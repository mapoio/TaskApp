from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import UserSerializer
from djoser.views import RegistrationView
from djoser import serializers, settings, utils, signals
from TaskApp.settings import DEBUG
from rest_framework import generics, permissions, status, response
from django.contrib.auth import get_user_model

Users = get_user_model()


# Create your views here.


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.filter(is_active=True).order_by('-id')
    serializer_class = UserSerializer
    filter_fields = ('id', 'username',)


class CustomRegistrationView(RegistrationView):
    '''
    注册接口，API测试
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
    密码重置接口
    '''
    serializer_class = serializers.serializers_manager.get('password_reset')
    permission_classes = (
        permissions.AllowAny,
    )

    _users = None

    def get_users(self, email):
        if self._users is None:
            active_users = Users._default_manager.filter(
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
