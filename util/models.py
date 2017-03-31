from django.db import models

# Create your models here.
class ModulePermission(models.Model):
    class Meta:
        # 创建管理员级别的权限
        permissions = (
            ("user.user", u"用户管理"),
            ("company.company",u"组织管理-组织管理"),
            ("company.department",u"组织管理-部门管理"),
        )