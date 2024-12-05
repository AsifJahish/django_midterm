from django.urls import path
from .views import ReviewCreateView, ReviewListView

urlpatterns = [
    path('reviews/create/<int:product_id>/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:product_id>/', ReviewListView.as_view(), name='review-list'),
]
