# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from person_panel.models import StudentInfoModel,PersonalInfoModel
from user_panel.models import CompanyInfoModel

def get_time():
    return datetime.datetime.now()

def get_date():
    return datetime.date.today()

class StudentLeaveModel(models.Model):
    person=models.ForeignKey(StudentInfoModel)
    start=models.DateField()
    end=models.DateField(blank=True,null=True)
    reason=models.CharField(max_length=100,blank=True,null=True)
    company_id=models.ForeignKey(CompanyInfoModel,default='')

    class Meta:
        db_table='student_leave'

    def __str__(self):
        return  str(self.person.full_name())+' - '+ str(self.reason)


class AttendanceInfoModel(models.Model):
    person=models.ForeignKey(StudentInfoModel)
    time=models.DateTimeField(default=get_time)
    in_or_out=models.BooleanField(max_length=1)
    company_id=models.ForeignKey(CompanyInfoModel,default='')

    class meta:
        db_table='attendance_info'

    def __str__(self):
        return str(self.person)+' - '+ str(self.time)+ ' - '+ str(self.in_or_out)

    def in_or_out_name(self):
        if self.in_or_out==True:
            return 'İçeri Girdi'
        else:
            return 'Dışarı Çıktı'

class VacationInfoModel(models.Model):
    person=models.ForeignKey(PersonalInfoModel)
    start_day=models.DateField()
    end_day=models.DateField(null=True,blank=True)
    reason=models.CharField(max_length=100,blank=True,null=True)
    company_id=models.ForeignKey(CompanyInfoModel,default='')

    class Meta:
        db_table='vacation_info'

    def __str__(self):
        return self.person.full_name()+self.reason


class CityInfoModel(models.Model):
    city_name = models.CharField(max_length=50, blank=False)
    city_slug = models.CharField(max_length=50, blank=False)
    class Meta:
        db_table='adres_city'

class TownInfoModel(models.Model):
    city = models.ForeignKey(CityInfoModel)
    town_name = models.CharField(max_length=50, blank=False)
    town_slug = models.CharField(max_length=50, blank=False)
    class Meta:
        db_table='adres_town'

class NeighborhoodInfoModel(models.Model):
    town = models.ForeignKey(TownInfoModel)
    neighborhood_name = models.CharField(max_length=100, blank=False)
    neighborhood_slug = models.CharField(max_length=100, blank=False)
    class Meta:
        db_table='adres_neigh'

class PostalCodeInfoModel(models.Model):
    neighborhood =models.ForeignKey(NeighborhoodInfoModel)
    pk_name = models.CharField(max_length=100, blank=False)
    pk_slug = models.CharField(max_length=100, blank=False)
    postal_code = models.CharField(max_length=30, blank=False)
    class Meta:
        db_table='adres_postal'