from django_graphene_permissions.permissions import BasePermission


class IsSuperUserPermission(BasePermission):
    @staticmethod
    def has_permission(context):
        return bool(context.user.is_superuser)
