from rest_framework import permissions
from guardian.core import ObjectPermissionChecker
from guardian.shortcuts import get_perms_for_model,get_user_perms
from django.http import Http404

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
        elif view.action == 'list':
            peimission = 'add_' + view.queryset.model._meta.app_label
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


class ObjectPermissions(permissions.DjangoModelPermissions):
    """
    The request is authenticated using Django's object-level permissions.
    It requires an object-permissions-enabled backend, such as Django Guardian.

    It ensures that the user is authenticated, and has the appropriate
    `add`/`change`/`delete` permissions on the object using .has_perms.

    This permission can only be applied against view classes that
    provide a `.queryset` attribute.
    """
    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    _pydev_stop_at_break = True

    def get_required_object_permissions(self, view, method, model_cls):
        # TODO 在此处添加获取用户自定义的需要的权限
        if hasattr(view, 'permission_required'):
            for parm_test in view.permission_required:
                self.perms_map[parm_test] = view.permission_required[parm_test]
        kwargs = {
            'app_label': model_cls._meta.app_label,
            'model_name': model_cls._meta.model_name
        }
        return [perm % kwargs for perm in self.perms_map[method]]

    def has_permission(self, request, view):
        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.
        if getattr(view, '_ignore_model_permissions', False):
            return True

        if hasattr(view, 'get_queryset'):
            queryset = view.get_queryset()
        else:
            queryset = getattr(view, 'queryset', None)

        assert queryset is not None, (
            'Cannot apply DjangoModelPermissions on a view that '
            'does not set `.queryset` or have a `.get_queryset()` method.'
        )

        if view.suffix != 'List':
            return True

        perms = self.get_required_permissions(request.method, queryset.model)

        return (
            request.user and
            (permissions.is_authenticated(request.user) or not self.authenticated_users_only) and
            request.user.has_perms(perms)
        )

    def has_object_permission(self, request, view, obj):
        if hasattr(view, 'get_queryset'):
            queryset = view.get_queryset()
        else:
            queryset = getattr(view, 'queryset', None)

        assert queryset is not None, (
            'Cannot apply DjangoObjectPermissions on a view that '
            'does not set `.queryset` or have a `.get_queryset()` method.'
        )

        model_cls = queryset.model
        user = request.user

        perms = self.get_required_object_permissions(view, request.method, model_cls)

        if 'all' in perms:
            return True

        checker = ObjectPermissionChecker(user)

        for perm in perms:
            if checker.has_perm(perm, obj):
                return True

        # TODO 在此处添加对象级别的权限控制（封装并传参数 permission_required）
        # TODO 记得有外键`关联的地方设置on_delete属性，否则后果严重
        if not user.has_perms(perms, obj):
            # If the user does not have permissions we need to determine if
            # they have read permissions to see 403, or not, and simply see
            # a 404 response.

            if request.method in permissions.SAFE_METHODS:
                # Read permissions already checked and failed, no need
                # to make another lookup.
                raise Http404

            read_perms = self.get_required_object_permissions(view, 'GET', model_cls)
            if not user.has_perms(read_perms, obj):
                raise Http404

            # Has read permissions.
            return False

        return True
