# -*- coding: utf-8 -*-
from django import forms
from .models import StudentInfoModel,ParentInfoModel,PersonalInfoModel,PersonIDInfoModel
from user_panel.models import CompanyInfoModel
from stock_panel.models import RoomInfoModel
import datetime
from phonenumber_field.formfields import PhoneNumberField
from localflavor.tr.tr_provinces import PROVINCE_CHOICES
from PIL import Image

class ParentInfoForm(forms.ModelForm):
    def __init__(self, user, POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(ParentInfoForm, self).__init__(POST,*args, **kwargs)
        self.user=user
        self.fields['person'].queryset = StudentInfoModel.objects.filter(company=user.company)

    person=forms.ModelChoiceField(StudentInfoModel.objects.all(),label='Öğrenci Numarası',widget=forms.Select(attrs={"class":"select2"}))
    name=forms.CharField(max_length=20,label='Ad')
    last_name=forms.CharField(max_length=20,label='Soyad')
    tcn=forms.CharField(max_length=11,label='Kimlik Numarası',required=False)
    phone=PhoneNumberField(label='Telefon Numarası',required=False)
    email=forms.EmailField(label='Mail Adresi',widget=forms.EmailInput(),required=False)
    relative_degree=forms.CharField(max_length=20,label='Yakınlık Derecesi',required=False)
    job=forms.CharField(max_length=20,label='İşi',required=False)
    company=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)

    class Meta:
        model=ParentInfoModel
        fields=('id',
                'person',
                'name',
                'last_name',
                'tcn',
                'phone',
                'email',
                'relative_degree',
                'job',
                'company',
                )

    def clean(self):
        tc_no=self.cleaned_data.get('tcn')
        if tc_no:
            try:
                list_tc =[int(x) for x in tc_no]
                tc10 = (sum(list_tc[0:10:2]) * 7 - sum(list_tc[1:9:2])) % 10
                tc11 = (sum(list_tc[0:9]) + tc10) % 10

                if list_tc[9] == tc10 and list_tc[10] == tc11:
                    pass
                else:
                    self.add_error('tcn','Lütfen Doğru Kimlik Numarasını Giriniz!')
            except ValueError:
                self.add_error('tcn', 'Lütfen Doğru Kimlik Numarasını Giriniz!')

    def clean_company(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id)


class PersonalInfoForm(forms.ModelForm):
    def __init__(self, user, POST=None,FILES=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(PersonalInfoForm, self).__init__(POST,FILES,*args, **kwargs)
        self.user=user
        self.fields['tcn'].queryset = PersonIDInfoModel.objects.filter(company=user.company)

    tcn=forms.ModelChoiceField(PersonIDInfoModel.objects.all(),label='Kimlik Kaydı',widget=forms.Select(attrs={"class":"select2"}))
    phone=PhoneNumberField(label='Telefon Numarası')
    email=forms.EmailField(label='Mail Adresi',widget=forms.EmailInput())
    salary=forms.CharField(label='Maaş')
    start_day=forms.DateField(label='İşe Başlama Tarihi',widget=forms.DateInput(attrs={'class':'date-picker'}),initial=datetime.datetime.today())
    end_day=forms.DateField(label='İşten Ayrılma Tarihi',widget=forms.DateInput(attrs={'class':'date-picker'}),initial=datetime.datetime.today(),required=False)
    city=forms.ChoiceField(choices=PROVINCE_CHOICES,label='İl',widget=forms.Select(attrs={"class":"select2"}),required=False)
    town=forms.CharField(max_length=20,label='İlçe',required=False)
    address=forms.CharField(max_length=100,label='Adres',required=False)
    blood_type=forms.ChoiceField(choices=PersonalInfoModel.blood_type_list,label='Emanet Türü',widget=forms.Select(attrs={"class":"select2"}),required=False)
    health_notes=forms.CharField(max_length=100,label='Sağlık Notları',required=False,widget=forms.Textarea())
    special_notes=forms.CharField(max_length=100,label='Özel Notlar',required=False,widget=forms.Textarea())
    image_field=forms.ImageField(label='Profile Resmi',widget=forms.FileInput(),required=False)
    company=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)

    class Meta:
        model=PersonalInfoModel
        fields=('id',
                'tcn',
                'phone',
                'email',
                'salary',
                'start_day',
                'end_day',
                'city',
                'town',
                'address',
                'blood_type',
                'health_notes',
                'special_notes',
                'image_field',
                'company',
                )
    def clean(self):
        salary=self.cleaned_data.get('amount')
        if 0.0<float(salary)<10000.00:
            pass
        else:
            self.add_error('salary','Yanlış Miktar')
        image = self.cleaned_data.get('image')
        if image:
            img = Image.open(image)

            # validate content type
            main, sub = image.content_type.split('/')
            if not (main == 'image' and sub.lower() in ['jpeg', 'pjpeg', 'png', 'jpg']):
                self.add_error('image','JPEG veya PNG dosyası yükleyiniz')

            # validate file size
            if len(image) > (1 * 1024 * 1024):
                self.add_error('image','10 MB den düşük dosyalar yükleyiniz ')
        else:
            self.add_error('image','Yüklenen dosya okunamadı')
        person=self.cleaned_data.get('tcn')
        if person:
            if person in PersonalInfoModel.objects.all():
                self.add_error('tcn','Seçtiğiniz Kimlik Kaydı Başka Bir Kişiye Atanmıştır. Lütfen Tekrar Seçiniz.')
            elif person in StudentInfoModel.objects.all():
                self.add_error('tcn', 'Seçtiğiniz Kimlik Kaydı Başka Bir Kişiye Atanmıştır. Lütfen Tekrar Seçiniz.')

    def clean_company(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id)


class PersonIDInfoForm(forms.ModelForm):
    def __init__(self, user, POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(PersonIDInfoForm, self).__init__(POST,*args, **kwargs)
        self.user=user

    nation=forms.ChoiceField(choices=PersonIDInfoModel.nation_list,label='Uyruğu',widget=forms.Select(attrs={"class":"select2"}))
    idcard_type=forms.ChoiceField(choices=PersonIDInfoModel.idcard_type_list,label='Kimlik Türü',widget=forms.Select(attrs={"class":"select2"}))
    gender=forms.ChoiceField(choices=PersonIDInfoModel.gender_list,label='Cinsiyeti',widget=forms.Select(attrs={"class":"select2"}))
    medeni_hali=forms.ChoiceField(choices=PersonIDInfoModel.medeni_hal_list,label='Medeni Hali',widget=forms.Select(attrs={"class":"select2"}))
    tcn=forms.CharField(max_length=11,label='Kimlik Numarası')
    name=forms.CharField(max_length=20,label='Adı')
    last_name=forms.CharField(max_length=20,label='Soyadı')
    father=forms.CharField(max_length=20,label='Baba Adı')
    mother=forms.CharField(max_length=20,label='Anne Adı')
    birth_day=forms.DateField(label='Doğum Tarihi',widget=forms.DateInput(attrs={'class':'date-picker'}),initial=datetime.datetime.today())
    birth_place=forms.ChoiceField(choices=PROVINCE_CHOICES,label='Doğum Yeri',widget=forms.Select(attrs={"class":"select2"}),required=False)
    register_vilage=forms.ChoiceField(choices=PROVINCE_CHOICES,label='Kayıtlı Olduğu İl',widget=forms.Select(attrs={"class":"select2"}),required=False)
    register_town=forms.CharField(max_length=20,label='Kayıtlı Olduğu İlçe',required=False)
    register_distinct=forms.CharField(max_length=20,label='Kayıtlı Olduğu Mahalle',required=False)
    nufus_cilt=forms.CharField(max_length=4,label='Cilt No',required=False)
    nufus_ailesira=forms.CharField(max_length=5,label='Aile Sıra No',required=False)
    nufus_sirano=forms.CharField(max_length=4,label='Sıra No',required=False)
    company=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)

    class Meta:
        model=PersonIDInfoModel
        fields=('nation',
                'idcard_type',
                'gender',
                'medeni_hali',
                'tcn',
                'name',
                'last_name',
                'father',
                'mother',
                'birth_day',
                'birth_place',
                'register_vilage',
                'register_town',
                'register_distinct',
                'nufus_cilt',
                'nufus_ailesira',
                'nufus_sirano',
                'company',
                )
    def clean(self):
        tc_no=self.cleaned_data.get('tcn')
        if tc_no:
            try:
                list_tc =[int(x) for x in tc_no]
                tc10 = (sum(list_tc[0:10:2]) * 7 - sum(list_tc[1:9:2])) % 10
                tc11 = (sum(list_tc[0:9]) + tc10) % 10

                if list_tc[9] == tc10 and list_tc[10] == tc11:
                    pass
                else:
                    self.add_error('tcn','Lütfen Doğru Kimlik Numarasını Giriniz!')
            except ValueError:
                self.add_error('tcn', 'Lütfen Doğru Kimlik Numarasını Giriniz!')

    def clean_company(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id)


class StudentInfoForm(forms.ModelForm):
    def __init__(self, user, POST=None,FILES=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(StudentInfoForm, self).__init__(POST,FILES,*args, **kwargs)
        self.user=user
        self.fields['tcn'].queryset = PersonIDInfoModel.objects.filter(company=user.company)
        self.fields['room_id'].queryset = RoomInfoModel.objects.filter(company=user.company)

    id=forms.CharField(max_length=7,label='Sözleşme No',)#initial=str(int(StudentInfoModel.objects.all().last().id)+1))
    position=forms.BooleanField(widget=forms.HiddenInput(),label='Öğrencinin Pozisyonu',required=False)
    tcn=forms.ModelChoiceField(PersonIDInfoModel.objects.all(),label='Kimlik Kaydı',widget=forms.Select(attrs={"class":"select2"}))
    phone=PhoneNumberField(label='Telefon Numarası')
    email=forms.EmailField(label='Mail Adresi',widget=forms.EmailInput(),required=False)
    start_day=forms.DateField(label='Kayıt Tarihi',widget=forms.DateInput(attrs={'class':'date-picker'}),initial=datetime.datetime.today())
    leave_day = forms.DateField(label='Ayrılış Tarihi', widget=forms.DateInput(attrs={'class': 'date-picker'}),required=False)
    city=forms.ChoiceField(choices=PROVINCE_CHOICES,label='İl',widget=forms.Select(attrs={"class":"select2"}),required=False)
    town=forms.CharField(max_length=20,label='İlçe',required=False)
    address=forms.CharField(max_length=100,label='Adres',required=False)
    room_id=forms.ModelChoiceField(RoomInfoModel.objects.all(),label='Oda Numarası',widget=forms.Select(attrs={"class":"select2"}))
    type=forms.ChoiceField(choices=StudentInfoModel.student_type_list,label='Öğrenci Tipi',widget=forms.Select(attrs={"class":"select2"}))
    school_name=forms.CharField(max_length=30,label='Okul Adı',required=False)
    education_year=forms.ChoiceField(choices=StudentInfoModel.year_list,label='Eğitim Yılı',widget=forms.Select(attrs={"class":"select2"}),required=False)
    blood_type=forms.ChoiceField(choices=StudentInfoModel.blood_type_list,label='Kan Grubu',widget=forms.Select(attrs={"class":"select2"}),required=False)
    health_notes=forms.CharField(max_length=200,label='Sağlık Notları',widget=forms.Textarea(),required=False)
    special_notes=forms.CharField(max_length=200,label='Özel Notlar',widget=forms.Textarea(),required=False)
    image_field=forms.ImageField(label='Profile Resmi',widget=forms.FileInput(),required=False)
    company=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)

    class Meta:
        model=StudentInfoModel
        fields=(
                'id',
                'position',
                'tcn',
                'phone',
                'email',
                'start_day',
                'leave_day',
                'city',
                'town',
                'address',
                'room_id',
                'type',
                'school_name',
                'education_year',
                'blood_type',
                'health_notes',
                'special_notes',
                'image_field',
                'company',
                )
    def clean(self):#kontrol edilmedi
        image = self.cleaned_data.get('image_field')
        room=self.cleaned_data.get('room_id')
        person=self.cleaned_data.get('tcn')
        if image:
            img = Image.open(image)

            # validate content type
            main, sub = image.content_type.split('/')
            if main == 'image' and sub.lower() in ['jpeg', 'pjpeg', 'png', 'jpg']:
                pass
            else:
                self.add_error('image_field','JPEG veya PNG dosyası yükleyiniz')
            # validate file size
            if len(image) > (1 * 1024 * 1024):
                self.add_error('image_field','10 MB den düşük dosyalar yükleyiniz ')

        if room:
            roomid=RoomInfoModel.objects.filter(company=self.user.company).filter(no=room)[0]
            qouta=0
            for row in StudentInfoModel.objects.filter(company=self.user.company):
                if row.room_id.id == roomid.id:
                    qouta+=1
            if qouta<int(roomid.people):
                pass
            else:
                self.add_error('room_id','Seçilen Odada Kontenjan Doludur!')
        if person:
            if person in PersonalInfoModel.objects.all():
                self.add_error('tcn','Seçtiğiniz Kimlik Kaydı Başka Bir Kişiye Atanmıştır. Lütfen Tekrar Seçiniz.')
            elif person in StudentInfoModel.objects.all():
                self.add_error('tcn', 'Seçtiğiniz Kimlik Kaydı Başka Bir Kişiye Atanmıştır. Lütfen Tekrar Seçiniz.')


    def clean_company(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id)