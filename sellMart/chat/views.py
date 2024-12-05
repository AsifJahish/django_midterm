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


# # chat/views.py
# from django.shortcuts import render, get_object_or_404
# from .models import ChatRoom

# def chat_room_view(request, chatroom_id):
#     chat_room = get_object_or_404(ChatRoom, id=chatroom_id)
#     return render(request, 'chat.html', {'chat_room': chat_room})


# from django.shortcuts import render, redirect, get_object_or_404
# from chat.models import ChatRoom, Message
# from products.models import Product
# from django.contrib.auth.models import User
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required

# @login_required
# def create_or_open_chat(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
    
#     # Check if the buyer is authenticated
#     if not request.user.is_authenticated:
#         return redirect('login')  # Redirect to login if the user is not authenticated
    
#     # Try to find an existing chat room between the buyer and seller for this product
#     chat_room = ChatRoom.objects.filter(
#         buyer=request.user, 
#         seller=product.created_by, 
#         product=product
#     ).first()

#     if not chat_room:
#         # If no existing chat room, create a new one
#         chat_room = ChatRoom.objects.create(
#             buyer=request.user,
#             seller=product.created_by,
#             product=product
#         )

#     # Handle the message submission
#     if request.method == "POST":
#         message_content = request.POST.get("message")
#         if message_content:
#             Message.objects.create(
#                 chat_room=chat_room,
#                 sender=request.user,
#                 content=message_content
#             )
#             return redirect('create-or-open-chat', product_id=product.id)  # Refresh the page to see the new message

#     return render(request, 'chat.html', {'chat_room': chat_room})




from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, Message
from django.utils import timezone

# View for the chat room
@login_required
def chat_room_view(request, chatroom_id):
    # Retrieve the chat room based on the chatroom_id
    chat_room = get_object_or_404(ChatRoom, id=chatroom_id)

    # Check if the logged-in user is either the buyer or the seller in the chat
    if request.user not in [chat_room.buyer, chat_room.seller]:
        return HttpResponseForbidden("You are not part of this chat room.")

    # If the form is submitted, create a new message
    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            # Create a new message and associate it with the chat room and sender
            new_message = Message.objects.create(
                chat_room=chat_room,
                sender=request.user,
                content=message_content,
                sent_at=timezone.now()
            )
            # After the message is sent, redirect to the same chat room to view the new message
            return redirect('chat-room', chatroom_id=chatroom_id)

    # If GET request, render the chat room and its messages
    return render(request, 'chat.html', {'chat_room': chat_room})
