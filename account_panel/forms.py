# -*- coding: utf-8 -*-
from django import forms

from .models import TransactionInfoModel,PersonAssetInfoModel,AccountInfoModel,BillInfoModel
from person_panel.models import StudentInfoModel

import datetime
class TransactionInfoForm(forms.ModelForm):
    account_no=forms.ModelChoiceField(AccountInfoModel.objects.all(),label='Hesap Numarası',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    transaction_type=forms.ChoiceField(choices=TransactionInfoModel.transaction_type_list,label='İşlem Türü',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    transaction_amount=forms.CharField(max_length=10,label='İşlem Miktarı')
    transaction_time=forms.DateTimeField(input_formats='%Y-%m-%d %H:%M:%S',widget=forms.DateTimeInput(attrs={"pickTime": False,"startDate": "2007","class":"datetime-picker","style":"height: 30px"}),label='İşlem Zamanı')
    transaction_desc=forms.CharField(max_length=100,label='İşlem Açıklaması',required=False,empty_value=True)
    class Meta:
        model=TransactionInfoModel
        fields=[
            #'transaction_no',
            'account_no',
            'transaction_type',
            'transaction_amount',
            'transaction_time',
            'transaction_desc',
        ]


class PersonAssetInfoForm(forms.ModelForm):
    person_id=forms.ModelChoiceField(StudentInfoModel.objects.all(),label='Öğrenci No',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    asset_amount=forms.CharField(max_length=5,label='Ödenen Miktar')
    asset_debt=forms.CharField(max_length=5,label='Ödenecek Miktar')
    asset_period=forms.CharField(max_length=2,label='Taksit Miktarı')
    asset_type=forms.ChoiceField(choices=PersonAssetInfoModel.asset_type_list,label='Ödeme Türü',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    asset_desc=forms.CharField(max_length=100,label='Ödeme Planı Açıklaması',required=False,empty_value=True)
    class Meta:
        model=PersonAssetInfoModel
        fields=[
            'asset_id',
            'person_id',
            'asset_amount',
            'asset_debt',
            'asset_period',
            'asset_type',
            'asset_desc',
        ]

    def asset_type_list(self):
        return PersonAssetInfoModel.asset_type_list

class AccountInfoForm(forms.ModelForm):
    account_no=forms.CharField(max_length=10,label='Hesap Numarası')
    account_name=forms.CharField(max_length=20,label='Hesap Adı')
    account_type=forms.ChoiceField(choices=AccountInfoModel.account_type_list,widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}),label='Hesap türü')
    account_amount=forms.CharField(max_length=10,label='Hesap Müktarı')
    account_desc=forms.CharField(max_length=100,label='Hesap Açıklaması')
    account_bank=forms.ChoiceField(choices=AccountInfoModel.bank_code,label='Banka Kodu',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    class Meta:
        model=AccountInfoModel
        fields=[
            'account_no',
            'account_name',
            'account_type',
            'account_amount',
            'account_desc',
            'account_bank',
        ]

class BillInfoForm(forms.ModelForm):
    bill_type=forms.ChoiceField(choices=BillInfoModel.bill_type_list,label='Fatura Türü',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    bill_code=forms.CharField(max_length=10,label='Fatura Kodu')
    bill_amount=forms.CharField(max_length=10,label='Fatura Miktarı')
    bill_period=forms.CharField(max_length=10,label='Fatura Dönemi')
    bill_lastday=forms.DateField(input_formats='%Y-%m-%d',widget=forms.DateInput(attrs={"pickTime": False,"startDate": "2007","class":"date-picker","style":"height: 30px"}),label='Fatura Son Ödeme Tarihi')
    bill_address=forms.CharField(max_length=200,label='Fatura Adresi')
    bill_desc=forms.CharField(max_length=100,label='Fatura Açıklaması')
    class Meta:
        model=BillInfoModel
        fields=[
            'bill_type',
            'bill_code',
            'bill_amount',
            'bill_period',
            'bill_lastday',
            'bill_address',
            'bill_desc',
        ]

class MoneyTransferForm(forms.Form):
    from_account=forms.ModelChoiceField(AccountInfoModel)
    to_account=forms.ModelChoiceField(AccountInfoModel)
    transfer_type=forms.ChoiceField(TransactionInfoModel.transaction_type_list)
    transfer_amount=forms.CharField(max_length=10)
    transfer_datetime=forms.DateTimeField(widget=forms.SplitDateTimeWidget)
    transfer_desc=forms.CharField(max_length=100)

    class Meta:
        fields=[
            'from_account',
            'to_account',
            'transfer_type',
            'transfer_amount',
            'transfer_datetime',
            'transfer_desc',
                ]
    def check_to_account(self):
        pass