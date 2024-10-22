from django.urls import path
from .views import home, product_list, product_detail, add_product

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views 

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/add/', add_product, name='add_product'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)