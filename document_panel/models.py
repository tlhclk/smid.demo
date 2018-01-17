# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from person_panel.models import StudentInfoModel,PersonalInfoModel
import datetime
from user_panel.models import CompanyInfoModel


def get_time():
    return datetime.datetime.now()

def get_date():
    return datetime.date.today()

class DocumentInfoModel(models.Model):
    document_type_list=(('1','Kimlik Kartı'),('2','Sigorta'),('3','Fatura'),('4','İzin Kağıdı'),('5','Öğrenci Sertifikası'))
    person=models.ForeignKey(StudentInfoModel,on_delete=models.CASCADE)
    date=models.DateField(max_length=10,null=True,blank=True)
    type=models.CharField(max_length=20,choices=document_type_list)
    desc=models.CharField(max_length=100,null=True,blank=True)
    image_field=models.ImageField(upload_to='document_image/',max_length=100)
    company=models.ForeignKey(CompanyInfoModel,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        db_table='document_info'

    def __str__(self):
        return str(self.type_name())+' - '+ str(self.person_name())

    def type_name(self):
        return dict(self.document_type_list)[self.type]

    def person_name(self):
        return StudentInfoModel.objects.get(pk=self.person).full_name() or PersonalInfoModel.objects.get(pk=self.person).full_name()

    def person_list(self):
        return StudentInfoModel.objects.all()


class LiabilityInfoModel(models.Model):
    fixture_type_list = (('1', 'Baza'), ('2', 'Yatak'), ('3', 'Dolap'), ('4', 'Halı'), ('5', 'Komodin'),
                         ('6', 'Tül'), ('7', 'Perde'), ('8', 'Masa'), ('9', 'Sandalye'), ('10', 'Askılık'),
                         ('11', 'Kitaplık'), ('12', 'Lamba'), ('13', 'Klima'), ('14', 'Ayna'))
    person=models.ForeignKey(StudentInfoModel,unique=False,on_delete=models.CASCADE)
    type=models.CharField(max_length=50,choices=fixture_type_list)
    desc=models.CharField(max_length=100,default='',blank=True)
    give_day=models.DateTimeField(default=get_time,max_length=20)
    last_day=models.DateTimeField(blank=True,max_length=20,null=True)
    take_day=models.DateTimeField(blank=True,null=True)
    penalty=models.CharField(max_length=30,blank=True,default='0.0')
    company = models.ForeignKey(CompanyInfoModel,on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        db_table='liability_info'

    def __str__(self):
        return str(self.person.full_name()) + ' - '+ str(self.type_name())

    def fixture_type_name(self):
        return dict(self.fixture_type_list)[self.type]

    def type_name(self):
        return dict(self.fixture_type_list)[self.type]

