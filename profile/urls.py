from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
import profile.views as views


route = DefaultRouter()
route.register(r'profile',views.ProfileViewSet)

urlpatterns = [
    url(r'^',include(route.urls))
]