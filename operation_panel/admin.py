# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import StudentLeaveModel,AttendanceInfoModel,VacationInfoModel,NotificationInfoModel,CityInfoModel,TownInfoModel,NeighborhoodInfoModel,PostalCodeInfoModel
from django.contrib import admin

admin.site.register(StudentLeaveModel)
admin.site.register(AttendanceInfoModel)
admin.site.register(VacationInfoModel)
admin.site.register(NotificationInfoModel)
admin.site.register(CityInfoModel)
admin.site.register(TownInfoModel)
admin.site.register(NeighborhoodInfoModel)
admin.site.register(PostalCodeInfoModel)
