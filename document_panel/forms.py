# -*- coding: utf-8 -*-
from django import forms
from .models import DocumentInfoModel,LiabilityInfoModel
from person_panel.models import StudentInfoModel
from user_panel.models import CompanyInfoModel
import datetime
from PIL import Image


class DocumentInfoForm(forms.ModelForm):
    def __init__(self, user, POST=None,FILES=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(DocumentInfoForm, self).__init__(POST,FILES,*args, **kwargs)
        self.user=user
        self.fields['person'].queryset = StudentInfoModel.objects.filter(company_id=user.company_id)

    id=forms.CharField(max_length=10,label='Dosya Numarası',)#initial=str(int(DocumentInfoModel.objects.last().id)+1))
    person=forms.ModelChoiceField(StudentInfoModel.objects.all(),label='Öğrenci Numarası',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    type=forms.ChoiceField(DocumentInfoModel.document_type_list,label='Dosya Türü',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    desc=forms.CharField(max_length=100,label='Dosya Açıklaması',required=False)
    date=forms.DateField(label='Dosya Tarihi',widget=forms.DateInput(attrs={"pickTime": False, "class": "date-picker", "style": "height: 30px"  }))
    image_field=forms.ImageField(label='Dosya',widget=forms.FileInput(),required=False)
    company_id=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)
    class Meta:
        model=DocumentInfoModel
        fields=['id',
                'person',
                'type',
                'desc',
                'date',
                'image_field',
                'company_id',
                ]
    def clean_image_field(self):
        image =self.cleaned_data.get('image_field')
        return image

    def clean(self):
        image = self.cleaned_data.get('image_field')
        #print (image.path.split('.')[-1] if '.' in image.path else None)
        if image:
            try:
                # validate content type
                main, sub = image.content_type.split('/')
                if not (main == 'image' and sub.lower() in ['jpeg', 'pjpeg', 'png', 'jpg']):
                    self.add_error('image_field','JPEG veya PNG dosyası yükleyiniz')

                # validate file size
                if len(image) > (1 * 4140 * 5520):
                    self.add_error('image_field','10 MB den düşük dosyalar yükleyiniz ')
            except AttributeError:
                img = Image.open(image)
                main, sub = 'image',img.format
                if not (main == 'image' and sub.lower() in ['jpeg', 'pjpeg', 'png', 'jpg']):
                    self.add_error('image_field','JPEG veya PNG dosyası yükleyiniz')

                # validate file size
                if len(image) > (1 * 4140 * 5520):
                    self.add_error('image_field','10 MB den düşük dosyalar yükleyiniz ')

        else:
            self.add_error('image_field','Yüklenen dosya okunamadı')



    def clean_company_id(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id_id)


class LiabilityInfoForm(forms.ModelForm):# TODO: DatetimeField'larda editleme sayfasında zamanlar kayıyor. tekrardan düzenlem yapılması gerekiyor.
    def __init__(self, user, POST=None,FILES=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(LiabilityInfoForm, self).__init__(POST,FILES,*args, **kwargs)
        self.user=user
        self.fields['person'].queryset = StudentInfoModel.objects.filter(company_id=user.company_id)

    person=forms.ModelChoiceField(StudentInfoModel.objects.all(),label='Öğrenci Numarası',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    type=forms.ChoiceField(LiabilityInfoModel.fixture_type_list,label='Emanet Türü',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    desc=forms.CharField(max_length=100,label='Emanet Açıklaması',required=False)
    give_day=forms.DateTimeField(label='Emanet Verilme Tarihi',widget=forms.DateTimeInput(attrs={'class':'datetime-picker',"pickTime": False,"style":"height: 30px"}))
    take_day=forms.DateTimeField(label='Emanet Teslim Tarihi',widget=forms.DateTimeInput(attrs={'class':'datetime-picker',"pickTime": False,"style":"height: 30px"}),required=False)
    last_day=forms.DateTimeField(label='Emanet Son Teslim Tarihi',widget=forms.DateTimeInput(attrs={'class':'datetime-picker',"pickTime": False,"style":"height: 30px"}))
    penalty=forms.CharField(max_length=5,label='Gecikme Cezası',required=False)
    company_id=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)
    class Meta:
        model = LiabilityInfoModel
        fields = ['person',
                  'type',
                  'desc',
                  'give_day',
                  'take_day',
                  'last_day',
                  'penalty',
                'company_id',
                  ]
    def clean(self):
        gived=self.cleaned_data.get('give_day')
        lastd=self.cleaned_data.get('last_day')
        taked=self.cleaned_data.get('take_day')
        if lastd and gived:
            if lastd<gived:
                self.add_error('last_day','Lütfen Geçerli Bir Tarih Giriniz')
        if taked and gived:
            if taked<gived:
                self.add_error('take_day','Lütfen Geçerli Bir Tarih Giriniz')

    def clean_penalty(self):
        lastd=self.cleaned_data.get('last_day')
        taked=self.cleaned_data.get('take_day')
        if lastd and taked:
            if lastd<taked:
                penalty= ((taked-lastd).days*2)
                print (penalty)
                return penalty
            else:
                penalty=0
        else:
            penalty=0
        return penalty

    def clean_company_id(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id_id)