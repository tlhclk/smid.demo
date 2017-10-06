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
    document_type_list=[('1','Kimlik Kartı'),('2','Sigorta'),('3','Fatura'),('4','İzin Kağıdı'),('5','Öğrenci Sertifikası'),]
    id=models.CharField(max_length=10,primary_key=True,verbose_name='Document Id: ',default='')
    person=models.ForeignKey(StudentInfoModel,verbose_name='Person id: ')
    date=models.DateField(default=get_date,verbose_name='Document Record Date: ',max_length=10)
    type=models.CharField(max_length=20,verbose_name='Document Type: ',choices=document_type_list)
    desc=models.CharField(max_length=100,verbose_name='Documnet Description: ',default='')
    image_field=models.ImageField(default='',upload_to='document_image/',verbose_name='Documnet Image or Scan',max_length=100,blank=True)
    company_id=models.ForeignKey(CompanyInfoModel,default='')

    class Meta:# TODO: db_table adı düzenlenecek
        db_table='documnet_info'

    def __str__(self):
        return str(self.type_name())+' - '+ str(self.person_name())

    def type_name(self):
        return dict(self.document_type_list)[self.type]

    def person_name(self):
        return StudentInfoModel.objects.get(pk=self.person).full_name() or PersonalInfoModel.objects.get(pk=self.person).full_name()

    def person_list(self):
        return StudentInfoModel.objects.all()


class LiabilityInfoModel(models.Model):
    fixture_type_list = [('1', 'Baza'), ('2', 'Yatak'), ('3', 'Dolap'), ('4', 'Halı'), ('5', 'Komodin'),
                         ('6', 'Tül'), ('7', 'Perde'), ('8', 'Masa'), ('9', 'Sandalye'), ('10', 'Askılık'),
                         ('11', 'Kitaplık'), ('12', 'Lamba'), ('13', 'Klima'), ('14', 'Ayna')]# TODO: liste düzenlenecek
    #record_no=models.CharField(max_length=10,verbose_name='Record No: ',primary_key=True,default='1')
    person=models.ForeignKey(StudentInfoModel,verbose_name='Person Id: ',unique=False)
    type=models.CharField(max_length=50,verbose_name='Liability Type: ',choices=fixture_type_list)
    desc=models.CharField(max_length=100,verbose_name='Liability Description: ',default='',blank=True)
    give_day=models.DateTimeField(default='',verbose_name='Liability Day',max_length=20)
    last_day=models.DateTimeField(blank=True,verbose_name='Liability Last day',max_length=20,null=True)
    take_day=models.DateTimeField(blank=True,verbose_name='Liability Return day',null=True)
    penalty=models.CharField(max_length=30,blank=True,default='')
    company_id = models.ForeignKey(CompanyInfoModel, default='None')

    class Meta:
        db_table='liability_info'

    def __str__(self):
        return str(self.person.full_name()) + ' - '+ str(self.type_name())

    def fixture_type_name(self):
        return dict(self.fixture_type_list)[self.type]

    def person_list(self):
        return StudentInfoModel.objects.all()

    def type_name(self):
        return dict(self.fixture_type_list)[self.type]

