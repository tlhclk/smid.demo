# -*- codingutf-8 -*-
import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from stock_panel.models import RoomInfoModel
from localflavor.tr.tr_provinces import PROVINCE_CHOICES



class StudentInfoModel(models.Model):
    year_list=(('0','Preparation'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'))
    #city_list = (('01', 'Adana'), ('02', 'Ad\xc4\xb1yaman'), ('03', 'Afyon'), ('04', 'A\xc4\x9fr\xc4\xb1'), ('05', 'Amasya'),('06', 'Ankara'), ('07', 'Antalya'), ('08', 'Artvin'), ('09', 'Ayd\xc4\xb1n'), ('10', 'Bal\xc4\xb1kesir'),('11', 'Bilecik'), ('12', 'Bing\xc3\xb6l'), ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'),('17', '\xc3\x87anakkale'), ('18', '\xc3\x87ank\xc4\xb1r\xc4\xb1'), ('19', '\xc3\x87orum'), ('20', 'Denizli'),('21', 'Diyarbak\xc4\xb1r'), ('22', 'Edirne'), ('23', 'Elaz\xc4\xb1\xc4\x9f'), ('24', 'Erzincan'),('25', 'Erzurum'), ('26', 'Eski\xc5\x9fehir'), ('27', 'Gaziantep'), ('28', 'Giresun'),('29', 'G\xc3\xbcm\xc3\xbc\xc5\x9fhane'), ('30', 'Hakkari'), ('31', 'Hatay'), ('32', 'Isparta'), ('33', 'Mersin'),('34', '\xc4\xb0stanbul'), ('35', '\xc4\xb0zmir'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'),('39', 'K\xc4\xb1rklareli'), ('40', 'K\xc4\xb1r\xc5\x9fehir'), ('41', 'Kocaeli'), ('42', 'Konya'),('43', 'K\xc3\xbctahya'), ('44', 'Malatya'), ('45', 'Manisa'), ('46', 'Kahramanmara\xc5\x9f'), ('47', 'Mardin'),('48', 'Mu\xc4\x9fla'), ('49', 'Mu\xc5\x9f'), ('50', 'Nev\xc5\x9fehir'), ('51', 'Ni\xc4\x9fde'), ('52', 'Ordu'),('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'), ('57', 'Sinop'), ('58', 'Sivas'),('59', 'Tekirda\xc4\x9f'), ('60', 'Tokat'), ('61', 'Trabzon'), ('62', 'Tunceli'), ('63', '\xc5\x9eanl\xc4\xb1urfa'),('64', 'U\xc5\x9fak'), ('65', 'Van'), ('66', 'Yozgat'), ('67', 'Zonguldak'), ('68', 'Aksaray'), ('69', 'Bayburt'),('70', 'Karaman'), ('71', 'K\xc4\xb1r\xc4\xb1kkale'), ('72', 'Batman'), ('73', '\xc5\x9e\xc4\xb1rnak'),('74', 'Bart\xc4\xb1n'), ('75', 'Ardahan'), ('76', 'I\xc4\x9fd\xc4\xb1r'), ('77', 'Yalova'),('78', 'Karab\xc3\xbck'), ('79', 'Kilis'), ('80', 'Osmaniye'), ('81', 'D\xc3\xbczce'))
    blood_type_list = (('0', '0 rh +'), ('1', '0 rh -'), ('2', 'A rh +'), ('3', 'A rh -'), ('4', 'B rh +'), ('5', 'B rh -'),('6', 'AB rh+'), ('7', 'AB rh-'))
    student_type_list=(('0','Guest'),('1','Temporary'),('2','Permanent'))

    id = models.CharField(max_length=7,verbose_name='Student Id',help_text='ID',primary_key=True)
    student_position= models.BooleanField(verbose_name='Student Position',help_text='In-Out')
    student_tcn = models.CharField(max_length=11,default='00000000000',verbose_name='TC No',help_text='11 digit',unique=True)
    student_name = models.CharField(max_length=200,default='Ahmet',verbose_name='Student Name',help_text='Student Name')
    student_lastname = models.CharField(max_length=200,default='Yilmaz',verbose_name='Student Last Name',help_text='Student Last Name')
    student_phone = PhoneNumberField(default='+905553332211',verbose_name='Phone Number',help_text='+905553332211')
    student_email = models.EmailField(default='qwe@gam.com',verbose_name='Student Email',help_text='aaaaa@aaaa.aaa',unique=True)
    student_birthday = models.DateField(default='1990-12-31',verbose_name='Birthday',help_text='1990-12-31')
    student_regday = models.DateField(default=datetime.date.today,verbose_name='Registration Day',help_text='1990-12-31')
    student_city = models.CharField(null=True,max_length=20,choices=PROVINCE_CHOICES,default='Ankara',verbose_name='Student City',help_text='City Where Student From')
    student_town = models.CharField(null=True,max_length=20,default='yok',verbose_name='Student Town',help_text='Town Where Student From')
    student_adress = models.CharField(null=True,max_length=50,default='yok',verbose_name='Student Address',help_text='Distinct, Street, Building No, Flat No')
    #room_no = models.CharField(max_length=10,null=True,blank=True)
    room_no = models.ForeignKey(RoomInfoModel,null=True,unique=False,verbose_name='Room Number',help_text='Room Number Student Assigned')
    student_type = models.CharField(max_length=10, choices=student_type_list, default='Permanent',verbose_name='Student Type',help_text='Student Accommodation Type')
    birth_place = models.CharField(null=True,max_length=20, choices=PROVINCE_CHOICES, default=PROVINCE_CHOICES[0],verbose_name='Birth City',help_text='City Where Student Birth')
    school_name = models.CharField(null=True,max_length=50, default='okulsuz',verbose_name='School Name',help_text='School Name')
    education_year = models.CharField(null=True,max_length=20, choices=year_list, default=year_list[0],verbose_name='Education Year',help_text='Education Year')
    blood_type = models.CharField(null=True,max_length=20, choices=blood_type_list, default='0 rh +',verbose_name='Blood Type',help_text='Blood Type')
    health_notes = models.CharField(null=True,blank=True,max_length=100, default='-',verbose_name='Health Notes',help_text='Health Notes')
    special_notes = models.CharField(null=True,blank=True,max_length=100, default='-',verbose_name='Special Notes',help_text='Special Notes')
    file_field = models.ImageField(null=True,blank=True,upload_to='profile_pic/',default='Desktop/asd.jpg',verbose_name='Image Upload',help_text='Add an Image')


    class Meta:
        db_table= 'student_info'

    def __str__(self):
        return self.id

    def __unicode__(self):
        return str(self.id)

    def city_name(self):
        return PROVINCE_CHOICES[int(self.student_city)-1][1]

    def birth_city_name(self):
        return PROVINCE_CHOICES[int(self.birth_place)-1][1]

    def education_year_name(self):
        return self.year_list[int(self.education_year)][1]

    def blood_type_name(self):
        return self.blood_type_list[int(self.blood_type)][1]

    def student_type_name(self):
        return self.student_type_list[int(self.student_type)][1]

    def full_name(self):
        return '%s %s'% (self.student_name,self.student_lastname)

    def group(self):
        return 'Student'


class ParentInfoModel(models.Model):
    id=models.CharField(max_length=50,primary_key=True,verbose_name='Parent Id: ',help_text='Parent Id')
    #student_id=models.CharField(max_length=10,null=True,blank=True)
    student_id=models.ForeignKey(StudentInfoModel,null=False,unique=False)
    parent_name=models.CharField(max_length=20,null=False,verbose_name='Parent Name',help_text='Parent Name')
    parent_lastname=models.CharField(max_length=20,null=False,verbose_name='Parent Lastname')
    parent_TCN=models.CharField(max_length=11,null=False,verbose_name='Parent TCN',blank=True)
    parent_phone=PhoneNumberField(null=False,verbose_name='Parent Phone')
    parent_email=models.EmailField(null=False,verbose_name='Parent E-mail')
    relative_degree=models.CharField(max_length=20,null=False,verbose_name='Relative Degree',default='Father')
    parent_job=models.CharField(max_length=20,blank=True,verbose_name='Parent Job')

    class Meta:
        db_table='parent_info'

    def __str__(self):
        return self.parent_name

    def full_name(self):
        return '%s %s'% (self.parent_name,self.parent_lastname)

    def group(self):
        return 'Parent'


class PersonalInfoModel(models.Model):
    #city_list = (('01', 'Adana'), ('02', 'Ad\xc4\xb1yaman'), ('03', 'Afyon'), ('04', 'A\xc4\x9fr\xc4\xb1'), ('05', 'Amasya'),('06', 'Ankara'), ('07', 'Antalya'), ('08', 'Artvin'), ('09', 'Ayd\xc4\xb1n'), ('10', 'Bal\xc4\xb1kesir'),('11', 'Bilecik'), ('12', 'Bing\xc3\xb6l'), ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'),('17', '\xc3\x87anakkale'), ('18', '\xc3\x87ank\xc4\xb1r\xc4\xb1'), ('19', '\xc3\x87orum'), ('20', 'Denizli'),('21', 'Diyarbak\xc4\xb1r'), ('22', 'Edirne'), ('23', 'Elaz\xc4\xb1\xc4\x9f'), ('24', 'Erzincan'),('25', 'Erzurum'), ('26', 'Eski\xc5\x9fehir'), ('27', 'Gaziantep'), ('28', 'Giresun'),('29', 'G\xc3\xbcm\xc3\xbc\xc5\x9fhane'), ('30', 'Hakkari'), ('31', 'Hatay'), ('32', 'Isparta'), ('33', 'Mersin'),('34', '\xc4\xb0stanbul'), ('35', '\xc4\xb0zmir'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'),('39', 'K\xc4\xb1rklareli'), ('40', 'K\xc4\xb1r\xc5\x9fehir'), ('41', 'Kocaeli'), ('42', 'Konya'),('43', 'K\xc3\xbctahya'), ('44', 'Malatya'), ('45', 'Manisa'), ('46', 'Kahramanmara\xc5\x9f'), ('47', 'Mardin'),('48', 'Mu\xc4\x9fla'), ('49', 'Mu\xc5\x9f'), ('50', 'Nev\xc5\x9fehir'), ('51', 'Ni\xc4\x9fde'), ('52', 'Ordu'),('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'), ('57', 'Sinop'), ('58', 'Sivas'),('59', 'Tekirda\xc4\x9f'), ('60', 'Tokat'), ('61', 'Trabzon'), ('62', 'Tunceli'), ('63', '\xc5\x9eanl\xc4\xb1urfa'),('64', 'U\xc5\x9fak'), ('65', 'Van'), ('66', 'Yozgat'), ('67', 'Zonguldak'), ('68', 'Aksaray'), ('69', 'Bayburt'),('70', 'Karaman'), ('71', 'K\xc4\xb1r\xc4\xb1kkale'), ('72', 'Batman'), ('73', '\xc5\x9e\xc4\xb1rnak'),('74', 'Bart\xc4\xb1n'), ('75', 'Ardahan'), ('76', 'I\xc4\x9fd\xc4\xb1r'), ('77', 'Yalova'),('78', 'Karab\xc3\xbck'), ('79', 'Kilis'), ('80', 'Osmaniye'), ('81', 'D\xc3\xbczce'))
    blood_type_list=(('0','0 rh +'),('1','0 rh -'),('2','A rh +'),('3','A rh -'),('4','B rh +'),('5','B rh -'),('6','AB rh+'),('7','AB rh-'))
    personal_type_list=[('0','Accountant'),('1',''),('2','')]
    id = models.CharField(max_length=7,verbose_name='Personal Id', help_text='ID', primary_key=True)
    personal_tcn = models.CharField(max_length=11, default='00000000000', verbose_name='TC No', help_text='11 digit',unique=True)
    personal_name = models.CharField(max_length=200, default='Ahmet', verbose_name='Personal Name',help_text='Personal Name')
    personal_lastname = models.CharField(max_length=200, default='Yilmaz', verbose_name='Personal Last Name',help_text='Personal Last Name')
    personal_phone = PhoneNumberField(default='+905553332211', verbose_name='Phone Number', help_text='+905553332211')
    personal_email = models.EmailField(default='qwe@gam.com', verbose_name='Personal Email', help_text='aaaaa@aaaa.aaa',unique=True)
    personal_startday = models.DateField(default=datetime.date.today, verbose_name='Start Day',help_text='1990-12-31')
    personal_endday = models.DateField(verbose_name='Quit Day',help_text='1990-12-31',blank=True,null=True)
    personal_city = models.CharField(null=True, max_length=20, choices=PROVINCE_CHOICES, default='Ankara',verbose_name='Personal City', help_text='City Where Personal From')
    personal_town = models.CharField(null=True, max_length=20, default='yok', verbose_name='Personal Town',help_text='Town Where Personal From')
    personal_adress = models.CharField(null=True, max_length=50, default='yok', verbose_name='Personal Address',help_text='Distinct, Street, Building No, Flat No')
    personal_birthday = models.DateField(default='1990-12-31', verbose_name='Birthday', help_text='1990-12-31')
    blood_type = models.CharField(null=True,max_length=20, choices=blood_type_list, default='0 rh +',verbose_name='Blood Type',help_text='Blood Type')
    health_notes = models.CharField(null=True,blank=True,max_length=100, default='-',verbose_name='Health Notes',help_text='Health Notes')
    special_notes = models.CharField(null=True,blank=True,max_length=100, default='-',verbose_name='Special Notes',help_text='Special Notes')
    image_field = models.ImageField(null=True,blank=True,upload_to='profile_pic/',default='Desktop/asd.jpg',verbose_name='Image Upload',help_text='Profile Image Path')


    class Meta:
        db_table='personal_info'

    def __str__(self):
        return self.id

    def __unicode__(self):
        return str(self.id)

    def image_path(self):
        return self.image_field.path

    def city_name(self):
        return PROVINCE_CHOICES[int(self.personal_city)-1][1]

    def blood_type_name(self):
        return self.blood_type_list[int(self.blood_type)][1]

    #def personal_type_name(self):
    #    return self.personal_type_list[int(self.personal_type)][1]

    def full_name(self):
        return '%s %s'% (self.personal_name,self.personal_lastname)

    def group(self):
        return 'Personal'

