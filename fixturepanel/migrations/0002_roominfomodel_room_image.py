# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixturepanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roominfomodel',
            name='room_image',
            field=models.ImageField(default=None, null=True, upload_to=b'room_image/'),
        ),
    ]
