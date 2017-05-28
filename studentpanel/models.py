
import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from fixturepanel.models import RoomInfoModel


class StudentInfoModel(models.Model):
    room_number_list=[]
    for room in RoomInfoModel.objects.all():
        room_number_list.append((room.room_no,room.room_no))
    year_list=(('Prep','Preparation'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'))
    city_list = (('01', 'Adana'), ('02', 'Ad\xc4\xb1yaman'), ('03', 'Afyon'), ('04', 'A\xc4\x9fr\xc4\xb1'), ('05', 'Amasya'),('06', 'Ankara'), ('07', 'Antalya'), ('08', 'Artvin'), ('09', 'Ayd\xc4\xb1n'), ('10', 'Bal\xc4\xb1kesir'),('11', 'Bilecik'), ('12', 'Bing\xc3\xb6l'), ('13', 'Bitlis'), ('14', 'Bolu'), ('15', 'Burdur'), ('16', 'Bursa'),('17', '\xc3\x87anakkale'), ('18', '\xc3\x87ank\xc4\xb1r\xc4\xb1'), ('19', '\xc3\x87orum'), ('20', 'Denizli'),('21', 'Diyarbak\xc4\xb1r'), ('22', 'Edirne'), ('23', 'Elaz\xc4\xb1\xc4\x9f'), ('24', 'Erzincan'),('25', 'Erzurum'), ('26', 'Eski\xc5\x9fehir'), ('27', 'Gaziantep'), ('28', 'Giresun'),('29', 'G\xc3\xbcm\xc3\xbc\xc5\x9fhane'), ('30', 'Hakkari'), ('31', 'Hatay'), ('32', 'Isparta'), ('33', 'Mersin'),('34', '\xc4\xb0stanbul'), ('35', '\xc4\xb0zmir'), ('36', 'Kars'), ('37', 'Kastamonu'), ('38', 'Kayseri'),('39', 'K\xc4\xb1rklareli'), ('40', 'K\xc4\xb1r\xc5\x9fehir'), ('41', 'Kocaeli'), ('42', 'Konya'),('43', 'K\xc3\xbctahya'), ('44', 'Malatya'), ('45', 'Manisa'), ('46', 'Kahramanmara\xc5\x9f'), ('47', 'Mardin'),('48', 'Mu\xc4\x9fla'), ('49', 'Mu\xc5\x9f'), ('50', 'Nev\xc5\x9fehir'), ('51', 'Ni\xc4\x9fde'), ('52', 'Ordu'),('53', 'Rize'), ('54', 'Sakarya'), ('55', 'Samsun'), ('56', 'Siirt'), ('57', 'Sinop'), ('58', 'Sivas'),('59', 'Tekirda\xc4\x9f'), ('60', 'Tokat'), ('61', 'Trabzon'), ('62', 'Tunceli'), ('63', '\xc5\x9eanl\xc4\xb1urfa'),('64', 'U\xc5\x9fak'), ('65', 'Van'), ('66', 'Yozgat'), ('67', 'Zonguldak'), ('68', 'Aksaray'), ('69', 'Bayburt'),('70', 'Karaman'), ('71', 'K\xc4\xb1r\xc4\xb1kkale'), ('72', 'Batman'), ('73', '\xc5\x9e\xc4\xb1rnak'),('74', 'Bart\xc4\xb1n'), ('75', 'Ardahan'), ('76', 'I\xc4\x9fd\xc4\xb1r'), ('77', 'Yalova'),('78', 'Karab\xc3\xbck'), ('79', 'Kilis'), ('80', 'Osmaniye'), ('81', 'D\xc3\xbczce'))
    blood_type_list=(('O rh +','0 rh +'),('0 rh -','0 rh -'),('A rh +','A rh +'),('A rh -','A rh -'),('B rh +','B rh +'),('B rh -','B rh -'),('AB rh +','AB rh+'),('AB rh -','AB rh-'))
    student_type=(('Misafir','Misafir'),('Gecici','Gecici'),('Normal','Normal'))

    student_tcn = models.CharField(max_length=11,default='idsiz',verbose_name='TC No: ')
    student_name = models.CharField(max_length=200,default='isimsiz',verbose_name='Student Name:')
    student_lastname = models.CharField(max_length=200,default='soysuz')
    student_phone = PhoneNumberField(default='+905553332211')
    student_email = models.EmailField(default='qwe@gam.com')
    student_birthday = models.DateField('Dogum Gunu',default='1990-12-31')
    student_regday = models.DateField(default=datetime.date.today,null=True)
    student_city = models.CharField(null=True,max_length=20,choices=city_list,default='Ankara')
    student_town = models.CharField(null=True,max_length=20,default='yok')
    student_adress = models.CharField(null=True,max_length=50,default='yok')

    room_number = models.CharField(max_length=7, choices=room_number_list, null=True, default='405')
    student_type = models.CharField(max_length=10, choices=student_type, default='Gecici')
    birth_place = models.CharField(max_length=20, choices=city_list, default='Ankara')
    school_name = models.CharField(max_length=50, default='okulsuz')
    education_year = models.CharField(max_length=20, choices=year_list, default='1')
    blood_type = models.CharField(max_length=20, choices=blood_type_list, default='0 rh +')
    health_notes = models.CharField(max_length=100, null=True, default='-')
    special_notes = models.CharField(max_length=100, null=True, default='-')
    file_field = models.FileField(upload_to='profile_pic/',default=None, null=True)


    class Meta:
        db_table= 'student_info'

    def __str__(self):
        return self.student_name,self.student_lastname,self.student_email

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

