from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer
from django.contrib.auth import get_user_model

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    item_total_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'item_price', 'item_total_price']

    def get_item_total_price(self, obj):
        return obj.total_price()

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    buyer = serializers.ReadOnlyField(source='buyer.username')
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'buyer', 'order_date', 'status', 'total_amount', 'items']

    def get_total_amount(self, obj):
        return obj.total_amount
