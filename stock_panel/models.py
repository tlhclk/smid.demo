# -*- coding: utf-8 -*-
from django.db import models
import datetime
from user_panel.models import CompanyInfoModel

class RoomInfoModel(models.Model):
    room_people_list=[('1','Tek Kişilik'),('2','İki Kişilik'),('3','Üç Kişilik'),('4','Dört Kişilik'),('5','Beş Kişilik')]
    room_type_list=[('1','Duşakabin'),('2','Ranzalı'),('3','Normal'),('4','Mutfaklı')]
    id=models.CharField(max_length=10,primary_key=True)
    no=models.CharField(max_length=4,default='')
    floor=models.CharField(max_length=2,null=True,blank=True)
    people=models.CharField(max_length=2,choices=room_people_list)
    type=models.CharField(max_length=20,choices=room_type_list)
    desc=models.CharField(max_length=100,blank=True,null=True)
    company_id = models.ForeignKey(CompanyInfoModel,default='')

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


    def people_list(self):
        from person_panel.models import StudentInfoModel
        return [person for person in StudentInfoModel.objects.filter(room_id=self.id)]

    def situation(self):
        if int(self.people)==0:
            return 'pasif'
        elif int(self.people)-len(self.people_list())==0:
            return 'dolu'
        else:
            return 'bos'

class FixtureInfoModel(models.Model):
    fixture_type_list = [('1', 'Baza'), ('2', 'Yatak'), ('3', 'Dolap'), ('4', 'Halı'), ('5', 'Komodin'),
                         ('6', 'Tül'), ('7', 'Perde'), ('8', 'Masa'), ('9', 'Sandalye'), ('10', 'Askılık'),
                         ('11', 'Kitaplık'), ('12', 'Lamba'), ('13', 'Klima'), ('14', 'Ayna')]
    no = models.CharField(max_length=10,primary_key=True)
    room=models.ForeignKey(RoomInfoModel,unique=False,default='')
    type=models.CharField(max_length=20,choices=fixture_type_list)
    notes=models.CharField(max_length=100,blank=True,null=True)
    image_field = models.ImageField(upload_to='fixture_image/',default='')
    company_id=models.ForeignKey(CompanyInfoModel,default='')

    class Meta:
        db_table='fixture_info'

    def __str__(self):
        return ('%s - %s'%(self.no,self.type_name()))

    def type_name(self):
        return self.fixture_type_list[int(self.type)-1][1]


