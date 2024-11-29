from rest_framework import serializers
from .models import Review
from products.serializers import ProductSerializer
from users.models import CustomUser

class ReviewSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    buyer_username = serializers.ReadOnlyField(source='buyer.username')

    class Meta:
        model = Review
        fields = ['id', 'product', 'product_name', 'buyer_username', 'rating', 'comment', 'created_at']
