from .serializer import CompanySerializer,DepartmentSerializer
from .models import Company,Department
from rest_framework import viewsets,permissions
from rest_framework.response import Response
from rest_framework import status
from .permission import IsAdminCreateOnly
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminCreateOnly)

    def post(self, request, *args, **kwargs):
        data = {
            'name':request.data['name'],
            'info':request.data['info'],
            'company':self.get_object()
        }
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            department = Department.objects.create(name = data['name'],info=data['info'],company = data['company'])
            department.save()
            return Response({'status': 'department created success'},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)



class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminCreateOnly)

    def create(self, request, *args, **kwargs):
        data = {
            'name': request.data['name'],
            'info': request.data['info'],
            'company': Company.objects.get(id=request.data['company'])
        }
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            department = Department.objects.create(name=data['name'], info=data['info'], company=data['company'])
            department.save()
            return Response({'status': 'department created success'},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)