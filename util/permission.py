from rest_framework import permissions
from guardian.core import ObjectPermissionChecker
from guardian.shortcuts import get_perms_for_model

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


class ModulePermission(permissions.BasePermission):
    authenticated_users_only = True

    # TOdo 权限检查，在此处添加，要自由控制，做好封装准备，当请求是post时，应当检查权限
    def has_permission(self, request, view):
        perms = get_perms_for_model(view.queryset.model)
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        checker = ObjectPermissionChecker(request.user)
        permission_required = view.permission_required
        for perm in permission_required:
            if checker.has_perm(perm, obj):
                return True

        return False
