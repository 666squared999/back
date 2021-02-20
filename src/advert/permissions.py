from rest_framework import permissions


class UsersPermission(permissions.BasePermission):
    user_required_actions = [
        "create",
        "update",
        "partial_update",
        "destroy",
    ]

    def has_permission(self, request, view):

        if view.action in self.user_required_actions:
            return request.user.is_authenticated
        else: return True