# -*- coding: utf-8 -*-
from django.db import models
import datetime
from user_panel.models import CompanyInfoModel

class RoomInfoModel(models.Model):
    room_people_list=(('1','Tek Kişilik'),('2','İki Kişilik'),('3','Üç Kişilik'),('4','Dört Kişilik'),('5','Beş Kişilik'),('6',' Altı Kişilik'))
    room_type_list=(('1','Koridor'),('2','Çalışma Odası'),('3','Konaklama'),('4','Mutfak'),('5','Diğer'))
    no=models.CharField(max_length=4,default='')
    floor=models.CharField(max_length=2,null=True,blank=True)
    people=models.CharField(max_length=2,choices=room_people_list,default='4')
    type=models.CharField(max_length=20,choices=room_type_list,default='3')
    desc=models.CharField(max_length=100,blank=True,null=True)
    company = models.ForeignKey(CompanyInfoModel,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        db_table='room_info'

    def __str__(self):
        return str(self.no)

    def __unicode__(self):
        return str(self.no)

    def people_name(self):
        return self.room_people_list[int(self.people)-1][1]

    def type_name(self):
        return self.room_type_list[int(self.type)-1][1]

    def people_list(self):
        from person_panel.models import StudentInfoModel
        a_list=[person for person in StudentInfoModel.objects.filter(room_id_id=self.id,company=self.company_id)]
        asad=['']*(int(self.people)-len(a_list))
        return a_list+asad

    def fixture_list(self):
        return [fixture for fixture in FixtureInfoModel.objects.filter(room_id=self.id,company=self.company_id)]

    def situation(self):
        if int(self.people)==0:
            return 'pasif'
        elif '' not in self.people_list():
            return 'dolu'
        else:
            return 'bos'

class FixtureInfoModel(models.Model):
    fixture_type_list = (('1', 'Baza'), ('2', 'Yatak'), ('3', 'Dolap'), ('4', 'Halı'), ('5', 'Komodin'),
                         ('6', 'Tül'), ('7', 'Perde'), ('8', 'Masa'), ('9', 'Sandalye'), ('10', 'Askılık'),
                         ('11', 'Kitaplık'), ('12', 'Lamba'), ('13', 'Klima'), ('14', 'Ayna'))
    fixture_image_list = (('1', 'Baza.jpg'), ('2', 'Yatak.jpg'), ('3', 'Dolap.jpg'), ('4', 'Halı.jpg'), ('5', 'Komodin.jpg'),
                         ('6', 'Tül.jpg'), ('7', 'Perde.jpg'), ('8', 'Masa.jpg'), ('9', 'Sandalye.jpg'), ('10', 'Askılık.jpg'),
                         ('11', 'Kitaplık.jpg'), ('12', 'Lamba.jpg'), ('13', 'Klima.jpg'), ('14', 'Ayna.jpg'))
    no = models.CharField(max_length=10,primary_key=True)
    room=models.ForeignKey(RoomInfoModel,unique=False,default='',on_delete=models.CASCADE)
    type=models.CharField(max_length=20,choices=fixture_type_list)
    notes=models.CharField(max_length=100,blank=True,null=True)
    image_field = models.ImageField(upload_to='fixture_image/',blank=True,null=True)
    company=models.ForeignKey(CompanyInfoModel,default='',on_delete=models.CASCADE)

    class Meta:
        db_table='fixture_info'

    def __str__(self):
        return ('%s - %s'%(self.no,self.type_name()))

    def type_name(self):
        return self.fixture_type_list[int(self.type)-1][1]



