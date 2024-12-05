

# from django.urls import path
# from .views import OrderCreateView, OrderDetailView, OrderListView

# urlpatterns = [
#     path('orders/create/', OrderCreateView.as_view(), name='order-create'),
#     path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
#     path('orders/', OrderListView.as_view(), name='order-list'),
# ]


from django.urls import path
from .views import OrderCreateView, OrderDetailView, OrderListView, ObtainTokenPairView, RefreshTokenView

urlpatterns = [
    path('api/token/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    
    # Order-related endpoints
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
]
