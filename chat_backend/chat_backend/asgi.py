# chat_backend/asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat_app import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_backend.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/chat/<int:user_id>/", consumers.ChatConsumer.as_asgi()),
        ])
    ),
})
