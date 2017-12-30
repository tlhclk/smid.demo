# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from user_panel.models import CompanyInfoModel

# Create your models here.

class EventInfoModel(models.Model):
    type_list=[('0','Doğum Günü'),('1','Toplantı'),('2','Diğer')]
    name=models.CharField(max_length=30,default='')
    start_time=models.DateTimeField(default='')
    end_time=models.DateTimeField(default='')
    all_day=models.NullBooleanField()
    place=models.CharField(max_length=100,null=True,blank=True)
    type=models.CharField(max_length=10,choices=type_list,null=True,blank=True)
    desc=models.CharField(max_length=200,null=True,blank=True)
    company_id=models.ForeignKey(CompanyInfoModel,default='',on_delete=models.CASCADE)

    class Meta:
        db_table='event_info'

    def __str__(self):
        return self.name

    def type_name(self):
        return dict(self.type_list)[self.type]