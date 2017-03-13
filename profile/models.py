from django.db import models
from django.contrib.auth.models import User
from company.models import Department
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16,default='',blank=True)
    sex = models.IntegerField(default=0)
    phone = models.CharField(max_length=16,default='',blank=True)
    department = models.ForeignKey(Department,blank=True,related_name='profile',default=None)

    class Meta:
        ordering = ('created',)
        get_latest_by = 'created'

    def __str__(self):
        return self.created

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)