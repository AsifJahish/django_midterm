from rest_framework import serializers
from .models import ChatRoom, Message
from users.models import CustomUser
from products.serializers import ProductSerializer

class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = Message
        fields = ['id', 'sender', 'sender_username', 'content', 'sent_at']

class ChatRoomSerializer(serializers.ModelSerializer):
    buyer_username = serializers.ReadOnlyField(source='buyer.username')
    seller_username = serializers.ReadOnlyField(source='seller.username')
    product_name = serializers.ReadOnlyField(source='product.name')
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatRoom
        fields = ['id', 'buyer_username', 'seller_username', 'product_name', 'messages', 'created_at']
