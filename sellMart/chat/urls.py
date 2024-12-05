from django.urls import path
from .views import ChatRoomCreateView, MessageCreateView, ChatRoomListView

urlpatterns = [
    path('chats/create/', ChatRoomCreateView.as_view(), name='chat-create'),
    path('chats/<int:chatroom_id>/message/', MessageCreateView.as_view(), name='chat-message-create'),
    path('chats/', ChatRoomListView.as_view(), name='chat-list'),
]
