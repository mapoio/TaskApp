from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views import PermissionViewSet,GuardianGroupViewSet,GuardianUserViewSet

route = DefaultRouter()
route.register(r'django', PermissionViewSet)
route.register(r'user', GuardianUserViewSet)
route.register(r'group', GuardianGroupViewSet)

urlpatterns = [
    url(r'^', include(route.urls))
]
