# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User,CompanyInfoModel
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


admin.site.register(User,UserAdmin)
admin.site.register(CompanyInfoModel)