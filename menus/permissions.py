from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Check if Patient is author of the Survey.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff
     
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff