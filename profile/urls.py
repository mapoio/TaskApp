from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
import profile.views as view
from django.conf.urls import url,include
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from .views import CustomPasswordResetView,CustomRegistrationView
from djoser.views import LogoutView,PasswordResetConfirmView
from TaskApp.settings import DEBUG
from djoser import views
from django.contrib.auth import get_user_model

#
route = DefaultRouter()
route.register(r'profile',view.ProfileViewSet)
#
# urlpatterns = [
#     url(r'^',include(route.urls))
# ]

# urlpatterns = []
#
# urlpatterns += [
#     url(r'^dev/',include(route.urls)),
#     url(r'^password/reset/confirm/',PasswordResetConfirmView.as_view()),
#     url(r'^login', obtain_jwt_token),
#     url(r'^logout', LogoutView.as_view()),
#     url(r'^api-token-refresh/', refresh_jwt_token),
#     url(r'^api-token-verify/', verify_jwt_token),
#     # url(r'^', include('djoser.urls.base')),
# ]

User = get_user_model()

base_urlpatterns = []

if DEBUG:
    base_urlpatterns += [
        url(r'^password/reset/', CustomPasswordResetView.as_view()),  # 开发时时使用这个接口来获得邮件内容，显示在控制台
        url(r'^register/', CustomRegistrationView.as_view()),  # debug时使用这个接口来获得邮件内容，显示在控制台
    ]

base_urlpatterns += [
    url(r'^dev/',include(route.urls)),
    url(r'^login/', obtain_jwt_token),
    url(r'^logout/', LogoutView.as_view()),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^me/$', views.UserView.as_view(), name='user'),
    url(r'^register/$', views.RegistrationView.as_view(), name='register'),
    url(r'^activate/$', views.ActivationView.as_view(), name='activate'),
    url(r'^{0}/$'.format(User.USERNAME_FIELD), views.SetUsernameView.as_view(), name='set_username'),
    url(r'^password/$', views.SetPasswordView.as_view(), name='set_password'),
    url(r'^password/reset/$', views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password/reset/confirm/$', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

urlpatterns = tuple(base_urlpatterns) + (url(r'^$', views.RootView.as_view(), name='root'),)
