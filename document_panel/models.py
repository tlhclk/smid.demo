# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from person_panel.models import StudentInfoModel,PersonalInfoModel
import datetime

class DocumentInfoModel(models.Model):
    document_type_list=[('1','ID Card'),('2','Insurance'),('3','Bill'),('4','Leave Doc.'),('5','Student Certificate'),]
    document_id=models.CharField(max_length=10,primary_key=True,verbose_name='Document Id: ')
    #person_id=models.CharField(max_length=7,verbose_name='Person Id: ',null=False)
    person_id=models.ForeignKey(StudentInfoModel,verbose_name='Person id: ')
    document_date=models.DateField(default=datetime.date.today,verbose_name='Document Record Date: ')
    document_type=models.CharField(max_length=20,verbose_name='Document Type: ',null=False,choices=document_type_list)
    document_description=models.CharField(max_length=100,verbose_name='Documnet Description: ',blank=True)
    document_image=models.ImageField(default='Desktop/asd.jpg',upload_to='document_image/',verbose_name='Documnet Image or Scan',max_length=100)

    class Meta:
        db_table='documnet_info'

    def __str__(self):
        return self.document_id

    def document_type_name(self):
        return self.document_type_list[int(self.document_type)-1][1]

    def person_id_name(self):
        return StudentInfoModel.objects.get(pk=self.person_id).full_name() or PersonalInfoModel.objects.get(pk=self.person_id).full_name()

class LiabilityInfoModel(models.Model):
    fixture_type_list = [('1', 'Box Spring'), ('2', 'Bed'), ('3', 'Wardrobe'), ('4', 'Carpet'), ('5', 'Night Stand'),
                         ('6', 'Tulle'), ('7', 'Veil'), ('8', 'Table'), ('9', 'Chair'), ('10', 'Coat Hanger'),
                         ('11', 'Bookcase'), ('12', 'Lamp'), ('13', 'Klima'), ('14', 'Mirror')]
    record_no=models.CharField(max_length=10,verbose_name='Record No: ',primary_key=True,default='1')
    person_id=models.ForeignKey(StudentInfoModel,verbose_name='Person Id: ',null=False,unique=False)
    #person_id=models.CharField(max_length=10,blank=True,null=True)
    liability_type=models.CharField(max_length=50,verbose_name='Liability Type: ',choices=fixture_type_list)
    liability_name=models.CharField(max_length=50,verbose_name='Liability Name: ')
    liability_desc=models.CharField(max_length=100,verbose_name='Liability Description: ')
    liability_date=models.DateField(default=datetime.date.today,verbose_name='Liability Day')
    liability_lastday=models.DateField(null=True,blank=True,verbose_name='Liability Last day',default=datetime.datetime.today()+datetime.timedelta(days=7))
    liability_return=models.DateField(blank=True,null=True,verbose_name='Liability Return day')
    liability_penalty=models.CharField(max_length=30,blank=True,null=True)


    class Meta:
        db_table='liability_info'

    def __str__(self):
        return self.record_no

