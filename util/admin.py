from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get(app_label='auth', model='group')

# TODO 这里应该集中到一个统一的文件中管理
# TODO 我发现guardian是可以自定义对象的各种属性，包括使用不同对象的权限去认证
try:
    Permission.objects.get(codename='view_task')
except:
    permission = Permission.objects.create(codename='view_task',
                                           name='view task',
                                           content_type=content_type)
