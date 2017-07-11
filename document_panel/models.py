# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from person_panel.models import StudentInfoModel,PersonalInfoModel
import datetime

class DocumentInfoModel(models.Model):
    document_type_list=[('01','ID Card'),('02','Insurance'),('03','Bill'),('04','Leave Doc.'),('05','Student Certificate'),]
    document_id=models.CharField(max_length=10,primary_key=True,verbose_name='Document Id: ')
    #person_id=models.CharField(max_length=7,verbose_name='Person Id: ',null=False)
    person_id=models.ForeignKey(StudentInfoModel,verbose_name='Person id: ')
    document_date=models.DateField(default=datetime.date.today,verbose_name='Document Record Date: ')
    document_type=models.CharField(max_length=20,verbose_name='Document Type: ',null=False,choices=document_type_list)
    document_description=models.CharField(max_length=100,verbose_name='Documnet Description: ',blank=True)
    document_image=models.ImageField(default='Desktop/asd.jpg',upload_to='document_image/',verbose_name='Documnet Image or Scan')

    class Meta:
        db_table='documnet_info'

    def __str__(self):
        return self.document_id

    def document_type_name(self):
        return self.document_type_list[int(self.document_type)-1][1]

    def person_id_name(self):
        return StudentInfoModel.objects.get(pk=self.person_id).full_name() or PersonalInfoModel.objects.get(pk=self.person_id).full_name()
