# -*- coding: utf-8 -*-
from django import forms

from .models import TransactionInfoModel,PersonAssetInfoModel,AccountInfoModel,BillInfoModel
import datetime
class TransactionInfoForm(forms.ModelForm):
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
    class Meta:
        model=PersonAssetInfoModel
        fields=[
            'asset_id',
            'person_id',
            'asset_amount',
            'asset_debt',
            'asset_desc',
            'asset_type',
        ]

class AccountInfoForm(forms.ModelForm):
    class Meta:
        model=AccountInfoModel
        fields=[
            'account_no',
            'account_name',
            'account_type',
            'account_amount',
            'account_desc',

        ]

class BillInfoForm(forms.ModelForm):
    bill_lastday=forms.DateField(initial=datetime.date.strftime(datetime.date.today(),'%d-%m-%Y'),input_formats='%Y-%m-%d')
    class Meta:
        model=BillInfoModel
        fields=[
            #'bill_no',
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