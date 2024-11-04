from django.urls import path

from . import views



urlpatterns = [
    path('chat/<int:seller_id>/', views.chat_room, name='chat_room'),
    path('chat/<int:chat_room_id>/', views.chat_room, name='chat_room'),
    path('chat/<int:chat_room_id>/send/', views.send_message, name='send_message'),
]
