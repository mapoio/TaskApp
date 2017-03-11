from django.shortcuts import render
from .serializer import CompanySerializer,DepartmentSerializer
from .models import Company,Department
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

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
            return Response({'status': 'department created success'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)



class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

