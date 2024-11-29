from django.urls import path
from .views import OrderCreateView, OrderDetailView, OrderListView

urlpatterns = [
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
]
