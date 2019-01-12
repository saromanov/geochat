from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    fields = ['text', 'user_id', 'geometry']

admin.site.register(Message, MessageAdmin)
