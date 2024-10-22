from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='products'),
    path('category/<slug:category_slug>/', views.ProductListView.as_view(), name='product_list_by_category'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('seller/products/', views.SellerProductListView.as_view(), name='seller_products'),
    path('seller/product/add/', views.ProductCreateView.as_view(), name='product_create'),
    path('seller/product/<slug:slug>/edit/', views.ProductUpdateView.as_view(), name='product_update'),
    path('seller/product/<slug:slug>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
]