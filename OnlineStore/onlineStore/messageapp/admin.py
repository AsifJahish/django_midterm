from django.contrib import admin

# Register your models here.
from .models import ChatRoom
from .models import Message


admin.site.register(ChatRoom)
admin.site.register(Message)