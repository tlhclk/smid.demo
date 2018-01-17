# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import FixtureInfoModel,RoomInfoModel

from django.contrib import admin

admin.site.register(FixtureInfoModel)
admin.site.register(RoomInfoModel)