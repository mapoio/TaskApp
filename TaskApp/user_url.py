from django.conf.urls import url,include
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from .views import CustomPasswordResetView,CustomRegistrationView
from djoser.views import LogoutView,PasswordResetConfirmView
from  .settings import DEBUG

urlpatterns = []

if DEBUG:
    urlpatterns += [
        url(r'^password/reset/confirm/',PasswordResetConfirmView.as_view()),
        url(r'^password/reset/', CustomPasswordResetView.as_view()),  # 开发时时使用这个接口来获得邮件内容，显示在控制台
        url(r'^register', CustomRegistrationView.as_view()),  # debug时使用这个接口来获得邮件内容，显示在控制台
    ]
urlpatterns += [
    url(r'^login', obtain_jwt_token),
    url(r'^logout', LogoutView.as_view()),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^', include('djoser.urls.base')),
]
