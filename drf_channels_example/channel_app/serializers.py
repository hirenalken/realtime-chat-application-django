from channel_app.models import User, UserMessage, Room
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'users'
        model = User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'users'
        model = User
        fields = ('id', 'full_name', 'username')


class UserMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserMessage
        db_table = 'user_messages'


class UserMessageGetSerializer(serializers.ModelSerializer):
    from_user = UserProfileSerializer()

    class Meta:
        model = UserMessage
        db_table = 'user_messages'


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room