# -*- coding: utf-8 -*-
import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from stock_panel.models import RoomInfoModel
from localflavor.tr.tr_provinces import PROVINCE_CHOICES


def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class PersonIDInfoModel(models.Model):
    idcard_type_list = [('1', 'Nüfus Cüzdanı'), ('2', 'TC Kimliği'), ('3', 'Ehliyet'), ('4', 'Pasaport'),('5', 'Diğer')]
    nation_list = [('1', 'Türkiye')]
    gender_list = [('1', 'Kadın'), ('2', 'Erkek')]
    medeni_hal_list = [('1', 'Bekar'), ('2', 'Evli'), ('3', 'Dul'), ('4', 'Diğer')]
    city_list=PROVINCE_CHOICES
    s_tcn = models.CharField(max_length=11, default='', verbose_name='TC No',primary_key=True)
    s_name = models.CharField(max_length=50, default='', verbose_name='İsim',)
    s_lastname = models.CharField(max_length=50, default='', verbose_name='Soyisim',)
    s_birthday = models.DateTimeField(default='1990-12-31 00:00:00', verbose_name='Doğum Tarihi',)
    s_birth_place = models.CharField(null=True, max_length=20, choices=PROVINCE_CHOICES,verbose_name='Doğduğu Şehir',default='1')
    s_father = models.CharField(max_length=50, verbose_name='Baba Adı',default='')
    s_mother = models.CharField(max_length=50, verbose_name='Anne Adı',default='')
    s_nation = models.CharField(max_length=50, verbose_name='Uyruk', choices=nation_list,default='1')
    s_idcard_type = models.CharField(max_length=50, verbose_name='Kimlik Türü', choices=idcard_type_list,default='1')
    s_register_vilage = models.CharField(max_length=50, verbose_name='Kayıtlı Olduğu İl', choices=PROVINCE_CHOICES,default='1')
    s_register_town = models.CharField(max_length=50, verbose_name='Kayıtlı Olduğu İlçe', default='')
    s_register_distinct = models.CharField(max_length=50, verbose_name='Kayıtlı Olduğu Mahalle', default='')
    s_gender = models.CharField(max_length=5, verbose_name='Cinsiyet', default='1', choices=gender_list)
    s_nufus_cilt = models.CharField(max_length=4, verbose_name='Cilt No',default='')
    s_nufus_ailesira = models.CharField(max_length=5, verbose_name='Aile Sira No',default='')
    s_nufus_sirano = models.CharField(max_length=4, verbose_name='Sira No',default='')
    s_medeni_hali = models.CharField(max_length=10, verbose_name='Medeni Hali', default='1', choices=medeni_hal_list)

    class Meta:
        db_table='personid_info'

    def __str__(self):
        return self.s_tcn

    def full_name(self):
        return '%s %s'% (self.s_name,self.s_lastname)

    def birth_city_name(self):
        return PROVINCE_CHOICES[int(self.s_birth_place)-1][1]

    def s_idcard_type_name(self):
        return dict(self.idcard_type_list)[self.s_idcard_type]

    def s_nation_name(self):
        return dict(self.nation_list)[self.s_nation]

    def s_gender_name(self):
        return dict(self.gender_list)[self.s_gender]

    def s_medeni_hali_name(self):
        return dict(self.medeni_hal_list)[self.s_medeni_hali]


class PersonalInfoModel(models.Model):
    #city_list = (('01', 'Adana'), ('02', 'Ad\xc4\xb1yaman'), ('03', 'Afyon'), ('04', 'A\xc4\x9fr\xc4\xb1'), ('05', 'Amasya'),('06', 'Ankara'), ('07', 'Antalya'), ('08', 'Artvin'), ('09', 'Ayd\xc4\xb1n'), ('10', 'Bal\xc4\xb1kesir'),('11', 'Bilecik'), ('12', 'Bing\xc3\xb6l'), ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'),('17', '\xc3\x87anakkale'), ('18', '\xc3\x87ank\xc4\xb1r\xc4\xb1'), ('19', '\xc3\x87orum'), ('20', 'Denizli'),('21', 'Diyarbak\xc4\xb1r'), ('22', 'Edirne'), ('23', 'Elaz\xc4\xb1\xc4\x9f'), ('24', 'Erzincan'),('25', 'Erzurum'), ('26', 'Eski\xc5\x9fehir'), ('27', 'Gaziantep'), ('28', 'Giresun'),('29', 'G\xc3\xbcm\xc3\xbc\xc5\x9fhane'), ('30', 'Hakkari'), ('31', 'Hatay'), ('32', 'Isparta'), ('33', 'Mersin'),('34', '\xc4\xb0stanbul'), ('35', '\xc4\xb0zmir'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'),('39', 'K\xc4\xb1rklareli'), ('40', 'K\xc4\xb1r\xc5\x9fehir'), ('41', 'Kocaeli'), ('42', 'Konya'),('43', 'K\xc3\xbctahya'), ('44', 'Malatya'), ('45', 'Manisa'), ('46', 'Kahramanmara\xc5\x9f'), ('47', 'Mardin'),('48', 'Mu\xc4\x9fla'), ('49', 'Mu\xc5\x9f'), ('50', 'Nev\xc5\x9fehir'), ('51', 'Ni\xc4\x9fde'), ('52', 'Ordu'),('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'), ('57', 'Sinop'), ('58', 'Sivas'),('59', 'Tekirda\xc4\x9f'), ('60', 'Tokat'), ('61', 'Trabzon'), ('62', 'Tunceli'), ('63', '\xc5\x9eanl\xc4\xb1urfa'),('64', 'U\xc5\x9fak'), ('65', 'Van'), ('66', 'Yozgat'), ('67', 'Zonguldak'), ('68', 'Aksaray'), ('69', 'Bayburt'),('70', 'Karaman'), ('71', 'K\xc4\xb1r\xc4\xb1kkale'), ('72', 'Batman'), ('73', '\xc5\x9e\xc4\xb1rnak'),('74', 'Bart\xc4\xb1n'), ('75', 'Ardahan'), ('76', 'I\xc4\x9fd\xc4\xb1r'), ('77', 'Yalova'),('78', 'Karab\xc3\xbck'), ('79', 'Kilis'), ('80', 'Osmaniye'), ('81', 'D\xc3\xbczce'))
    blood_type_list=(('0','0 rh +'),('1','0 rh -'),('2','A rh +'),('3','A rh -'),('4','B rh +'),('5','B rh -'),('6','AB rh+'),('7','AB rh-'))
    personal_type_list=[('0','Accountant'),('1',''),('2','')]
    id = models.CharField(max_length=7,verbose_name='Personel No', primary_key=True,default='')
    personal_tcn = models.OneToOneField(PersonIDInfoModel, verbose_name='Personelin Kimlik Numarası', unique=True)
    #personal_tcn = models.CharField(max_length=11, verbose_name='Personel TC No', help_text='11 digit',unique=True)
    #personal_name = models.CharField(max_length=200, default='Ahmet', verbose_name='Personel İsmi',help_text='Personal Name')
    #personal_lastname = models.CharField(max_length=200, default='Yilmaz', verbose_name='Personel Soyismi',help_text='Personal Last Name')
    personal_phone = PhoneNumberField(default='+905553332211', verbose_name='Telefon Numarası',max_length=13)
    personal_email = models.EmailField(default='', verbose_name='Email Adresi',unique=True)
    personal_startday = models.DateTimeField(default=get_time, verbose_name='İşe Başlangıç Tarihi')
    personal_endday = models.DateTimeField(verbose_name='İşten Ayrılma Günü',default=get_time)
    personal_city = models.CharField(max_length=20, choices=PROVINCE_CHOICES, verbose_name='Personel Adres İli',default='1')
    personal_town = models.CharField(max_length=20, default='', verbose_name='Personel Adres İlçesi')
    personal_adress = models.CharField( max_length=100, default='', verbose_name='Personel Adres')
    #personal_birthday = models.DateTimeField(default='1990-12-31 00:00:00', verbose_name='Doğum Tarihi', help_text='1990-12-31 00:00:00')
    blood_type = models.CharField(max_length=20, choices=blood_type_list, default='1',verbose_name='Kan Grubu')
    health_notes = models.CharField(max_length=200, default='',verbose_name='Sağlık Notları')
    special_notes = models.CharField(max_length=200, default='',verbose_name='Özel Notlar')
    image_field = models.ImageField(upload_to='profile_pic/',default='',verbose_name='Profil Resmi')


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
        return self.personal_tcn.full_name()

    def group(self):
        return 'Personal'


class StudentInfoModel(models.Model):
    year_list=(('0','Preparation'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'))
    #city_list = (('01', 'Adana'), ('02', 'Ad\xc4\xb1yaman'), ('03', 'Afyon'), ('04', 'A\xc4\x9fr\xc4\xb1'), ('05', 'Amasya'),('06', 'Ankara'), ('07', 'Antalya'), ('08', 'Artvin'), ('09', 'Ayd\xc4\xb1n'), ('10', 'Bal\xc4\xb1kesir'),('11', 'Bilecik'), ('12', 'Bing\xc3\xb6l'), ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'),('17', '\xc3\x87anakkale'), ('18', '\xc3\x87ank\xc4\xb1r\xc4\xb1'), ('19', '\xc3\x87orum'), ('20', 'Denizli'),('21', 'Diyarbak\xc4\xb1r'), ('22', 'Edirne'), ('23', 'Elaz\xc4\xb1\xc4\x9f'), ('24', 'Erzincan'),('25', 'Erzurum'), ('26', 'Eski\xc5\x9fehir'), ('27', 'Gaziantep'), ('28', 'Giresun'),('29', 'G\xc3\xbcm\xc3\xbc\xc5\x9fhane'), ('30', 'Hakkari'), ('31', 'Hatay'), ('32', 'Isparta'), ('33', 'Mersin'),('34', '\xc4\xb0stanbul'), ('35', '\xc4\xb0zmir'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'),('39', 'K\xc4\xb1rklareli'), ('40', 'K\xc4\xb1r\xc5\x9fehir'), ('41', 'Kocaeli'), ('42', 'Konya'),('43', 'K\xc3\xbctahya'), ('44', 'Malatya'), ('45', 'Manisa'), ('46', 'Kahramanmara\xc5\x9f'), ('47', 'Mardin'),('48', 'Mu\xc4\x9fla'), ('49', 'Mu\xc5\x9f'), ('50', 'Nev\xc5\x9fehir'), ('51', 'Ni\xc4\x9fde'), ('52', 'Ordu'),('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'), ('57', 'Sinop'), ('58', 'Sivas'),('59', 'Tekirda\xc4\x9f'), ('60', 'Tokat'), ('61', 'Trabzon'), ('62', 'Tunceli'), ('63', '\xc5\x9eanl\xc4\xb1urfa'),('64', 'U\xc5\x9fak'), ('65', 'Van'), ('66', 'Yozgat'), ('67', 'Zonguldak'), ('68', 'Aksaray'), ('69', 'Bayburt'),('70', 'Karaman'), ('71', 'K\xc4\xb1r\xc4\xb1kkale'), ('72', 'Batman'), ('73', '\xc5\x9e\xc4\xb1rnak'),('74', 'Bart\xc4\xb1n'), ('75', 'Ardahan'), ('76', 'I\xc4\x9fd\xc4\xb1r'), ('77', 'Yalova'),('78', 'Karab\xc3\xbck'), ('79', 'Kilis'), ('80', 'Osmaniye'), ('81', 'D\xc3\xbczce'))
    blood_type_list = (('0', '0 rh +'), ('1', '0 rh -'), ('2', 'A rh +'), ('3', 'A rh -'), ('4', 'B rh +'), ('5', 'B rh -'),('6', 'AB rh+'), ('7', 'AB rh-'))
    student_type_list=(('0','Normal'),('1','Geçici'),('2','Misafir'))

    id = models.CharField(max_length=7,verbose_name='Öğrenci No',help_text='ID',primary_key=True,default='1701001')
    #student_tcn=models.CharField(max_length=11,blank=True)
    student_tcn=models.OneToOneField(PersonIDInfoModel,verbose_name='Öğrencinin Kimlik Numarası',unique=True)
    student_phone = PhoneNumberField(default='+905553332211',verbose_name='Telefon Numarası',max_length=13)
    student_email = models.EmailField(default='',verbose_name='Email Adresi',unique=True)
    student_regday = models.DateTimeField(default=get_time,verbose_name='Kayıt Tarihi')
    student_city = models.CharField(max_length=20,choices=PROVINCE_CHOICES,verbose_name='Adres Şehri',default='1')
    student_town = models.CharField(max_length=20,default='',verbose_name='Adres İlçesi')
    student_adress = models.CharField(max_length=100,default='',verbose_name='Adres')

    room_no = models.ForeignKey(RoomInfoModel,verbose_name='Oda Numarası',default='101')
    student_type = models.CharField(max_length=10, choices=student_type_list, default='1',verbose_name='Öğrenci Türü')
    school_name = models.CharField(max_length=50, default='',verbose_name='Okul')
    education_year = models.CharField(max_length=20, choices=year_list, default='1',verbose_name='Eğitim Yılı')
    blood_type = models.CharField(max_length=20, choices=blood_type_list, default='1',verbose_name='Kan Grubu')
    health_notes = models.CharField(max_length=200, default='',verbose_name='Sağlık Notları')
    special_notes = models.CharField(max_length=200, default='',verbose_name='Özel Notlar')
    file_field = models.ImageField(upload_to='profile_pic/',default='',verbose_name='Profil Resmi')
    student_position= models.BooleanField(verbose_name='Öğrenci Konumu',default=True)


    class Meta:
        db_table= 'student_info'

    def __str__(self):
        return self.id

    def __unicode__(self):
        return str(self.id)

    def full_name(self):
        return self.student_tcn.full_name()

    def city_name(self):
        return PROVINCE_CHOICES[int(self.student_city)-1][1]

    def education_year_name(self):
        return self.year_list[int(self.education_year)][1]

    def blood_type_name(self):
        return self.blood_type_list[int(self.blood_type)][1]

    def student_type_name(self):
        return self.student_type_list[int(self.student_type)][1]

    def tcn_list(self):
        return PersonIDInfoModel.objects.all()

    def room_list(self):
        return RoomInfoModel.objects.all()

    def city_list(self):
        return PROVINCE_CHOICES


    def group(self):
        return 'Student'



class ParentInfoModel(models.Model):
    id=models.CharField(max_length=8,primary_key=True,verbose_name='Veli No',default='1704001')
    #student_id=models.CharField(max_length=10,null=True,blank=True)
    student_id=models.ForeignKey(StudentInfoModel,unique=False,verbose_name='Öğrenci No')
    parent_name=models.CharField(max_length=20,verbose_name='Veli Adı',default='')
    parent_lastname=models.CharField(max_length=20,verbose_name='Veli Soyadı',default='')
    parent_TCN=models.CharField(max_length=11,verbose_name='Veli TCN',default='')
    parent_phone=PhoneNumberField(verbose_name='Veli Telefonu',default='')
    parent_email=models.EmailField(verbose_name='Veli Email Adresi',default='')
    relative_degree=models.CharField(max_length=20,verbose_name='Yakınlık Derecesi',default='')
    parent_job=models.CharField(max_length=20,verbose_name='Veli Mesleği',default='')

    class Meta:
        db_table='parent_info'

    def __str__(self):
        return self.parent_name

    def full_name(self):
        return '%s %s'% (self.parent_name,self.parent_lastname)

    def group(self):
        return 'Parent'
