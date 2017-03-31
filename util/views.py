from rest_framework import viewsets
from .serializer import Permission, PermissionSerializer, IsAdminUser, GuardianGroupSerializer, GuardianUserSerializer
from guardian.models import GroupObjectPermission,UserObjectPermission


# Create your views here.

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = (IsAdminUser,)


class GuardianGroupViewSet(viewsets.ModelViewSet):
    queryset = GroupObjectPermission.objects.all()
    serializer_class = GuardianGroupSerializer
    permission_classes = (IsAdminUser,)


class GuardianUserViewSet(viewsets.ModelViewSet):
    queryset = UserObjectPermission.objects.all()
    serializer_class = GuardianUserSerializer
    permission_classes = (IsAdminUser,)
