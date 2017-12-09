# -*- coding: utf-8 -*-
from django import forms
from .models import FixtureInfoModel,RoomInfoModel
from user_panel.models import CompanyInfoModel


class FixtureInfoForm(forms.ModelForm):
    def __init__(self, user, POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(FixtureInfoForm, self).__init__(POST,*args, **kwargs)
        self.user=user
        self.fields['room'].queryset = RoomInfoModel.objects.filter(company_id=user.company_id)
    no=forms.CharField(max_length=10,label='Eşya Kodu',)#initial=str(int(FixtureInfoModel.objects.last().no)+1))
    room=forms.ModelChoiceField(RoomInfoModel.objects.all(),label='Oda Numarası',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    type=forms.ChoiceField(FixtureInfoModel.fixture_type_list,label='Eşya Tipi',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    notes=forms.CharField(max_length=100,label='Eşya Notları',required=False)
    image_field=forms.ImageField(label='Eşya Resmi',widget=forms.FileInput(),required=False)
    company_id=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)
    class Meta:
        model=FixtureInfoModel
        fields=('no',
                'room',
                'type',
                'notes',
                'image_field',
                'company_id',
                )
    def clean(self):
        image = self.cleaned_data.get('image')
        if image:

            # validate content type
            main, sub = image.content_type.split('/')
            if not (main == 'image' and sub.lower() in ['jpeg', 'pjpeg', 'png', 'jpg']):
                self.add_error('image','JPEG veya PNG dosyası yükleyiniz')

            # validate file size
            if len(image) > (1 * 1024 * 1024):
                self.add_error('image','10 MB den düşük dosyalar yükleyiniz ')
        else:
            self.add_error('image','Yüklenen dosya okunamadı')


    def clean_company_id(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id_id)


class RoomInfoForm(forms.ModelForm):
    def __init__(self, user, POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(RoomInfoForm, self).__init__(POST,*args, **kwargs)
        self.user=user
    id=forms.CharField(widget=forms.HiddenInput(),required=False)
    no=forms.CharField(max_length=4,label='Oda Numarası')
    floor=forms.CharField(max_length=2,label='Oda Katı',required=False)
    people=forms.ChoiceField(RoomInfoModel.room_people_list,label='Kişi Sayısı',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    type=forms.ChoiceField(RoomInfoModel.room_type_list,label='Oda Tipi',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    desc=forms.CharField(max_length=100,label='Oda Açıklması',required=False)
    company_id=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)
    class Meta:
        model=RoomInfoModel
        fields=('id',
                'no',
                'floor',
                'people',
                'type',
                'desc',
                'company_id',
                )

    def clean_id(self):
        if self.cleaned_data.get('id'):
            return self.cleaned_data.get('id')
        else:
            room_list=RoomInfoModel.objects.all()
            if len(room_list)!=0:
                return str(int(RoomInfoModel.objects.last().id)+1)
            else:
                return '1'


    def clean_company_id(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id_id)
