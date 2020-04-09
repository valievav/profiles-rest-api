from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    Allows user to edit its own profile
    """

    def has_object_permission(self, request, view, obj):
        """
        Checks if user has permission to update profile.
        Allowed own profile update only.
        """
        if request.method in permissions.SAFE_METHODS:  # allow to view other users info (on GET)
            return True

        return obj.id == request.user.id  # allow to change obj ONLY if it belongs to user (on PATCH/PUT/DELETE)


class UpdateOwnStatus(permissions.BasePermission):
    """
    Allow users to update their own status
    """

    def has_object_permission(self, request, view, obj):
        """
        Checks that user has permission to update status.
        Allowed own status update only.
        """
        if request.method in permissions.SAFE_METHODS:   # allow to view other users info (on GET)
            return True

        return obj.id == request.user.id  # allow to change obj ONLY if it belongs to user (on PATCH/PUT/DELETE)

