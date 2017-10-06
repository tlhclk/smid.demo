# -*- coding: utf-8 -*-
from django.db import models
import datetime
from user_panel.models import CompanyInfoModel

class RoomInfoModel(models.Model):
    room_people_list=[('1','Tek Kişilik'),('2','İki Kişilik'),('3','Üç Kişilik'),('4','Dört Kişilik'),('5','Beş Kişilik')]
    room_type_list=[('1','Duşakabin'),('2','Ranzalı'),('3','Normal'),('4','Mutfaklı')]
    id=models.CharField(max_length=10,verbose_name='room ID',primary_key=True)
    no=models.CharField(max_length=4,verbose_name='Room No: ')
    floor=models.CharField(max_length=2,verbose_name='Room Floor: ',default='')
    people=models.CharField(max_length=2,choices=room_people_list,verbose_name='Room People: ')
    type=models.CharField(max_length=20,choices=room_type_list,verbose_name='Room Type: ')
    desc=models.CharField(max_length=100,verbose_name='Room Description',blank=True,default='',null=True)
    image_field=models.ImageField(upload_to='room_image/',blank=True,verbose_name='Room Image: ',default='')
    company_id = models.ForeignKey(CompanyInfoModel, default='')

    class Meta:
        db_table='room_info'

    def __str__(self):
        return str(self.no)

    def __unicode__(self):
        return str(self.id)

    def people_name(self):
        return self.room_people_list[int(self.people)-1][1]

    def type_name(self):
        return self.room_type_list[int(self.type)-1][1]

    def check_image(self):
        print (self.image_field.path)

class FixtureInfoModel(models.Model):
    fixture_type_list = [('1', 'Baza'), ('2', 'Yatak'), ('3', 'Dolap'), ('4', 'Halı'), ('5', 'Komodin'),
                         ('6', 'Tül'), ('7', 'Perde'), ('8', 'Masa'), ('9', 'Sandalye'), ('10', 'Askılık'),
                         ('11', 'Kitaplık'), ('12', 'Lamba'), ('13', 'Klima'), ('14', 'Ayna')]
    no = models.CharField(max_length=10,primary_key=True,verbose_name='Fixture No: ')
    room=models.ForeignKey(RoomInfoModel,unique=False,verbose_name='Room No: ',default='')
    type=models.CharField(max_length=20,choices=fixture_type_list,verbose_name='Fixture Type:')
    notes=models.CharField(max_length=100,default='',blank=True, verbose_name='Fixture Notes: ')
    image_field = models.ImageField(upload_to='fixture_image/', blank=True,verbose_name='Fixture Image: ',default='')
    company_id=models.ForeignKey(CompanyInfoModel,default='')

    class Meta:
        db_table='fixture_info'

    def __str__(self):
        return ('%s - %s'%(self.no,self.type_name()))

    def type_name(self):
        return self.fixture_type_list[int(self.type)-1][1]


