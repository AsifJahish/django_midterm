from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer
from .permissions import IsBuyerOrSeller

class ChatRoomCreateView(generics.CreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated, IsBuyerOrSeller]

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsBuyerOrSeller]

    def perform_create(self, serializer):
        chat_room = ChatRoom.objects.get(id=self.kwargs['chatroom_id'])
        serializer.save(sender=self.request.user, chat_room=chat_room)

class ChatRoomListView(generics.ListAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ChatRoom.objects.filter(buyer=self.request.user) | ChatRoom.objects.filter(seller=self.request.user)
