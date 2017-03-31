from django.db import models
from django.contrib.auth.models import User, Group
from company.models import Department
from django.db.models.signals import post_save


# Create your models here.

class Tag(models.Model):
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey('Profile', related_name='tag', db_index=True)
    data = models.CharField(max_length=64, db_index=True, unique=True)

    class Meta:
        ordering = ('-created', 'data')
        get_latest_by = 'created'

    def __str__(self):
        return '%d: %s' % (self.user_id, self.data)


class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    user = models.OneToOneField(User,
                                unique=True,
                                related_name='profile',
                                db_index=True)
    nickname = models.CharField(max_length=64,
                                default='',
                                blank=True,
                                db_index=True,
                                verbose_name=u'姓名')

    sex = models.BooleanField(default=0,
                              verbose_name=u'性别',
                              help_text=u'这个还是要选的')

    phone = models.CharField(max_length=64,
                             default='',
                             blank=True,
                             verbose_name=u'电话',
                             help_text=u'11位中国大陆地区的手机号码')

    department = models.ForeignKey(Department,
                                   null=True,
                                   related_name='profile',
                                   default=None,
                                   on_delete=models.SET_NULL,
                                   verbose_name=u'组织',
                                   help_text=u'选择一个适合的组织')

    class Meta:
        ordering = ('-created', 'nickname')
        get_latest_by = 'created'

    def __str__(self):
        return '%d: %s' % (self.user_id, self.user.username)
