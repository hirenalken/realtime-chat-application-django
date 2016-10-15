from channel_app.custom_exceptions import ValidationException
from channel_app.models import User
from channel_app.serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token


def fetch_token(user):
    try:
        # Get the goal for the specified user and return key
        token = Token.objects.get(user_id=user.id)
        token_key = token.key
    except Token.DoesNotExist:
        # If token is not found then generate token
        token_key = generate_token(user)
    return token_key


def generate_token(user):
    token = Token.objects.create(user=user)
    # Return only the key with is associated with the object
    return token.key


def check_user_exists_for_login(username):
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        raise ValidationException({"message": "User with username %s does not exists." % username},
                                  status=status.HTTP_404_NOT_FOUND)


def authenticate_user(username, password, user):
    user = authenticate(username=username, password=password)
    if user:
        serializer = UserSerializer(user)
        serializer_dict = serializer.data
        serializer_dict["message"] = "Login successful"
        serializer_dict["token"] = fetch_token(user)
        # serializer_dict['Integrations'] = get_all_active_integrations(user)
        return serializer_dict
    else:
        raise ValidationException({"message": "Invalid password"},
                                  status=status.HTTP_401_UNAUTHORIZED
                                  )