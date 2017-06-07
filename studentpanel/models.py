# -*- codingutf-8 -*-
import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from fixturepanel.models import RoomInfoModel
import os


class StudentInfoModel(models.Model):
    room_number_list=[]
    for room in RoomInfoModel.objects.all():
        room_number_list.append((room.room_no,room.room_no))
    year_list=(('Prep','Preparation'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'))
    city_list = (('01', 'Adana'), ('02', 'Ad\xc4\xb1yaman'), ('03', 'Afyon'), ('04', 'A\xc4\x9fr\xc4\xb1'), ('05', 'Amasya'),('06', 'Ankara'), ('07', 'Antalya'), ('08', 'Artvin'), ('09', 'Ayd\xc4\xb1n'), ('10', 'Bal\xc4\xb1kesir'),('11', 'Bilecik'), ('12', 'Bing\xc3\xb6l'), ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'),('17', '\xc3\x87anakkale'), ('18', '\xc3\x87ank\xc4\xb1r\xc4\xb1'), ('19', '\xc3\x87orum'), ('20', 'Denizli'),('21', 'Diyarbak\xc4\xb1r'), ('22', 'Edirne'), ('23', 'Elaz\xc4\xb1\xc4\x9f'), ('24', 'Erzincan'),('25', 'Erzurum'), ('26', 'Eski\xc5\x9fehir'), ('27', 'Gaziantep'), ('28', 'Giresun'),('29', 'G\xc3\xbcm\xc3\xbc\xc5\x9fhane'), ('30', 'Hakkari'), ('31', 'Hatay'), ('32', 'Isparta'), ('33', 'Mersin'),('34', '\xc4\xb0stanbul'), ('35', '\xc4\xb0zmir'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'),('39', 'K\xc4\xb1rklareli'), ('40', 'K\xc4\xb1r\xc5\x9fehir'), ('41', 'Kocaeli'), ('42', 'Konya'),('43', 'K\xc3\xbctahya'), ('44', 'Malatya'), ('45', 'Manisa'), ('46', 'Kahramanmara\xc5\x9f'), ('47', 'Mardin'),('48', 'Mu\xc4\x9fla'), ('49', 'Mu\xc5\x9f'), ('50', 'Nev\xc5\x9fehir'), ('51', 'Ni\xc4\x9fde'), ('52', 'Ordu'),('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'), ('57', 'Sinop'), ('58', 'Sivas'),('59', 'Tekirda\xc4\x9f'), ('60', 'Tokat'), ('61', 'Trabzon'), ('62', 'Tunceli'), ('63', '\xc5\x9eanl\xc4\xb1urfa'),('64', 'U\xc5\x9fak'), ('65', 'Van'), ('66', 'Yozgat'), ('67', 'Zonguldak'), ('68', 'Aksaray'), ('69', 'Bayburt'),('70', 'Karaman'), ('71', 'K\xc4\xb1r\xc4\xb1kkale'), ('72', 'Batman'), ('73', '\xc5\x9e\xc4\xb1rnak'),('74', 'Bart\xc4\xb1n'), ('75', 'Ardahan'), ('76', 'I\xc4\x9fd\xc4\xb1r'), ('77', 'Yalova'),('78', 'Karab\xc3\xbck'), ('79', 'Kilis'), ('80', 'Osmaniye'), ('81', 'D\xc3\xbczce'))
    blood_type_list=(('0_rh_+','0 rh +'),('0_rh_-','0 rh -'),('A_rh_+','Arh +'),('A_rh_-','A rh -'),('B_rh_+','B rh +'),('B_rh_-','B rh -'),('AB_rh_+','AB rh+'),('AB_rh_-','AB rh-'))
    student_type=(('Guest','Guest'),('Temporary','Temporary'),('Permanent','Permanent'))

    student_tcn = models.CharField(max_length=11,default='00000000000',verbose_name='TC No',help_text='11 digit',unique=True)
    student_name = models.CharField(max_length=200,default='Ahmet',verbose_name='Student Name',help_text='Student Name')
    student_lastname = models.CharField(max_length=200,default='Yilmaz',verbose_name='Student Last Name',help_text='Student Last Name')
    student_phone = PhoneNumberField(default='+905553332211',verbose_name='Phone Number',help_text='+905553332211')
    student_email = models.EmailField(default='qwe@gam.com',verbose_name='Student Email',help_text='aaaaa@aaaa.aaa',unique=True)
    student_birthday = models.DateField(default='31/12/1990',verbose_name='Birthday',help_text='31//12/1990')
    student_regday = models.DateField(default=datetime.date.today,verbose_name='Registration Day',help_text='31/12/1990')
    student_city = models.CharField(null=True,max_length=20,choices=city_list,default='Ankara',verbose_name='Student City',help_text='City Where Student From')
    student_town = models.CharField(null=True,max_length=20,default='yok',verbose_name='Student Town',help_text='Town Where Student From')
    student_adress = models.CharField(null=True,max_length=50,default='yok',verbose_name='Student Address',help_text='Distinct, Street, Building No, Flat No')

    room_number = models.CharField(null=True,max_length=3, choices=room_number_list, default='101',verbose_name='Room Number',help_text='Room Number Student Assigned')
    student_type = models.CharField(max_length=10, choices=student_type, default='Permanent',verbose_name='Student Type',help_text='Student Accommodation Type')
    birth_place = models.CharField(null=True,max_length=20, choices=city_list, default=city_list[0],verbose_name='Birth City',help_text='City Where Student Birth')
    school_name = models.CharField(null=True,max_length=50, default='okulsuz',verbose_name='School Name',help_text='School Name')
    education_year = models.CharField(null=True,max_length=20, choices=year_list, default=year_list[0],verbose_name='Education Year',help_text='Education Year')
    blood_type = models.CharField(null=True,max_length=20, choices=blood_type_list, default='0 rh +',verbose_name='Blood Type',help_text='Blood Type')
    health_notes = models.CharField(null=True,blank=True,max_length=100, default='-',verbose_name='Health Notes',help_text='Health Notes')
    special_notes = models.CharField(null=True,blank=True,max_length=100, default='-',verbose_name='Special Notes',help_text='Special Notes')
    file_field = models.ImageField(null=True,blank=True,upload_to='profile_pic/',default='Desktop/asd.jpg',verbose_name='Image Upload',help_text='Profile Image Path')


    class Meta:
        db_table= 'student_info'

    def __str__(self):
        return self.student_name,self.student_lastname,self.student_email

    def image_path(self):
        print (self.file_field.path)
        return os.stat(self.file_field.path)

class ParentInfoModel(models.Model):
    student_info_list=StudentInfoModel.objects.all()
    student_id_list=[]
    for student in student_info_list:
        student_id_list.append((student.id,'%s %s'% (student.student_name,student.student_lastname)))

    student_id=models.IntegerField(choices=student_id_list,primary_key=True)
    parent_name=models.CharField(max_length=20)
    parent_lastname=models.CharField(max_length=20)
    parent_TCN=models.CharField(max_length=11)
    parent_phone=PhoneNumberField()
    parent_email=models.EmailField()
    relative_degree=models.CharField(max_length=20)
    parent_job=models.CharField(max_length=20)
    #student=models.ForeignKey(StudentInfoModel,on_delete=models.CASCADE)

    class Meta:
        db_table='parent_info'

    def __str__(self):
        return self.parent_name


# class DepartmentInfoModel(models.Model):
#     pass
#
# class DepositInfoModel(models.Model):
#     pass
#


# class SchoolInfoModel(models.Model):
#     school_type_list=[(1,'Primary School'),(2,'High School'),(3,'College'),(4,'University'),(5,'Others')]
#     school_name=models.CharField(max_length=20)
#     school_type=models.CharField(max_length=20,choices=school_type_list)
#     school_city=models.CharField(max_length=20,choices=CityInfoModel.objects.all())
#     school_town=models.CharField(max_length=20)
