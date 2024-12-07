from rest_framework import permissions


class CheckOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class CheckHotel(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.status == 'client'

    def has_object_permission(self, request, view, obj):
        return obj.status != 'доступно'


class CheckOwnerHotel(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'owner':
            return True
        return False

