from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Check if the user prefers the item.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user