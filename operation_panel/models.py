# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from person_panel.models import StudentInfoModel
from user_panel.models import CompanyInfoModel

def get_time():
    return datetime.datetime.now()

def get_date():
    return datetime.date.today()

class StudentLeaveModel(models.Model):
    person_id=models.ForeignKey(StudentInfoModel,verbose_name='Permitted Person: ')
    #person_id=models.CharField(max_length=10,blank=True,null=True)
    leave_start=models.DateField(verbose_name='leave Start: ',default=get_date)
    leave_end=models.DateField(verbose_name='leave End: ',default=get_date)
    leave_reason=models.CharField(max_length=100,verbose_name='leave Reason: ',blank=True,default='',null=True)
    company_id=models.ForeignKey(CompanyInfoModel,default='')

    class Meta:
        db_table='student_leave'

    def __str__(self):
        return  str(self.id)


class AttendanceInfoModel(models.Model):
    person_id=models.ForeignKey(StudentInfoModel,verbose_name='Person: ')
    #person_id=models.CharField(max_length=10,blank=True,null=True)
    traffic_date=models.DateTimeField(default=get_time)
    in_or_out=models.BooleanField(max_length=1,verbose_name='In or Out: ')
    company_id=models.ForeignKey(CompanyInfoModel,default='')

    class meta:
        db_table='attendance_info'

    def __str__(self):
        return self.id