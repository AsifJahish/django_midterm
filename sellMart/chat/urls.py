from django.urls import path
from .views import ChatRoomCreateView, MessageCreateView, ChatRoomListView, chat_room_view

urlpatterns = [
    path('chats/create/', ChatRoomCreateView.as_view(), name='chat-create'),
    path('chats/<int:chatroom_id>/message/', MessageCreateView.as_view(), name='chat-message-create'),
    path('chats/', ChatRoomListView.as_view(), name='chat-list'),
    path('chats/<int:chatroom_id>/', chat_room_view, name='chat-room'),
]
