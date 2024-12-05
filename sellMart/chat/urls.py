from django.urls import path
from .views import ChatRoomCreateView, MessageCreateView, ChatRoomListView, chat_room_view


from . import views

urlpatterns = [
    path('chats/create/', ChatRoomCreateView.as_view(), name='chat-create'),
    path('chats/<int:chatroom_id>/message/', MessageCreateView.as_view(), name='chat-message-create'),
    path('chats/', ChatRoomListView.as_view(), name='chat-list'),

#  path('product/<int:product_id>/message/', views.create_or_open_chat, name='create-or-open-chat'),
#     path('chatroom/<int:chatroom_id>/', views.chat_room_view, name='chat-room'),


    path('chat/<int:chatroom_id>/', views.chat_room_view, name='chat-room'),
]
