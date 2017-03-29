from .serializer import CompanySerializer, DepartmentSerializer
from .models import Company, Department
from rest_framework import viewsets
from util.permission import ObjectPermissions
# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (ObjectPermissions,)
    permission_required = {'GET': 'all'}


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.DjangoObjectPermissions)
