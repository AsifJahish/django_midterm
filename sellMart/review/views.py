from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsBuyer
from products.models import Product

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsBuyer]

    def perform_create(self, serializer):
        product = Product.objects.get(id=self.kwargs['product_id'])
        serializer.save(buyer=self.request.user, product=product)

class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        product = Product.objects.get(id=self.kwargs['product_id'])
        return Review.objects.filter(product=product)
