# channels library를 활용해서 socket 연결하는 비동기 route 구현
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns) # ws://127.0.0.1:8000/ws/{room_id}
    )
})