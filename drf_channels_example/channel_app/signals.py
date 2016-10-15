import json

import re

from channels import Group


def send_message(sender, instance, **kwargs):
    from channel_app.serializers import UserMessageGetSerializer
    data = json.dumps(UserMessageGetSerializer(instance).data)

    if instance.room:
        room_label = instance.room.label
        room_label = re.sub('\s+', '_', room_label).lower()
        Group(room_label).send({'text': data})
    else:
        Group(instance.room.label).send({'text': data})
