from rest_framework import serializers
from .models import Profile
from company.models import Department

class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ('url','id','user','nickname','sex','phone','department','created')
        depth = 1
