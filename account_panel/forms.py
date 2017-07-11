# -*- coding: utf-8 -*-
from django import forms

from .models import TransactionInfoModel,PersonAssetInfoModel,AccountInfoModel,BillInfoModel

class TransactionInfoForm(forms.ModelForm):
    class Meta:
        model=TransactionInfoModel
        fields=[
            'transaction_no',
            'account_no',
            'transaction_type',
            'transaction_debit_credit',
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
    class Meta:
        model=BillInfoModel
        fields=[
            'bill_no',
            'bill_type',
            'bill_code',
            'bill_period',
            'bill_last_date',
            'bill_address',
            'bill_desc',
        ]