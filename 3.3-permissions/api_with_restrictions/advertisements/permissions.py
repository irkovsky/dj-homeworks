from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    def has_object_permisiion(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.creator == request.user