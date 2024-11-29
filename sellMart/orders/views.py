from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from .permissions import IsBuyer

# Order Views
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsBuyer]

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsBuyer]

    def get_object(self):
        return Order.objects.get(id=self.kwargs['pk'], buyer=self.request.user)

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsBuyer]

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)
