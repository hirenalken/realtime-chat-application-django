from channel_app.custom_exceptions import ValidationException
from channel_app.models import User, UserMessage, Room
from channel_app.serializers import UserSerializer, UserMessageSerializer, UserMessageGetSerializer, RoomSerializer, \
    UserProfileSerializer
from channel_app.utils import check_user_exists_for_login, authenticate_user

from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


class UserRegistrationView(APIView):
    def post(self, request, **kwargs):

        # Validate request first
        user, token = User.objects.create_user(request.data['username'], request.data['password'])
        user.full_name = request.data["full_name"]
        user.save()
        return_data = {'user_id': user.id, 'token': token}
        return Response(return_data, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    def post(self, request, **kwargs):
        try:
            username = request.data['username']
            password = request.data['password']
        except KeyError:
            return Response(
                {"message": "username and password is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            user = check_user_exists_for_login(username)
            data = authenticate_user(username, password, user)
            return Response(data, status=status.HTTP_200_OK)
        except ValidationException as e:
            return Response(e.errors, e.message)


class UsersDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UserMessageView(mixins.CreateModelMixin,
                      generics.GenericAPIView):

    serializer_class = UserMessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = UserMessage.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserMessageListView(mixins.ListModelMixin,
                          generics.GenericAPIView):

    serializer_class = UserMessageGetSerializer
    permission_classes = (IsAuthenticated,)
    queryset = UserMessage.objects.all()

    def get(self, request, *args, **kwargs):

        # if 'campaign_id' in query_params:
        #     # TODO HIREN
        #     # Check given campaign id is valid or not
        #     self.queryset = self.queryset.filter(campaign_id=query_params['campaign_id'])
        return self.list(request, *args, **kwargs)


class RoomDetailView(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     generics.GenericAPIView):

    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Room.objects.all()

    def post(self, request, *args, **kwargs):
        request.data['owner'] = request.user.id
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserListView(mixins.ListModelMixin,
                   generics.GenericAPIView):

    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)