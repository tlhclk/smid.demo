# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User,CompanyInfoModel
from django.contrib import admin

admin.site.register(User)
admin.site.register(CompanyInfoModel)
