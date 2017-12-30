# -*- coding: utf-8 -*-
import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from stock_panel.models import RoomInfoModel
from user_panel.models import CompanyInfoModel
from localflavor.tr.tr_provinces import PROVINCE_CHOICES
from django.contrib.auth.models import User

def get_time():
    return datetime.datetime.now()

def get_date():
    return datetime.date.today()


class PersonIDInfoModel(models.Model):
    idcard_type_list = [('1', 'Eski Kimlik'), ('2', 'Yeni Kimlik'), ('3', 'Ehliyet'), ('4', 'Pasaport'),('5', 'Diğer')]
    nation_list = [('1', 'Türkiye')]# TODO: milletler eklenecek
    gender_list = [('1', 'Kadın'), ('2', 'Erkek')]
    medeni_hal_list = [('1', 'Bekar'), ('2', 'Evli'), ('3', 'Dul'), ('4', 'Diğer')]
    city_list=PROVINCE_CHOICES
    tcn = models.CharField(max_length=11, default='',primary_key=True)
    name = models.CharField(max_length=20, default='',)
    last_name = models.CharField(max_length=20, default='',)
    birth_day = models.DateField(default='1990-12-31',max_length=10)
    birth_place = models.CharField(max_length=20, choices=PROVINCE_CHOICES,blank=True,null=True)
    father = models.CharField(max_length=20,default='')
    mother = models.CharField(max_length=20,default='')
    nation = models.CharField(max_length=30,choices=nation_list,default='1')
    idcard_type = models.CharField(max_length=50,choices=idcard_type_list,default='1')
    register_vilage = models.CharField(max_length=50,choices=PROVINCE_CHOICES,blank=True,null=True)
    register_town = models.CharField(max_length=50,blank=True,null=True)
    register_distinct = models.CharField(max_length=50,blank=True,null=True)
    gender = models.CharField(max_length=5,default='1', choices=gender_list)
    nufus_cilt = models.CharField(max_length=4,blank=True,null=True)
    nufus_ailesira = models.CharField(max_length=5,blank=True,null=True)
    nufus_sirano = models.CharField(max_length=4,blank=True,null=True)
    medeni_hali = models.CharField(max_length=10,choices=medeni_hal_list,blank=True,null=True)
    company_id=models.ForeignKey(CompanyInfoModel,default='',on_delete=models.CASCADE)

    class Meta:
        db_table='personid_info'

    def __str__(self):
        return str(self.tcn)+' - '+str(self.full_name())

    def full_name(self):
        return '%s %s'% (self.name,self.last_name)

    def birth_city_name(self):
        return PROVINCE_CHOICES[int(self.birth_place)-1][1]

    def idcard_type_name(self):
        return dict(self.idcard_type_list)[self.idcard_type]

    def nation_name(self):
        return dict(self.nation_list)[self.nation]

    def gender_name(self):
        return dict(self.gender_list)[self.gender]

    def medeni_hali_name(self):
        return dict(self.medeni_hal_list)[self.medeni_hali]

    def group(self):
        return 'Person_id'


class PersonalInfoModel(models.Model):
    blood_type_list=(('0','0 rh +'),('1','0 rh -'),('2','A rh +'),('3','A rh -'),('4','B rh +'),('5','B rh -'),('6','AB rh+'),('7','AB rh-'))
    personal_type_list=[('0','Accountant'),('1',''),('2','')]
    id = models.CharField(max_length=7,primary_key=True,default='')
    tcn = models.OneToOneField(PersonIDInfoModel,unique=True,on_delete=models.CASCADE)
    phone = PhoneNumberField(default='+905553332211',max_length=13)
    email = models.EmailField(default='',unique=True)
    start_day = models.DateField(default=get_date,max_length=10)
    end_day = models.DateField(max_length=10,null=True,blank=True)
    city = models.CharField(max_length=20, choices=PROVINCE_CHOICES,default='1')
    town = models.CharField(max_length=20, null=True,blank=True)
    address = models.CharField( max_length=100, null=True,blank=True)
    blood_type = models.CharField(max_length=20, choices=blood_type_list, default='1')
    health_notes = models.CharField(max_length=200, null=True,blank=True)
    special_notes = models.CharField(max_length=200, null=True,blank=True)
    image_field = models.ImageField(upload_to='profile_pic/',default='')
    salary=models.CharField(max_length=7,default='2000.0')
    company_id=models.ForeignKey(CompanyInfoModel,default='',on_delete=models.CASCADE)

    class Meta:
        db_table='personal_info'

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)

    def image_path(self):
        return self.image_field.path

    def city_name(self):
        return PROVINCE_CHOICES[int(self.city)-1][1]

    def blood_type_name(self):
        return self.blood_type_list[int(self.blood_type)][1]

    def full_name(self):
        return self.tcn.full_name()

    def group(self):
        return 'Personel'


class StudentInfoModel(models.Model):
    year_list=(('0','Hazırlık'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'))
    #city_list = (('01', 'Adana'), ('02', 'Ad\xc4\xb1yaman'), ('03', 'Afyon'), ('04', 'A\xc4\x9fr\xc4\xb1'), ('05', 'Amasya'),('06', 'Ankara'), ('07', 'Antalya'), ('08', 'Artvin'), ('09', 'Ayd\xc4\xb1n'), ('10', 'Bal\xc4\xb1kesir'),('11', 'Bilecik'), ('12', 'Bing\xc3\xb6l'), ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'),('17', '\xc3\x87anakkale'), ('18', '\xc3\x87ank\xc4\xb1r\xc4\xb1'), ('19', '\xc3\x87orum'), ('20', 'Denizli'),('21', 'Diyarbak\xc4\xb1r'), ('22', 'Edirne'), ('23', 'Elaz\xc4\xb1\xc4\x9f'), ('24', 'Erzincan'),('25', 'Erzurum'), ('26', 'Eski\xc5\x9fehir'), ('27', 'Gaziantep'), ('28', 'Giresun'),('29', 'G\xc3\xbcm\xc3\xbc\xc5\x9fhane'), ('30', 'Hakkari'), ('31', 'Hatay'), ('32', 'Isparta'), ('33', 'Mersin'),('34', '\xc4\xb0stanbul'), ('35', '\xc4\xb0zmir'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'),('39', 'K\xc4\xb1rklareli'), ('40', 'K\xc4\xb1r\xc5\x9fehir'), ('41', 'Kocaeli'), ('42', 'Konya'),('43', 'K\xc3\xbctahya'), ('44', 'Malatya'), ('45', 'Manisa'), ('46', 'Kahramanmara\xc5\x9f'), ('47', 'Mardin'),('48', 'Mu\xc4\x9fla'), ('49', 'Mu\xc5\x9f'), ('50', 'Nev\xc5\x9fehir'), ('51', 'Ni\xc4\x9fde'), ('52', 'Ordu'),('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'), ('57', 'Sinop'), ('58', 'Sivas'),('59', 'Tekirda\xc4\x9f'), ('60', 'Tokat'), ('61', 'Trabzon'), ('62', 'Tunceli'), ('63', '\xc5\x9eanl\xc4\xb1urfa'),('64', 'U\xc5\x9fak'), ('65', 'Van'), ('66', 'Yozgat'), ('67', 'Zonguldak'), ('68', 'Aksaray'), ('69', 'Bayburt'),('70', 'Karaman'), ('71', 'K\xc4\xb1r\xc4\xb1kkale'), ('72', 'Batman'), ('73', '\xc5\x9e\xc4\xb1rnak'),('74', 'Bart\xc4\xb1n'), ('75', 'Ardahan'), ('76', 'I\xc4\x9fd\xc4\xb1r'), ('77', 'Yalova'),('78', 'Karab\xc3\xbck'), ('79', 'Kilis'), ('80', 'Osmaniye'), ('81', 'D\xc3\xbczce'))
    blood_type_list = (('0', '0 rh +'), ('1', '0 rh -'), ('2', 'A rh +'), ('3', 'A rh -'), ('4', 'B rh +'), ('5', 'B rh -'),('6', 'AB rh+'), ('7', 'AB rh-'))
    student_type_list=(('0','Normal'),('1','Geçici'),('2','Misafir'))

    id = models.CharField(max_length=7,primary_key=True,default='1701001')
    tcn=models.OneToOneField(PersonIDInfoModel,unique=True,on_delete=models.CASCADE)
    phone = PhoneNumberField(default='+905553332211',max_length=13)
    email = models.EmailField(null=True,blank=True)
    start_day = models.DateField(default=get_date,max_length=10)
    leave_day = models.DateField(max_length=10,null=True,blank=True)
    city = models.CharField(max_length=20,choices=PROVINCE_CHOICES,default='1')
    town = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    room_id = models.ForeignKey(RoomInfoModel,default='101',on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=student_type_list, default='1')
    school_name = models.CharField(max_length=30,null=True,blank=True)
    education_year = models.CharField(max_length=20, choices=year_list, default='1')
    blood_type = models.CharField(max_length=20, choices=blood_type_list, default='1')
    health_notes = models.CharField(max_length=200,null=True,blank=True)
    special_notes = models.CharField(max_length=200,null=True,blank=True)
    image_field = models.ImageField(upload_to='profile_pic/',null=True,blank=True)
    position= models.BooleanField(default='1')
    company_id=models.ForeignKey(CompanyInfoModel,default='',on_delete=models.CASCADE)


    class Meta:
        db_table= 'student_info'

    def __str__(self):
        return str(self.id+' - '+self.full_name())

    def __unicode__(self):
        return str(self.id)

    def full_name(self):
        return self.tcn.full_name()

    def city_name(self):
        return PROVINCE_CHOICES[int(self.city)-1][1]

    def education_year_name(self):
        return self.year_list[int(self.education_year)][1]

    def blood_type_name(self):
        return self.blood_type_list[int(self.blood_type)][1]

    def type_name(self):
        return self.student_type_list[int(self.type)][1]

    def payment_info(self):
        from account_panel.models import PersonAssetInfoModel
        return PersonAssetInfoModel.objects.filter(person_id=self.id)

    def parent(self):
        if len(ParentInfoModel.objects.filter(person=self.id))!=0:
            return ParentInfoModel.objects.filter(person=self.id)[0]
        else:
            return None

    def group(self):
        return 'Öğrenci'


class ParentInfoModel(models.Model):
    id=models.CharField(max_length=8,primary_key=True,default='1704001')
    person=models.ForeignKey(StudentInfoModel,unique=False,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,default='')
    last_name=models.CharField(max_length=20,default='')
    tcn=models.CharField(max_length=11,null=True,blank=True)
    phone=PhoneNumberField(default='')
    email=models.EmailField(default='')
    relative_degree=models.CharField(max_length=20,default='')
    job=models.CharField(max_length=20,null=True,blank=True)
    company_id=models.ForeignKey(CompanyInfoModel,default='',on_delete=models.CASCADE)

    class Meta:
        db_table='parent_info'

    def __str__(self):
        return self.id

    def full_name(self):
        return '%s %s'% (self.name,self.last_name)

    def group(self):
        return 'Veli'

