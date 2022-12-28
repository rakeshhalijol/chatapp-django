"""
ASGI config for chatdata project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.routing import URLRouter,ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path
from main.consumers import DetialConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatdata.settings')

application = get_asgi_application()

wspatterns = [
    path("ws/chat/",DetialConsumer.as_asgi())

]

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(URLRouter(wspatterns))
})


