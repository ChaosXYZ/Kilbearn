from django.urls import path
from django.conf.urls import url, include

from . import consumers

websocket_urlpatterns = [
    url(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]
