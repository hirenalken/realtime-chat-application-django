# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('channel_app', '0004_usermessage_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='channel_app.Room'),
        ),
    ]
