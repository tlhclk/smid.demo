# -*- coding: utf-8 -*-
from django.db import models
import datetime
from user_panel.models import CompanyInfoModel

class RoomInfoModel(models.Model):
    room_people_list=[('1','Tek Kişilik'),('2','İki Kişilik'),('3','Üç Kişilik'),('4','Dört Kişilik'),('5','Beş Kişilik')]
    room_type_list=[('1','Duşakabin'),('2','Ranzalı'),('3','Normal'),('4','Mutfaklı')]
    room_no=models.CharField(max_length=4,verbose_name='Room No: ')
    room_floor=models.CharField(max_length=2,verbose_name='Room Floor: ',default='')
    room_people=models.CharField(max_length=2,choices=room_people_list,verbose_name='Room People: ')
    room_type=models.CharField(max_length=20,choices=room_type_list,verbose_name='Room Type: ')
    room_desc=models.CharField(max_length=100,verbose_name='Room Description',blank=True,default='',null=True)
    room_image=models.ImageField(upload_to='room_image/',blank=True,verbose_name='Room Image: ',default='')
    company_id = models.ForeignKey(CompanyInfoModel, default='')

    class Meta:
        db_table='room_info'

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)

    def room_people_name(self):
        return self.room_people_list[int(self.room_people)-1][1]

    def room_type_name(self):
        return self.room_type_list[int(self.room_type)-1][1]

    def check_room_image(self):
        print (self.room_image.path)

class FixtureInfoModel(models.Model):
    fixture_type_list = [('1', 'Baza'), ('2', 'Yatak'), ('3', 'Dolap'), ('4', 'Halı'), ('5', 'Komodin'),
                         ('6', 'Tül'), ('7', 'Perde'), ('8', 'Masa'), ('9', 'Sandalye'), ('10', 'Askılık'),
                         ('11', 'Kitaplık'), ('12', 'Lamba'), ('13', 'Klima'), ('14', 'Ayna')]
    fixture_no = models.CharField(max_length=10,primary_key=True,verbose_name='Fixture No: ')
    room_id=models.ForeignKey(RoomInfoModel,unique=False,verbose_name='Room No: ',default='')
    #room_no=models.CharField(max_length=10,blank=True,null=True)
    fixture_type=models.CharField(max_length=20,choices=fixture_type_list,verbose_name='Fixture Type:')
    fixture_notes=models.CharField(max_length=100,default='',blank=True, verbose_name='Fixture Notes: ')
    fixture_image = models.ImageField(upload_to='fixture_image/', blank=True,verbose_name='Fixture Image: ',default='')
    company_id=models.ForeignKey(CompanyInfoModel,default='')

    class Meta:
        db_table='fixture_info'

    def __str__(self):
        return self.fixture_no

    def fixture_type_name(self):
        return self.fixture_type_list[int(self.fixture_type)-1][1]


