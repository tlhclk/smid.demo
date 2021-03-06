# -*- coding: utf-8 -*-
from django import forms
from .models import EventInfoModel
from user_panel.forms import CompanyInfoModel

class EventInfoForm(forms.ModelForm):
    def __init__(self, user,POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(EventInfoForm, self).__init__(POST,*args, **kwargs)
        self.user=user

    name=forms.CharField(max_length=30,label='Adı')
    start_time=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"datetime-picker"}),label='Başlama Zamanı')
    end_time=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"datetime-picker"}),label='Bitiş Zamanı')
    all_day=forms.BooleanField(required=False,label='Tüm Gün')
    place=forms.CharField(max_length=100,label='Konum',required=False)
    type=forms.ChoiceField(choices=EventInfoModel.type_list,label='Etkinlik Türü',widget=forms.Select(attrs={"class":"select2"}))
    desc=forms.CharField(max_length=200,label='Açıklama',required=False)
    company=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)
    class Meta:
        model=EventInfoModel
        fields=['name',
                'start_time',
                'end_time',
                'all_day',
                'place',
                'type',
                'desc',
                'company',
                ]

    def clean(self):
        startt=self.cleaned_data.get('start_time')
        endt=self.cleaned_data.get('end_time')
        if startt and endt:
            if endt<startt:
                self.add_error('end_time','Lütfen Geçerli Bir Tarih Giriniz')


    def clean_company(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id)