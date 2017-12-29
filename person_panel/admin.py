# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import StudentInfoModel,PersonIDInfoModel,PersonalInfoModel,ParentInfoModel
from django.contrib import admin

admin.site.register(PersonIDInfoModel)
admin.site.register(PersonalInfoModel)
admin.site.register(StudentInfoModel)
admin.site.register(ParentInfoModel)
