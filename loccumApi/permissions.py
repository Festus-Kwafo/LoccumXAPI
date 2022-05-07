from rest_framework import permissions

class IsLoccumUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_locum)

class IsInstitutionUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_institution)

class IsLoccumOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
    # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True            
    # Write permissions are only allowed to the loccum of a job
        return bool(obj.created_by == request.user.is_locum)

class IsInstitutionOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
    # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
            
    # Write permissions are only allowed to the institution of a job to update
        return bool(obj.created_by == request.user)