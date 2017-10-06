    # -*- coding: utf-8 -*-
from django import forms

from .models import TransactionInfoModel,PersonAssetInfoModel,AccountInfoModel,BillInfoModel
from person_panel.models import StudentInfoModel
from user_panel.models import CompanyInfoModel

class TransactionInfoForm(forms.ModelForm):
    def __init__(self, user,POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(TransactionInfoForm, self).__init__(POST,*args, **kwargs)
        self.user=user
        self.fields['account_no'].queryset =AccountInfoModel.objects.filter(company_id=user.company_id)

    account_no=forms.ModelChoiceField(AccountInfoModel.objects.all(),label='Hesap Numarası',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    type=forms.ChoiceField(choices=TransactionInfoModel.transaction_type_list,label='İşlem Türü',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    amount=forms.CharField(max_length=10,label='İşlem Miktarı')
    time=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"pickTime": False,"startDate": "2007","class":"datetime-picker","style":"height: 30px"}),label='İşlem Zamanı')
    desc=forms.CharField(max_length=100,label='İşlem Açıklaması',required=False,empty_value=True)
    company_id=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)
    class Meta:
        model=TransactionInfoModel
        fields=[
            'account_no',
            'type',
            'amount',
            'time',
            'desc',
            'company_id',
        ]
    def clean(self):
        amount=self.cleaned_data.get('amount')
        if 0.0<float(amount)<10000.00:
            print (amount)
        else:
            self.add_error('amount','Yanlış Miktar')

    def clean_company_id(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id_id)



class PersonAssetInfoForm(forms.ModelForm):
    def __init__(self, user,POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(PersonAssetInfoForm, self).__init__(POST,*args, **kwargs)
        self.user=user
        self.fields['person'].queryset =StudentInfoModel.objects.filter(company_id=user.company_id)

    id=forms.CharField(max_length=10,label='Ödeme Planı ID',initial=str(int(PersonAssetInfoModel.objects.all().order_by('-id')[0].id)+1))
    person=forms.ModelChoiceField(StudentInfoModel.objects.all(),label='Öğrenci No',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    amount=forms.CharField(max_length=5,label='Ödenen Miktar')
    debt=forms.CharField(max_length=5,label='Ödenecek Miktar')
    period=forms.CharField(max_length=2,label='Taksit Miktarı')
    type=forms.ChoiceField(choices=PersonAssetInfoModel.asset_type_list,label='Ödeme Türü',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    desc=forms.CharField(max_length=100,label='Ödeme Planı Açıklaması',required=False,empty_value=True)
    company_id=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)
    class Meta:
        model=PersonAssetInfoModel
        fields=[
            'id',
            'person',
            'amount',
            'debt',
            'period',
            'type',
            'desc',
            'company_id',
        ]
    def clean(self):
        amount=self.cleaned_data.get('amount')
        if 0.0<float(amount)<10000.00:
            print (amount)
        else:
            self.add_error('amount','Yanlış Miktar')
        debt=self.cleaned_data.get('debt')
        if 0.0<float(debt)<10000.00:
            print (debt)
        else:
            self.add_error('debt','Yanlış Miktar')
        period=self.cleaned_data.get('period')
        if 0<int(period)<13:
            print(period)
        else:
            self.add_error('period','Yanlış Dönem')

    def clean_company_id(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id_id)


class AccountInfoForm(forms.ModelForm):
    def __init__(self, user,POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(AccountInfoForm, self).__init__(POST,*args, **kwargs)
        self.user=user

    no=forms.CharField(max_length=10,label='Hesap Numarası')
    name=forms.CharField(max_length=20,label='Hesap Adı')
    type=forms.ChoiceField(choices=AccountInfoModel.account_type_list,label='Hesap Türü',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    amount=forms.CharField(max_length=10,label='Hesap Miktarı')
    desc=forms.CharField(max_length=100,label='Hesap Açıklaması',required=False,empty_value=True)
    bank_code=forms.ChoiceField(choices=AccountInfoModel.bank_code_list,label='Banka Şubesi',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    company_id=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)
    class Meta:
        model=AccountInfoModel
        fields=[
            'no',
            'name',
            'type',
            'amount',
            'desc',
            'bank_code',
            'company_id',
        ]
    def clean(self):
        amount=self.cleaned_data.get('amount')
        if 0.0<float(amount)<100000.00:
            print (amount)
        else:
            self.add_error('amount','Yanlış Miktar')

    def clean_company_id(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id_id)


class BillInfoForm(forms.ModelForm):
    def __init__(self, user,POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(BillInfoForm, self).__init__(POST,*args, **kwargs)
        self.user=user
        #self.fields['person'].queryset =StudentInfoModel.objects.filter(company_id=user.company_id)
    id=forms.CharField(max_length=10,initial=str(int(BillInfoModel.objects.all().order_by('-id')[0].id)+1))
    type=forms.ChoiceField(choices=BillInfoModel.bill_type_list,label='Fatura Türü',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    code=forms.CharField(max_length=10,label='Fatura Kodu')
    amount=forms.CharField(max_length=10,label='Fatura Miktarı')
    period=forms.CharField(max_length=10,label='Fatura Dönemi')
    last_day=forms.DateField(widget=forms.DateInput(attrs={"pickTime": False,"startDate": "2007","class":"date-picker","style":"height: 30px"}),label='Fatura Son Ödeme Tarihi')
    address=forms.CharField(max_length=200,label='Fatura Adresi',required=False,empty_value=True)
    desc=forms.CharField(max_length=100,label='Fatura Açıklaması',required=False,empty_value=True)
    company_id=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)
    class Meta:
        model=BillInfoModel
        fields=[
            'type',
            'code',
            'amount',
            'period',
            'last_day',
            'address',
            'desc',
            'company_id',
        ]
    def clean(self):
        amount = self.cleaned_data.get('amount')
        if 0.0 < float(amount) < 10000.00:
            print(amount)
        else:
            self.add_error('amount', 'Yanlış Miktar')

    def clean_company_id(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id_id)

