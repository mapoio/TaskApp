from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class UserProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16,default='',blank=True)
    sex = models.IntegerField(default=0)
    phone = models.CharField(max_length=16,default='',blank=True)

    class Meta:
        ordering = ('created',)
        get_latest_by = 'created'


