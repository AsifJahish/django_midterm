from django.urls import path
from .views import (
    ProductCreateView, ProductListView,
    CartDetailView, CartItemAddView, CartItemRemoveView
)

urlpatterns = [
    # Product URLs
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/', ProductListView.as_view(), name='product-list'),

    # Cart URLs
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
    path('cart/add/', CartItemAddView.as_view(), name='cart-item-add'),
    path('cart/remove/<int:pk>/', CartItemRemoveView.as_view(), name='cart-item-remove'),
]
