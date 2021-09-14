from rest_framework.permissions import BasePermission


class MoviePermissions(BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_authenticated
        elif view.action == 'create':
            return True
