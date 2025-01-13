# chat_app/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import ChatMessage

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.receiver_id = self.scope['url_route']['kwargs']['user_id']
        self.room_group_name = f"chat_{min(self.user.id, self.receiver_id)}_{max(self.user.id, self.receiver_id)}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Send old messages
        messages = ChatMessage.objects.filter(
            sender__id__in=[self.user.id, self.receiver_id],
            receiver__id__in=[self.user.id, self.receiver_id]
        ).order_by('timestamp')
        
        for message in messages:
            await self.send(text_data=json.dumps({
                'sender': message.sender.username,
                'message': message.message,
            }))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Save the message to the database
        receiver = User.objects.get(id=self.receiver_id)
        ChatMessage.objects.create(sender=self.user, receiver=receiver, message=message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sender': self.user.username,
                'message': message
            }
        )

    async def chat_message(self, event):
        sender = event['sender']
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'sender': sender,
            'message': message
        }))
