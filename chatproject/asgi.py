"""
ASGI config for chatproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack
from chatapp.consumers import EchoConsumer,ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproject.settings')

application = ProtocolTypeRouter({
        'http':get_asgi_application(),
        'websocket':AuthMiddlewareStack( 
            URLRouter([
                path('ws/chat/',EchoConsumer.as_asgi()),
                path('ws/chat/<str:uid>/',ChatConsumer.as_asgi())
            ])
        )
     })
