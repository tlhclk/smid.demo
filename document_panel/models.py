# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from person_panel.models import StudentInfoModel,PersonalInfoModel
import datetime

def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class DocumentInfoModel(models.Model):
    document_type_list=[('1','Kimlik Kartı'),('2','Sigorta'),('3','Fatura'),('4','İzin Kağıdı'),('5','Öğrenci Sertifikası'),]
    document_id=models.CharField(max_length=10,primary_key=True,verbose_name='Document Id: ',default='')
    #person_id=models.CharField(max_length=7,verbose_name='Person Id: ',null=False)
    person_id=models.ForeignKey(StudentInfoModel,verbose_name='Person id: ')
    document_date=models.DateTimeField(default=get_time,verbose_name='Document Record Date: ')
    document_type=models.CharField(max_length=20,verbose_name='Document Type: ',choices=document_type_list)
    document_description=models.CharField(max_length=100,verbose_name='Documnet Description: ',default='')
    document_image=models.ImageField(default='',upload_to='document_image/',verbose_name='Documnet Image or Scan',max_length=100)

    class Meta:
        db_table='documnet_info'

    def __str__(self):
        return self.document_id

    def document_type_name(self):
        return dict(self.document_type_list)[self.document_type]

    def person_id_name(self):
        return StudentInfoModel.objects.get(pk=self.person_id).full_name() or PersonalInfoModel.objects.get(pk=self.person_id).full_name()

    def person_list(self):
        return StudentInfoModel.objects.all()

class LiabilityInfoModel(models.Model):
    fixture_type_list = [('1', 'Baza'), ('2', 'Yatak'), ('3', 'Dolap'), ('4', 'Halı'), ('5', 'Komodin'),
                         ('6', 'Tül'), ('7', 'Perde'), ('8', 'Masa'), ('9', 'Sandalye'), ('10', 'Askılık'),
                         ('11', 'Kitaplık'), ('12', 'Lamba'), ('13', 'Klima'), ('14', 'Ayna')]
    #record_no=models.CharField(max_length=10,verbose_name='Record No: ',primary_key=True,default='1')
    person_id=models.ForeignKey(StudentInfoModel,verbose_name='Person Id: ',unique=False)
    #person_id=models.CharField(max_length=10,blank=True,null=True)
    liability_type=models.CharField(max_length=50,verbose_name='Liability Type: ',choices=fixture_type_list)
    #liability_name=models.CharField(max_length=50,verbose_name='Liability Name: ',default='')
    liability_desc=models.CharField(max_length=100,verbose_name='Liability Description: ',default='')
    liability_date=models.DateTimeField(default=get_time,verbose_name='Liability Day')
    liability_lastday=models.DateTimeField(blank=True,verbose_name='Liability Last day',default=get_time)
    liability_return=models.DateTimeField(blank=True,verbose_name='Liability Return day')
    liability_penalty=models.CharField(max_length=30,blank=True,default='')

    class Meta:
        db_table='liability_info'

    def __str__(self):
        return self.id

    def fixture_type_name(self):
        return dict(self.fixture_type_list)[self.liability_type]

    def person_list(self):
        return StudentInfoModel.objects.all()

    def liability_type_name(self):
        return dict(self.fixture_type_list)[self.liability_type]

