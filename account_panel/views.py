# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import TransactionInfoModel,PersonAssetInfoModel,AccountInfoModel,BillInfoModel
from .forms import TransactionInfoForm,PersonAssetInfoForm,AccountInfoForm,BillInfoForm
from django.shortcuts import render,redirect,HttpResponse
import datetime
import re


def options_menu(request):
    return render(request,'account_panel/option_menu.html')

def add_transaction(request):
    if request.user.has_perm('account_panel.add_transactioninfomodel'):
        formtransaction=TransactionInfoForm()
        if request.method=='POST':
            formtransaction=TransactionInfoForm(request.POST)
            if formtransaction.is_valid():
                account=formtransaction.cleaned_data.get('account_no')
                amount=formtransaction.cleaned_data.get('transaction_amount')
                transaction_type=formtransaction.cleaned_data.get('transaction_type')
                transaction_desc=formtransaction.cleaned_data.get('transaction_desc')
                transaction_accountsync(account,amount,transaction_type,transaction_desc)
                formtransaction.save()
                return redirect('../')
        return render(request,'account_panel/default_form.html',{'form':formtransaction})
    else: return HttpResponse('You has No authorizations')

def detail_transaction(request,transaction_no):
    if request.user.has_perm('account_panel.view_transactioninfomodel'):
        transaction=TransactionInfoModel.objects.get(pk=transaction_no)
        all_fields=TransactionInfoModel._meta.get_fields()
        return render(request,'account_panel/detail_transaction.html',{'transaction':transaction})
    else: return HttpResponse('You has No authorizations')

def table_transaction(request):
    if request.user.has_perm('account_panel.view_transactioninfomodel'):
        transaction_list=TransactionInfoModel.objects.all()
        return render(request,'account_panel/table_transaction.html',{'transaction_list':transaction_list})
    else: return HttpResponse('You has No authorizations')

def edit_transaction(request,transaction_no):
    if request.user.has_perm('account_panel.change_transactioninfomodel'):
        formtransaction=TransactionInfoForm(instance=TransactionInfoModel.objects.get(pk=transaction_no))
        if request.method=='POST':
            formtransaction=TransactionInfoForm(request.POST,instance=TransactionInfoModel.objects.get(pk=transaction_no))
            if formtransaction.is_valid():
                formtransaction.save()
                return redirect('../')
        return render(request,'account_panel/default_form.html',{'form':formtransaction})
    else: return HttpResponse('You has No authorizations')

def delete_transaction(request,transaction_no):
    if request.user.has_perm('account_panel.delete_transactioninfomodel'):
        TransactionInfoModel.objects.get(pk=transaction_no).delete()
        return redirect('../')
    else: return HttpResponse('You has No authorizations')

def add_asset(request):
    if request.user.has_perm('account_panel.add_personassetinfomodel'):
        formasset=PersonAssetInfoForm()
        if request.method=='POST':
            formasset=PersonAssetInfoForm(request.POST)
            if formasset.is_valid():
                formasset.save()
                return redirect('../')
        return render(request,'account_panel/default_form.html',{'form':formasset})
    else: return HttpResponse('You Have No Auth')

def detail_asset(request,asset_no):
    if request.user.has_perm('account_panel.view_personassetinfomodel'):
        if '1701' in asset_no:
            asset=PersonAssetInfoModel.objects.filter(person_id=asset_no)[0]
        else:
            asset = PersonAssetInfoModel.objects.get(pk=asset_no)
        return render(request,'account_panel/detail_personasset.html',{'asset':asset})
    else: return HttpResponse('You Have No Auth')

def table_asset(request):
    if request.user.has_perm('account_panel.view_personassetinfomodel'):
        asset_list=PersonAssetInfoModel.objects.all()
        return render(request,'account_panel/table_personasset.html',{'asset_list':asset_list})
    else: return HttpResponse('You Have No Auth')

def edit_asset(request,asset_no):
    if request.user.has_perm('account_panel.change_personassetinfomodel'):
        formasset=PersonAssetInfoForm(instance=PersonAssetInfoModel.objects.get(pk=asset_no))
        if request.method=='POST':
            formasset=PersonAssetInfoForm(request.POST,instance=PersonAssetInfoModel.objects.get(pk=asset_no))
            if formasset.is_valid():
                formasset.save()
                return redirect('../')
        return render(request,'account_panel/default_form.html',{'form':formasset})
    else: return HttpResponse('You Have No Auth')

def delete_asset(request,asset_no):
    if request.user.has_perm('account_panel.delete_personassetinfomodel'):
        PersonAssetInfoModel.objects.get(pk=asset_no).delete()
        return redirect('../')
    else: return HttpResponse('You Have No Auth')

def add_account(request):
    if request.user.has_perm('account_panel.add_accountinfomodel'):
        formaccount=AccountInfoForm()
        if request.method=='POST':
            formaccount=AccountInfoForm(request.POST)
            if formaccount.is_valid():
                formaccount.save()
                return redirect('../')
        return render(request,'account_panel/default_form.html',{'form':formaccount})
    else: return HttpResponse('You Have No Auth')

def detail_account(request,account_no):
    if request.user.has_perm('account_panel.view_accountinfomodel'):
        account=AccountInfoModel.objects.get(pk=account_no)
        return render(request,'account_panel/detail_account.html',{'account':account})
    else: return HttpResponse('You Have No Auth')

def table_account(request):
    if request.user.has_perm('account_panel.view_accountinfomodel'):
        account_list=AccountInfoModel.objects.all()
        return render(request,'account_panel/table_account.html',{'account_list':account_list})
    else: return HttpResponse('You Have No Auth')

def edit_account(request,account_no):
    if request.user.has_perm('account_panel.view_accountinfomodel'):
        formaccount=AccountInfoForm(instance=AccountInfoModel.objects.get(pk=account_no))
        if request.method=='POST':
            formaccount=AccountInfoForm(request.POST,instance=AccountInfoModel.objects.get(pk=account_no))
            if formaccount.is_valid():
                formaccount.save()
                return redirect('../../')
        return render(request,'account_panel/default_form.html',{'form':formaccount})
    else: return HttpResponse('You Have No Auth')

def delete_account(request,account_no):
    if request.user.has_perm('account_panel.view_accountinfomodel'):
        AccountInfoModel.objects.get(pk=account_no).delete()
        return redirect('../')
    else: return HttpResponse('You Have No Auth')

def add_bill(request):
    if request.user.has_perm('account_panel.add_billinfomodel'):
        formbill=BillInfoForm()
        if request.method=='POST':
            formbill=BillInfoForm(request.POST)
            print (formbill)
            if formbill.is_valid():
                bill_transactionsync(formbill)
                formbill.save()
                return redirect('http://127.0.0.1:8000/account_panel/asset_table/')
        return render(request,'account_panel/add_bill.html',{'form':formbill,'bill_type_list':BillInfoModel.bill_type_list})
    else: return HttpResponse('You have No Auth')

def detail_bill(request,bill_no):
    if request.user.has_perm('account_panel.view_billinfomodel'):
        bill=BillInfoModel.objects.get(pk=bill_no)
        return render(request,'account_panel/detail_bill.html',{'bill':bill})
    else: return HttpResponse('You have No Auth')

def table_bill(request):
    if request.user.has_perm('account_panel.view_billinfomodel'):
        bill_list=BillInfoModel.objects.all()
        return render(request,'account_panel/table_bill.html',{'bill_list':bill_list})
    else: return HttpResponse('You have No Auth')

def edit_bill(request,bill_no):
    if request.user.has_perm('account_panel.change_billinfomodel'):
        formbill=BillInfoForm(instance=BillInfoModel.objects.get(pk=bill_no))
        if request.method=='POST':
            formbill=BillInfoForm(request.POST,instance=BillInfoModel.objects.get(pk=bill_no))
            if formbill.is_valid():
                formbill.save()
                return redirect('../')
        return render(request,'account_panel/add_bill.html',{'form':formbill,'bill_type_list':BillInfoModel.bill_type_list})
    else: return HttpResponse('You have No Auth')

def delete_bill(request,bill_no):
    if request.user.has_perm('account_panel.delete_bilinfomodel'):
        BillInfoModel.objects.get(pk=bill_no).delete()
        return redirect('../')
    else: return HttpResponse('You have No Auth')

def transaction_accountsync(account_no,amount,transaction_type,transaction_desc):
    if transaction_type=='1' or transaction_type=='7':
        x=1
    elif transaction_type=='8':
        if re.search('1701\w{3}',transaction_desc):
            print (re.search('1701\w{3}',transaction_desc).group())
            transaction_to = re.search('1701\w{3}',transaction_desc).group()
            x = 1
            asset = PersonAssetInfoModel.objects.filter(person_id=transaction_to)[0]
            asset.asset_amount = str(float(asset.asset_amount) + x * float(amount))
            asset.asset_debt = str(float(asset.asset_debt) - x * float(amount))
            asset.save()
        else:
            return HttpResponse('Error','Transaction Description has some Errors')
    else:
        x=-1
    account_no.account_amount=str(float(account_no.account_amount)+x*float(amount))
    account_no.save()
    return redirect('../')

def bill_transactionsync(formbill):
    account_no=AccountInfoModel.objects.filter(account_name='Nakit')[0]
    amount=formbill.cleaned_data.get('bill_amount')
    description=formbill.cleaned_data.get('bill_desc')
    transaction=TransactionInfoModel(account_no=account_no,transaction_type='6',transaction_amount=amount,transaction_time=datetime.datetime.now(),transaction_desc=description)
    transaction_accountsync(account_no,amount,transaction_type='6',transaction_desc=description)
    transaction.save()

