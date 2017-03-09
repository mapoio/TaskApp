from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.


class GroupProfile(models.Model):
    name = models.CharField(max_length=16)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        get_latest_by = 'created'

    def __str__(self):
        return self.name,self.created


class Academic(models.Model):
    name = models.CharField(max_length=16)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        get_latest_by = 'created'

    def __str__(self):
        return self.name, self.created

class Major(models.Model):
    name = models.CharField(max_length=16)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        get_latest_by = 'created'

    def __str__(self):
        return self.name,self.created


class UserProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16,default='',blank=True)
    sex = models.IntegerField(default=0)
    phone = models.CharField(max_length=16,default='',blank=True)
    group = models.ForeignKey(GroupProfile,related_name='userprofile')
    birth = models.DateTimeField()
    classes = models.ForeignKey(Major)
    academic = models.ForeignKey(Academic)
    major = models.ForeignKey(Major)

    class Meta:
        ordering = ('created',)
        get_latest_by = 'created'


