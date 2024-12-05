from rest_framework.permissions import BasePermission

from rest_framework.permissions import BasePermission

class IsSeller(BasePermission):
    def has_permission(self, request, view):
        # Check if user is authenticated and has the 'seller' user_type
        return request.user.is_authenticated and request.user.user_type == 'seller'

class IsBuyer(BasePermission):
    def has_permission(self, request, view):
        # Check if user is authenticated and has the 'buyer' user_type
        return request.user.is_authenticated and request.user.user_type == 'buyer'
