from django.urls import path
from .views import CustomUserCreateView, CustomUserListView

from .views import signup, signin
urlpatterns = [
    path('create/', CustomUserCreateView.as_view(), name='user-create'),
    path('list/', CustomUserListView.as_view(), name='user-list'),


    path('signin/', signin, name='user-signin'),
    path('signup/', signup, name='user-signup'),
   
]
