# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import DocumentInfoModel,LiabilityInfoModel
from django.contrib import admin

admin.site.register(DocumentInfoModel)
admin.site.register(LiabilityInfoModel)
