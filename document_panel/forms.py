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
        self.fields['person'].queryset = StudentInfoModel.objects.filter(company=user.company)

    person=forms.ModelChoiceField(StudentInfoModel.objects.all(),label='Öğrenci Numarası',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    type=forms.ChoiceField(choices=DocumentInfoModel.document_type_list,label='Dosya Türü',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    desc=forms.CharField(max_length=100,label='Dosya Açıklaması',required=False)
    date=forms.DateField(label='Dosya Tarihi',widget=forms.DateInput(attrs={"pickTime": False, "class": "date-picker", "style": "height: 30px"  }))
    image_field=forms.ImageField(label='Dosya',widget=forms.FileInput(),required=False)
    company=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)

    class Meta:
        model=DocumentInfoModel
        fields=['id',
                'person',
                'type',
                'desc',
                'date',
                'image_field',
                'company',
                ]

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

    def clean_company(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id)


class LiabilityInfoForm(forms.ModelForm):
    def __init__(self, user, POST=None,FILES=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(LiabilityInfoForm, self).__init__(POST,FILES,*args, **kwargs)
        self.user=user
        self.fields['person'].queryset = StudentInfoModel.objects.filter(company=user.company)

    person=forms.ModelChoiceField(StudentInfoModel.objects.all(),label='Öğrenci Numarası',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    type=forms.ChoiceField(choices=LiabilityInfoModel.fixture_type_list,label='Emanet Türü',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    desc=forms.CharField(max_length=100,label='Emanet Açıklaması',required=False)
    give_day=forms.DateTimeField(label='Emanet Verilme Tarihi',widget=forms.DateTimeInput(attrs={'class':'datetime-picker'}))
    take_day=forms.DateTimeField(label='Emanet Teslim Tarihi',widget=forms.DateTimeInput(attrs={'class':'datetime-picker'}),required=False)
    last_day=forms.DateTimeField(label='Emanet Son Teslim Tarihi',widget=forms.DateTimeInput(attrs={'class':'datetime-picker'}))
    penalty=forms.CharField(max_length=5,label='Gecikme Cezası',required=False)
    company=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)
    class Meta:
        model = LiabilityInfoModel
        fields = ['person',
                  'type',
                  'desc',
                  'give_day',
                  'take_day',
                  'last_day',
                  'penalty',
                'company',
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
        penalty=self.cleaned_data.get('penalty')
        if float(penalty)==0.0:
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

    def clean_company(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id)