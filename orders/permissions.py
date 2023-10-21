from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Check if the user own the item.
    """
    message = 'You must be the owner of this object'
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user