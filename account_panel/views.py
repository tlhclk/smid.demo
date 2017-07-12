# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import TransactionInfoModel,PersonAssetInfoModel,AccountInfoModel,BillInfoModel
from .forms import TransactionInfoForm,PersonAssetInfoForm,AccountInfoForm,BillInfoForm
from django.shortcuts import render,redirect


def options_menu(request):
    return render(request,'account_panel/option_menu.html')

def add_transaction(request):
    formtransaction=TransactionInfoForm()
    if request.method=='POST':
        formtransaction=TransactionInfoForm(request.POST)
        if formtransaction.is_valid():
            account=formtransaction.cleaned_data.get('account_no')
            amount=formtransaction.cleaned_data.get('transaction_amount')
            d_c=formtransaction.cleaned_data.get('transaction_type')
            transaction_accountsync(account,amount,d_c)
            formtransaction.save()
            return redirect('../')
    return render(request,'account_panel/default_form.html',{'form':formtransaction})

def detail_transaction(request,transaction_no):
    transaction=TransactionInfoModel.objects.get(pk=transaction_no)
    return render(request,'account_panel/detail_transaction.html',{'transaction':transaction})

def table_transaction(request):
    transaction_list=TransactionInfoModel.objects.all()
    return render(request,'account_panel/table_transaction.html',{'transaction_list':transaction_list})

def edit_transaction(request,transaction_no):
    formtransaction=TransactionInfoForm(instance=TransactionInfoModel.objects.get(pk=transaction_no))
    if request.method=='POST':
        formtransaction=TransactionInfoForm(request.POST,instance=TransactionInfoModel.objects.get(pk=transaction_no))
        if formtransaction.is_valid():
            formtransaction.save()
            return redirect('../')
    return render(request,'account_panel/default_form.html',{'form':formtransaction})

def delete_transaction(request,transaction_no):
    TransactionInfoModel.objects.get(pk=transaction_no).delete()
    return redirect('../')

def add_asset(request):
    formasset=PersonAssetInfoForm()
    if request.method=='POST':
        formasset=PersonAssetInfoForm(request.POST)
        if formasset.is_valid():
            formasset.save()
            return redirect('../')
    return render(request,'account_panel/default_form.html',{'form':formasset})

def detail_asset(request,asset_no):
    asset=PersonAssetInfoModel.objects.get(pk=asset_no)
    return render(request,'account_panel/detail_personasset.html',{'asset':asset})

def table_asset(request):
    asset_list=PersonAssetInfoModel.objects.all()
    return render(request,'account_panel/table_personasset.html',{'asset_list':asset_list})

def edit_asset(request,asset_no):
    formasset=PersonAssetInfoForm(instance=PersonAssetInfoModel.objects.get(pk=asset_no))
    if request.method=='POST':
        formasset=PersonAssetInfoForm(request.POST,instance=PersonAssetInfoModel.objects.get(pk=asset_no))
        if formasset.is_valid():
            formasset.save()
            return redirect('../')
    return render(request,'account_panel/default_form.html',{'form':formasset})

def delete_asset(request,asset_no):
    PersonAssetInfoModel.objects.get(pk=asset_no).delete()
    return redirect('../')

def add_account(request):
    formaccount=AccountInfoForm()
    if request.method=='POST':
        formaccount=AccountInfoForm(request.POST)
        if formaccount.is_valid():
            formaccount.save()
            return redirect('../')
    return render(request,'account_panel/default_form.html',{'form':formaccount})

def detail_account(request,account_no):
    account=AccountInfoModel.objects.get(pk=account_no)
    return render(request,'account_panel/detail_account.html',{'account':account})

def table_account(request):
    account_list=AccountInfoModel.objects.all()
    return render(request,'account_panel/table_account.html',{'account_list':account_list})

def edit_account(request,account_no):
    formaccount=AccountInfoForm(instance=AccountInfoModel.objects.get(pk=account_no))
    if request.method=='POST':
        formaccount=AccountInfoForm(request.POST,instance=AccountInfoModel.objects.get(pk=account_no))
        if formaccount.is_valid():
            formaccount.save()
            return redirect('../')
    return render(request,'account_panel/default_form.html',{'form':formaccount})

def delete_account(request,account_no):
    AccountInfoModel.objects.get(pk=account_no).delete()
    return redirect('../')

def add_bill(request):
    formbill=BillInfoForm()
    if request.method=='POST':
        formbill=BillInfoForm(request.POST)
        if formbill.is_valid():
            formbill.save()
            return redirect('../')
    return render(request,'account_panel/default_form.html',{'form':formbill})

def detail_bill(request,bill_no):
    bill=BillInfoModel.objects.get(pk=bill_no)
    return render(request,'account_panel/detail_bill.html',{'bill':bill})

def table_bill(request):
    bill_list=BillInfoModel.objects.all()
    return render(request,'account_panel/table_bill.html',{'bill_list':bill_list})

def edit_bill(request,bill_no):
    formbill=BillInfoForm(instance=BillInfoModel.objects.get(pk=bill_no))
    if request.method=='POST':
        formbill=BillInfoForm(request.POST,instance=BillInfoModel.objects.get(pk=bill_no))
        if formbill.is_valid():
            formbill.save()
            return redirect('../')
    return render(request,'account_panel/default_form.html',{'form':formbill})

def delete_bill(request,bill_no):
    BillInfoModel.objects.get(pk=bill_no).delete()
    return redirect('../')

def transaction_accountsync(account,amount,d_c):
    if d_c=='1' or d_c=='7':
        x=1
    else:
        x=-1
    account.account_amount=str(float(account.account_amount)+x*float(amount))
    account.save()
    return redirect('../')