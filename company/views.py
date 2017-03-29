from .serializer import CompanySerializer, DepartmentSerializer
from .models import Company, Department
from rest_framework import viewsets, permissions
from .permission import IsAdminCreateOnly
from util.permission import ModulePermission
# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          ModulePermission)
    permission_required = ['company.change_company']


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminCreateOnly)
