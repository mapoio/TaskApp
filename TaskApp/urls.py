"""TaskApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from .views import CustomRegistrationView,CustomPasswordResetView
from djoser.views import LogoutView
from rest_framework.routers import DefaultRouter
from  .settings import DEBUG

urlpatterns = []

if DEBUG:
    urlpatterns += [
        url(r'^api/dev/',include('company.urls')),
        url(r'^api/v1/auth/user/password/reset/', CustomPasswordResetView.as_view()),  # 开发时时使用这个接口来获得邮件内容，显示在控制台
        url(r'^api/v1/auth/user/register', CustomRegistrationView.as_view()),  # debug时使用这个接口来获得邮件内容，显示在控制台
    ]

urlpatterns += [
    # url(r'^',include(route.urls))
    url(r'^api/v1/auth/user/login', obtain_jwt_token),
    url(r'^api/v1/auth/user/logout', LogoutView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/',include('rest_framework.urls')),
    url(r'^api/v1/auth/user/api-token-refresh/', refresh_jwt_token),
    url(r'^api/v1/auth/user/api-token-verify/', verify_jwt_token),
    url(r'^api/v1/auth/user/', include('djoser.urls.base')),
]

