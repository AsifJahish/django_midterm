from rest_framework.permissions import BasePermission

class IsBuyer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'buyer'

class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'seller'

class IsBuyerOrSeller(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.user_type == 'buyer' or request.user.user_type == 'seller')
