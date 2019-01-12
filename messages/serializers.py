from rest_framework import serializers
from .model import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'user_id', 'text', 'geometry')