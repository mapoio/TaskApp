from django.db import models
from django.contrib.auth.models import User,Group
from company.models import Department
from django.db.models.signals import post_save
# Create your models here.

class Tag(models.Model):
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey('Profile',related_name='tag',db_index=True)
    data = models.CharField(max_length=64,db_index=True,unique=True)

    class Meta:
        ordering = ('-created','data')
        get_latest_by = 'created'

    def __str__(self):
        return '%s: %s' % self.user_id,self.data

class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User,unique=True,related_name='profile',db_index=True)
    nickname = models.CharField(max_length=64,default='',blank=True,db_index=True)
    sex = models.IntegerField(default=0)
    phone = models.CharField(max_length=64,default='',blank=True)
    department = models.ForeignKey(Department,null=True,related_name='profile',default=None)
    # group = models.ForeignKey(Group,null=True,related_name='profile',default=None)
    # is_active = models.BooleanField(default=True,db_index=True)

    class Meta:
        ordering = ('-created','nickname')
        get_latest_by = 'created'

    def __str__(self):
        return '%s: %s' % self.user_id,self.user.username

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         profile = Profile()
#         profile.user = instance
#         profile.save()
#
# post_save.connect(create_user_profile, sender=User)