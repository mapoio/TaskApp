from rest_framework import permissions


class IsAdminCreateOnly(permissions.BasePermission):
    # TODO 使用下面这个函数作为入口，在加上下面第二个函数作为权限-对象级别的控制。
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        pass
