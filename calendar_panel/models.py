# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from user_panel.models import CompanyInfoModel
from person_panel.models import PersonIDInfoModel
import re

class EventInfoModel(models.Model):
    type_list=(('0','Doğum Günü'),('1','Toplantı'),('2','Diğer'))
    name=models.CharField(max_length=30,default='Adsız Etkinlik')
    start_time=models.DateTimeField(default='')
    end_time=models.DateTimeField(null=True,blank=True)
    all_day=models.NullBooleanField()
    place=models.CharField(max_length=100,null=True,blank=True)
    type=models.CharField(max_length=10,choices=type_list,null=True,blank=True)
    desc=models.CharField(max_length=200,null=True,blank=True)
    company=models.ForeignKey(CompanyInfoModel,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        db_table='event_info'

    def __str__(self):
        return self.name

    def type_name(self):
        return dict(self.type_list)[self.type]

    def person(self):
        person=re.search('[0-9]+',self.desc).groups()[0]
        if PersonIdInfoModel.objects.get(pk=person,company=self.company_id):
            return PersonIdInfoModel.objects.get(pk=person,company=self.company_id)
        else:
            return None