from rest_framework.permissions import BasePermission

class HasRolePermission(BasePermission):
    def has_permission(self, request, view):
        required_role = getattr(view, 'required_role', None)
        return request.user.is_authenticated and request.user.role and request.user.role.name == required_role