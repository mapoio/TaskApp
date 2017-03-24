from rest_framework import permissions
from guardian.compat import __all__
from guardian.shortcuts import assign_perm

"""
权限规则：
    指定权限内的人允许创建资源
    创建资源的人拥有修改（删除需要看情况）该资源的权限
    管理员分级
    系统管理员具有所有权限
    删除通过假删除来实现，不能够在数据库中真的删除了
"""

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    创建者权限检查
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user

