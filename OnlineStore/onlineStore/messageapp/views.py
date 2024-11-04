from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, Message
from .forms import MessageForm

# messageapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import ChatRoom, Message
from .forms import MessageForm
from userApp.models import User  # Import your User model if needed

def chat_room(request, seller_id):
    buyer = request.user
    seller = get_object_or_404(User, id=seller_id, is_seller=True)
    
    # Check if a chat room already exists
    chat_room, created = ChatRoom.objects.get_or_create(buyer=buyer, seller=seller)
    
    # Handle the message form submission
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_room = chat_room
            message.sender = buyer  # Assuming the buyer initiates the message
            message.save()
            return redirect('chat_room', seller_id=seller_id)
    else:
        form = MessageForm()
    
    messages = Message.objects.filter(chat_room=chat_room).order_by('created_at')
    
    return render(request, 'messageapp/chat_room.html', {
        'chat_room': chat_room,
        'messages': messages,
        'form': form,
    })

@login_required
def send_message(request, chat_room_id):
    if request.method == "POST":
        chat_room = get_object_or_404(ChatRoom, id=chat_room_id)
        content = request.POST.get("content")
        if content:
            Message.objects.create(chat_room=chat_room, sender=request.user, content=content)
        return redirect('chat_room', chat_room_id=chat_room_id)
