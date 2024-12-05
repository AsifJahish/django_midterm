from django.urls import path
from .views import (
    ProductCreateView, ProductListView,
    CartDetailView, CartItemAddView, CartItemRemoveView,
    
)

from . import views

from .views import add_to_cart, cart_items

from .views import product_list, product_create

from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Product URLs
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/', ProductListView.as_view(), name='product-list'),

    # Cart URLs
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
    path('cart/add/', CartItemAddView.as_view(), name='cart-item-add'),
    path('cart/remove/<int:pk>/', CartItemRemoveView.as_view(), name='cart-item-remove'),

    path('cart/add/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/items/', cart_items, name='cart-items'),


    path('list/', product_list, name='product-list'),
    path('productscreate', product_create, name='product-create'),

    path('logout/', LogoutView.as_view(), name='logout'),

]
