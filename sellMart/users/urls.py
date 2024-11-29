from django.urls import path
from .views import CustomUserCreateView, CustomUserListView

urlpatterns = [
    path('create/', CustomUserCreateView.as_view(), name='user-create'),
    path('list/', CustomUserListView.as_view(), name='user-list'),
]
