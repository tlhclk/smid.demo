# -*- codingutf-8 -*-
import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from stock_panel.models import RoomInfoModel
from localflavor.tr.tr_provinces import PROVINCE_CHOICES




class PersonalInfoModel(models.Model):
    #city_list = (('01', 'Adana'), ('02', 'Ad\xc4\xb1yaman'), ('03', 'Afyon'), ('04', 'A\xc4\x9fr\xc4\xb1'), ('05', 'Amasya'),('06', 'Ankara'), ('07', 'Antalya'), ('08', 'Artvin'), ('09', 'Ayd\xc4\xb1n'), ('10', 'Bal\xc4\xb1kesir'),('11', 'Bilecik'), ('12', 'Bing\xc3\xb6l'), ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'),('17', '\xc3\x87anakkale'), ('18', '\xc3\x87ank\xc4\xb1r\xc4\xb1'), ('19', '\xc3\x87orum'), ('20', 'Denizli'),('21', 'Diyarbak\xc4\xb1r'), ('22', 'Edirne'), ('23', 'Elaz\xc4\xb1\xc4\x9f'), ('24', 'Erzincan'),('25', 'Erzurum'), ('26', 'Eski\xc5\x9fehir'), ('27', 'Gaziantep'), ('28', 'Giresun'),('29', 'G\xc3\xbcm\xc3\xbc\xc5\x9fhane'), ('30', 'Hakkari'), ('31', 'Hatay'), ('32', 'Isparta'), ('33', 'Mersin'),('34', '\xc4\xb0stanbul'), ('35', '\xc4\xb0zmir'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'),('39', 'K\xc4\xb1rklareli'), ('40', 'K\xc4\xb1r\xc5\x9fehir'), ('41', 'Kocaeli'), ('42', 'Konya'),('43', 'K\xc3\xbctahya'), ('44', 'Malatya'), ('45', 'Manisa'), ('46', 'Kahramanmara\xc5\x9f'), ('47', 'Mardin'),('48', 'Mu\xc4\x9fla'), ('49', 'Mu\xc5\x9f'), ('50', 'Nev\xc5\x9fehir'), ('51', 'Ni\xc4\x9fde'), ('52', 'Ordu'),('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'), ('57', 'Sinop'), ('58', 'Sivas'),('59', 'Tekirda\xc4\x9f'), ('60', 'Tokat'), ('61', 'Trabzon'), ('62', 'Tunceli'), ('63', '\xc5\x9eanl\xc4\xb1urfa'),('64', 'U\xc5\x9fak'), ('65', 'Van'), ('66', 'Yozgat'), ('67', 'Zonguldak'), ('68', 'Aksaray'), ('69', 'Bayburt'),('70', 'Karaman'), ('71', 'K\xc4\xb1r\xc4\xb1kkale'), ('72', 'Batman'), ('73', '\xc5\x9e\xc4\xb1rnak'),('74', 'Bart\xc4\xb1n'), ('75', 'Ardahan'), ('76', 'I\xc4\x9fd\xc4\xb1r'), ('77', 'Yalova'),('78', 'Karab\xc3\xbck'), ('79', 'Kilis'), ('80', 'Osmaniye'), ('81', 'D\xc3\xbczce'))
    blood_type_list=(('0','0 rh +'),('1','0 rh -'),('2','A rh +'),('3','A rh -'),('4','B rh +'),('5','B rh -'),('6','AB rh+'),('7','AB rh-'))
    personal_type_list=[('0','Accountant'),('1',''),('2','')]
    id = models.CharField(max_length=7,verbose_name='Personel No', help_text='ID', primary_key=True)
    personal_tcn = models.CharField(max_length=11, default='00000000000', verbose_name='Personel TC No', help_text='11 digit',unique=True)
    personal_name = models.CharField(max_length=200, default='Ahmet', verbose_name='Personel İsmi',help_text='Personal Name')
    personal_lastname = models.CharField(max_length=200, default='Yilmaz', verbose_name='Personel Soyismi',help_text='Personal Last Name')
    personal_phone = PhoneNumberField(default='+905553332211', verbose_name='Telefon Numarası', help_text='+905553332211')
    personal_email = models.EmailField(default='qwe@gam.com', verbose_name='Email Adresi', help_text='aaaaa@aaaa.aaa',unique=True)
    personal_startday = models.DateField(default=datetime.date.today, verbose_name='İşe Başlangıç Tarihi',help_text='1990-12-31')
    personal_endday = models.DateField(verbose_name='İşten Ayrılma Günü',help_text='1990-12-31',blank=True,null=True)
    personal_city = models.CharField(null=True, max_length=20, choices=PROVINCE_CHOICES, default='Ankara',verbose_name='Personel Adres İli', help_text='City Where Personal From')
    personal_town = models.CharField(null=True, max_length=20, default='yok', verbose_name='Personel Adres İlçesi',help_text='Town Where Personal From')
    personal_adress = models.CharField(null=True, max_length=50, default='yok', verbose_name='Personel Adres',help_text='Distinct, Street, Building No, Flat No')
    personal_birthday = models.DateField(default='1990-12-31', verbose_name='Doğum Tarihi', help_text='1990-12-31')
    blood_type = models.CharField(null=True,max_length=20, choices=blood_type_list, default='0 rh +',verbose_name='Kan Grubu',help_text='Blood Type')
    health_notes = models.CharField(null=True,blank=True,max_length=100, default='-',verbose_name='Sağlık Notları',help_text='Health Notes')
    special_notes = models.CharField(null=True,blank=True,max_length=100, default='-',verbose_name='Özel Notlar',help_text='Special Notes')
    image_field = models.ImageField(null=True,blank=True,upload_to='profile_pic/',default='Desktop/asd.jpg',verbose_name='Profil Resmi',help_text='Profile Image Path')


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

class PersonIDInfoModel(models.Model):
    idcard_type_list = [('1', 'Nüfus Cüzdanı'), ('2', 'TC Kimliği'), ('3', 'Ehliyet'), ('4', 'Pasaport'),('5', 'Diğer')]
    nation_list = [('1', 'Türkiye')]
    gender_list = [('1', 'Kadın'), ('2', 'Erkek')]
    medeni_hal_list = [('1', 'Bekar'), ('2', 'Evli'), ('3', 'Dul'), ('4', 'Diğer')]
    s_tcn = models.CharField(max_length=11, default='00000000000', verbose_name='TC No', help_text='11 digit',primary_key=True)
    s_name = models.CharField(max_length=50, default='Ahmet', verbose_name='İsim', help_text='Student Name')
    s_lastname = models.CharField(max_length=50, default='Yilmaz', verbose_name='Soyisim',help_text='Student Last Name')
    s_birthday = models.DateField(default='1990-12-31', verbose_name='Doğum Tarihi', help_text='1990-12-31', )
    s_birth_place = models.CharField(null=True, max_length=20, choices=PROVINCE_CHOICES, default=PROVINCE_CHOICES[0],verbose_name='Doğduğu Şehir', help_text='City Where Student Birth')
    s_father = models.CharField(max_length=50, verbose_name='Baba Adı', default='Mehmet')
    s_mother = models.CharField(max_length=50, verbose_name='Anne Adı', default='Ayse')
    s_nation = models.CharField(max_length=50, verbose_name='Uyruk', default='1', choices=nation_list,blank='True')
    s_idcard_type = models.CharField(max_length=50, verbose_name='Kimlik Türü', default='1', choices=idcard_type_list,blank='True')
    s_register_vilage = models.CharField(max_length=50, verbose_name='Kayıtlı Olduğu İl', default='1',choices=PROVINCE_CHOICES, blank='True')
    s_register_town = models.CharField(max_length=50, verbose_name='Kayıtlı Olduğu İlçe', default='yok', blank='True')
    s_register_distinct = models.CharField(max_length=50, verbose_name='Kayıtlı Olduğu Mahalle', default='olabilir',blank='True')
    s_gender = models.CharField(max_length=50, verbose_name='Cinsiyet', default='1', choices=gender_list, blank='True')
    s_nufus_cilt = models.CharField(max_length=50, verbose_name='Cilt No', default='0001', blank='True')
    s_nufus_ailesira = models.CharField(max_length=50, verbose_name='Aile Sira No', default='00001', blank='True')
    s_nufus_sirano = models.CharField(max_length=50, verbose_name='Sira No', default='0001', blank='True')
    s_medeni_hali = models.CharField(max_length=50, verbose_name='Medeni Hali', default='1', choices=medeni_hal_list,blank='True')

    class Meta:
        db_table='personid_info'

    def __str__(self):
        return self.s_tcn+'-'+self.full_name()

    def full_name(self):
        return '%s %s'% (self.s_name,self.s_lastname)

    def birth_city_name(self):
        return PROVINCE_CHOICES[int(self.s_birth_place)-1][1]

    def s_idcard_type_name(self):
        return dict(self.idcard_type_list)[self.s_idcard_type]

    def student_nation_name(self):
        return dict(self.nation_list)[self.s_nation]

    def s_gender_name(self):
        return dict(self.gender_list)[self.s_gender]

    def s_medeni_hali_name(self):
        return dict(self.medeni_hal_list)[self.s_medeni_hali]



class StudentInfoModel(models.Model):
    year_list=(('0','Preparation'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'))
    #city_list = (('01', 'Adana'), ('02', 'Ad\xc4\xb1yaman'), ('03', 'Afyon'), ('04', 'A\xc4\x9fr\xc4\xb1'), ('05', 'Amasya'),('06', 'Ankara'), ('07', 'Antalya'), ('08', 'Artvin'), ('09', 'Ayd\xc4\xb1n'), ('10', 'Bal\xc4\xb1kesir'),('11', 'Bilecik'), ('12', 'Bing\xc3\xb6l'), ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'),('17', '\xc3\x87anakkale'), ('18', '\xc3\x87ank\xc4\xb1r\xc4\xb1'), ('19', '\xc3\x87orum'), ('20', 'Denizli'),('21', 'Diyarbak\xc4\xb1r'), ('22', 'Edirne'), ('23', 'Elaz\xc4\xb1\xc4\x9f'), ('24', 'Erzincan'),('25', 'Erzurum'), ('26', 'Eski\xc5\x9fehir'), ('27', 'Gaziantep'), ('28', 'Giresun'),('29', 'G\xc3\xbcm\xc3\xbc\xc5\x9fhane'), ('30', 'Hakkari'), ('31', 'Hatay'), ('32', 'Isparta'), ('33', 'Mersin'),('34', '\xc4\xb0stanbul'), ('35', '\xc4\xb0zmir'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'),('39', 'K\xc4\xb1rklareli'), ('40', 'K\xc4\xb1r\xc5\x9fehir'), ('41', 'Kocaeli'), ('42', 'Konya'),('43', 'K\xc3\xbctahya'), ('44', 'Malatya'), ('45', 'Manisa'), ('46', 'Kahramanmara\xc5\x9f'), ('47', 'Mardin'),('48', 'Mu\xc4\x9fla'), ('49', 'Mu\xc5\x9f'), ('50', 'Nev\xc5\x9fehir'), ('51', 'Ni\xc4\x9fde'), ('52', 'Ordu'),('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'), ('57', 'Sinop'), ('58', 'Sivas'),('59', 'Tekirda\xc4\x9f'), ('60', 'Tokat'), ('61', 'Trabzon'), ('62', 'Tunceli'), ('63', '\xc5\x9eanl\xc4\xb1urfa'),('64', 'U\xc5\x9fak'), ('65', 'Van'), ('66', 'Yozgat'), ('67', 'Zonguldak'), ('68', 'Aksaray'), ('69', 'Bayburt'),('70', 'Karaman'), ('71', 'K\xc4\xb1r\xc4\xb1kkale'), ('72', 'Batman'), ('73', '\xc5\x9e\xc4\xb1rnak'),('74', 'Bart\xc4\xb1n'), ('75', 'Ardahan'), ('76', 'I\xc4\x9fd\xc4\xb1r'), ('77', 'Yalova'),('78', 'Karab\xc3\xbck'), ('79', 'Kilis'), ('80', 'Osmaniye'), ('81', 'D\xc3\xbczce'))
    blood_type_list = (('0', '0 rh +'), ('1', '0 rh -'), ('2', 'A rh +'), ('3', 'A rh -'), ('4', 'B rh +'), ('5', 'B rh -'),('6', 'AB rh+'), ('7', 'AB rh-'))
    student_type_list=(('0','Normal'),('1','Geçici'),('2','Misafir'))

    id = models.CharField(max_length=7,verbose_name='Öğrenci No',help_text='ID',primary_key=True,default='1701001')
    #student_tcn=models.CharField(max_length=11,blank=True)
    student_tcn=models.OneToOneField(PersonIDInfoModel,verbose_name='Öğrencinin Kimlik Numarası',unique=True)
    student_phone = PhoneNumberField(default='+905553332211',verbose_name='Telefon Numarası',help_text='+905553332211')
    student_email = models.EmailField(default='qwe@gam.com',verbose_name='Email Adresi',help_text='aaaaa@aaaa.aaa',unique=True)
    student_regday = models.DateField(default=datetime.date.today,verbose_name='Kayıt Tarihi',help_text='1990-12-31')
    student_city = models.CharField(null=True,max_length=20,choices=PROVINCE_CHOICES,default='Ankara',verbose_name='Adres Şehri',help_text='City Where Student From')
    student_town = models.CharField(null=True,max_length=20,default='yok',verbose_name='Adres İlçesi',help_text='Town Where Student From')
    student_adress = models.CharField(null=True,max_length=50,default='yok',verbose_name='Adres',help_text='Distinct, Street, Building No, Flat No')

    room_no = models.ForeignKey(RoomInfoModel,null=True,unique=False,verbose_name='Oda Numarası',help_text='Room Number Student Assigned',default='101')
    student_type = models.CharField(max_length=10, choices=student_type_list, default='Permanent',verbose_name='Öğrenci Türü',help_text='Student Accommodation Type')
    school_name = models.CharField(null=True,max_length=50, default='okulsuz',verbose_name='Okul',help_text='School Name')
    education_year = models.CharField(null=True,max_length=20, choices=year_list, default=year_list[0],verbose_name='Eğitim Yılı',help_text='Education Year')
    blood_type = models.CharField(null=True,max_length=20, choices=blood_type_list, default='0 rh +',verbose_name='Kan Grubu',help_text='Blood Type')
    health_notes = models.CharField(null=True,blank=True,max_length=100, default='-',verbose_name='Sağlık Notları',help_text='Health Notes')
    special_notes = models.CharField(null=True,blank=True,max_length=100, default='-',verbose_name='Özel Notlar',help_text='Special Notes')
    file_field = models.ImageField(null=True,blank=True,upload_to='profile_pic/',default='Desktop/asd.jpg',verbose_name='Profil Resmi',help_text='Add an Image')
    student_position= models.BooleanField(verbose_name='Öğrenci Konumu',help_text='In-Out',default=True)


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


    def group(self):
        return 'Student'



class ParentInfoModel(models.Model):
    id=models.CharField(max_length=50,primary_key=True,verbose_name='Veli No',help_text='Parent Id')
    #student_id=models.CharField(max_length=10,null=True,blank=True)
    student_id=models.ForeignKey(StudentInfoModel,null=False,unique=False,verbose_name='Öğrenci No')
    parent_name=models.CharField(max_length=20,null=False,verbose_name='Veli Adı',help_text='Parent Name')
    parent_lastname=models.CharField(max_length=20,null=False,verbose_name='Veli Soyadı')
    parent_TCN=models.CharField(max_length=11,null=False,verbose_name='Veli TCN',blank=True)
    parent_phone=PhoneNumberField(null=False,verbose_name='Veli Telefonu')
    parent_email=models.EmailField(null=False,verbose_name='Veli Email Adresi')
    relative_degree=models.CharField(max_length=20,null=False,verbose_name='Yakınlık Derecesi',default='Father')
    parent_job=models.CharField(max_length=20,blank=True,verbose_name='Veli Mesleği')

    class Meta:
        db_table='parent_info'

    def __str__(self):
        return self.parent_name

    def full_name(self):
        return '%s %s'% (self.parent_name,self.parent_lastname)

    def group(self):
        return 'Parent'
