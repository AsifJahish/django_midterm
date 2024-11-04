from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Assuming you already have these imports
from userApp.models import Buyer, Seller, User

class ChatRoom(models.Model):
    """
    Represents a chat room between a buyer and a seller.
    """
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name="chat_rooms")
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="chat_rooms")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('buyer', 'seller')  # Ensures unique chat room per buyer-seller pair

    def __str__(self):
        return f"ChatRoom between {self.buyer.user.username} and {self.seller.user.username}"


class Message(models.Model):
    """
    Represents an individual message within a ChatRoom.
    """
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"

