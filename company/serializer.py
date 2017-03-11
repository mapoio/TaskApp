from .models import Company,Department
from rest_framework import serializers


class CompanySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Company
        fields = ('url','name','info','department',)
        depth = 1


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    # company = serializers.ReadOnlyField(source='company.name')
    class Meta:
        model = Department
        fields = ('url','company','name','info')
        depth = 1
