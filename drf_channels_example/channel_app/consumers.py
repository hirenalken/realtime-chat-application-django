import json

from channels import Group
from channels.sessions import channel_session
from django.http import HttpResponse
from channels.handler import AsgiHandler


# def http_consumer(message):
#     # Make standard HTTP response - access ASGI path attribute directly
#     response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
#     # Encode that response into message format (ASGI)
#     for chunk in AsgiHandler.encode_response(response):
#         message.reply_channel.send(chunk)
from drf_channels_example.settings import LOG


# @channel_session
def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    # print(message.content)

    # message.reply_channel.send({
    #     "text": message.content['text'],
    # })
    # try:
    #     prefix, room_label = message.content['path'].decode('ascii').strip('/').split('/')
    #     if prefix != 'direct_chat':
    #         LOG.debug('invalid ws path=%s', message.content['path'])
    #         return
    # except ValueError:
    #     LOG.debug('invalid ws path=%s', message.content['path'])
    #     return
    # data = {
    #
    # }
    pass


# Connected to websocket.connect and websocket.keepalive
@channel_session
def websocket_connect(message):
    try:
        prefix, room_label = message['path'].decode('ascii').strip('/').split('/')
        if prefix != 'direct_chat':
            LOG.debug('invalid ws path=%s', message['path'])
            return
    except ValueError:
        LOG.debug('invalid ws path=%s', message['path'])
        return
    print(room_label)
    Group(room_label).add(message.reply_channel)

    # message.reply_channel.send({
    #     "text": "connected",
    # })


# Connected to websocket.keepalive
def websocket_keepalive(message):
    message.reply_channel.send({
        "text": "alive",
    })


# Connected to websocket.disconnect
def websocket_disconnect(message):
    message.reply_channel.send({
        "text": "disconnected",
    })