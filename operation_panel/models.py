# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from person_panel.models import StudentInfoModel

def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class StudentLeaveModel(models.Model):
    person_list=[]
    #leave_id=models.CharField(max_length=10,primary_key=True,verbose_name='leave_id: ')
    person_id=models.ForeignKey(StudentInfoModel,verbose_name='Permitted Person: ')
    #person_id=models.CharField(max_length=10,blank=True,null=True)
    leave_start=models.DateTimeField(verbose_name='leave Start: ',default=get_time)
    leave_end=models.DateTimeField(verbose_name='leave End: ',default='2017-07-05')
    leave_reason=models.CharField(max_length=100,verbose_name='leave Reason: ',blank=True)

    class Meta:
        db_table='student_leave'

    def __str__(self):
        return  str(self.id)

class AttendanceInfoModel(models.Model):
    person_id=models.ForeignKey(StudentInfoModel,verbose_name='Person: ')
    #person_id=models.CharField(max_length=10,blank=True,null=True)
    traffic_date=models.DateTimeField(default=get_time)
    in_or_out=models.CharField(max_length=1,verbose_name='In or Out: ')

    class meta:
        db_table='attendance_info'

    def __str__(self):
        return self.id