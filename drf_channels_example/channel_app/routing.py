from channel_app.consumers import ws_message, websocket_connect, websocket_keepalive, websocket_disconnect
from channels.routing import route
# channel_routing = [
#     route("http.request", "channel_app.consumers.http_consumer"),
# ]

channel_routing = [
    route("websocket.receive", ws_message),
    route("websocket.connect", websocket_connect),
    route("websocket.keepalive", websocket_keepalive),
    route("websocket.disconnect", websocket_disconnect)
]

# channel_routing = {
#     "websocket.connect": "channel_app.consumers.websocket_connect",
#     "websocket.keepalive": "channel_app.consumers.websocket_keepalive",
#     "websocket.disconnect": "channel_app.consumers.websocket_disconnect"
# }