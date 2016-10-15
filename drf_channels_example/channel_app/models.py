from __future__ import unicode_literals

from channel_app.signals import send_message
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):

    def create_user(self, username, password=None):

        if not username:
            raise ValueError("User must have an username")

        user = self.model(
            # email=self.normalize_email(email),
            username=username)
        user.set_password(password)
        user.save(using=self._db)
        token = Token.objects.create(user=user)
        return user, token.key


class User(AbstractBaseUser):

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass

    class Meta:
        db_table = 'users'
        managed = True

    full_name = models.CharField(max_length=255, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    username = models.CharField(max_length=255, unique=True, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __unicode__(self):
        return self.username


class UserMessage(models.Model):
    class Meta:
        db_table = 'user_messages'
        managed = True

    from_user = models.ForeignKey(User, related_name='from_user')
    to_user = models.ForeignKey(User, related_name='to_user')
    message = models.TextField()
    room = models.ForeignKey('Room',null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

# signals registrations
post_save.connect(send_message, sender=UserMessage)


class Room(models.Model):
    class Meta:
        db_table = 'rooms'
        managed = True

    label = models.CharField(max_length=200)
    owner = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)