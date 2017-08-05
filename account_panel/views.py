# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import TransactionInfoModel,PersonAssetInfoModel,AccountInfoModel,BillInfoModel,StudentInfoModel
from .forms import TransactionInfoForm,PersonAssetInfoForm,AccountInfoForm,BillInfoForm
from django.shortcuts import render,redirect,HttpResponse
import datetime
import re
def add_transaction(request,filter_no):
    if request.user.has_perm('account_panel.add_transactioninfomodel'):
        if filter_no!='':
            if filter_no[:4]=='1701':
                formtransaction = TransactionInfoForm(initial={'transaction_desc': filter_no})
            else:
                formtransaction=TransactionInfoForm(initial={'account_no':filter_no})
        else:
            formtransaction = TransactionInfoForm()
        if request.method=='POST':
            formtransaction=TransactionInfoForm(request.POST)
            if formtransaction.is_valid():
                account=formtransaction.cleaned_data.get('account_no')
                amount=formtransaction.cleaned_data.get('transaction_amount')
                transaction_type=formtransaction.cleaned_data.get('transaction_type')
                transaction_desc=formtransaction.cleaned_data.get('transaction_desc')
                transaction_accountsync(account,amount,transaction_type,transaction_desc)
                formtransaction.save()
                return redirect('http://www.dormoni.com/account_panel/transaction_table/')
        return render(request,'account_panel/add_transaction.html',{'form':formtransaction,'transaction_type_list':TransactionInfoModel.transaction_type_list,'title':'Yeni İşlem Kaydı'})
    else: return redirect('http://www.dormoni.com/home/')

def detail_transaction(request,transaction_no):
    if request.user.has_perm('account_panel.view_transactioninfomodel'):
        transaction=TransactionInfoModel.objects.get(pk=transaction_no)
        return render(request,'account_panel/detail_transaction.html',{'transaction':transaction,'title':'İşlem Detayı'})
    else: return redirect('http://www.dormoni.com/home/')

def table_transaction(request,filter_no):
    if request.user.has_perm('account_panel.view_transactioninfomodel'):
        if filter_no!='':
            if filter_no[:4]=='1701':
                transaction_list = TransactionInfoModel.objects.filter(transaction_desc__contains=filter_no)
                return render(request, 'account_panel/table_transaction.html', {'transaction_list': transaction_list,'title':'İşlem Geçmişi'})
            elif filter_no[:4]=='1713':
                transaction_list = TransactionInfoModel.objects.filter(transaction_type='6')
                return render(request, 'account_panel/table_transaction.html', {'transaction_list': transaction_list,'title':'İşlem Geçmişi'})
            else:
                transaction_list=TransactionInfoModel.objects.filter(account_no=filter_no)
                return render(request,'account_panel/table_transaction.html',{'transaction_list':transaction_list,'title':'İşlem Geçmişi'})
        else:
            transaction_list=TransactionInfoModel.objects.all()
            return render(request,'account_panel/table_transaction.html',{'transaction_list':transaction_list,'title':'İşlem Geçmişi'})

    else: return redirect('http://www.dormoni.com/home/')

def edit_transaction(request,transaction_no):
    if request.user.has_perm('account_panel.change_transactioninfomodel'):
        formtransaction=TransactionInfoForm(instance=TransactionInfoModel.objects.get(pk=transaction_no))
        if request.method=='POST':
            formtransaction=TransactionInfoForm(request.POST,instance=TransactionInfoModel.objects.get(pk=transaction_no))
            if formtransaction.is_valid():
                formtransaction.save()
                return redirect('http://www.dormoni.com/account_panel/transaction_table/')
        return render(request,'account_panel/add_transaction.html',{'form':formtransaction,'title':'İşlemi Düzenleme'})
    else: return redirect('http://www.dormoni.com/home/')

def delete_transaction(request,transaction_no):
    if request.user.has_perm('account_panel.delete_transactioninfomodel'):
        TransactionInfoModel.objects.get(pk=transaction_no).delete()
        return redirect('http://www.dormoni.com/account_panel/transaction_table/')
    else: return redirect('http://www.dormoni.com/home/')

def add_asset(request):
    if request.user.has_perm('account_panel.add_personassetinfomodel'):
        new_id=str(int(PersonAssetInfoModel.objects.all().order_by('-asset_id')[0].asset_id)+1)
        formasset=PersonAssetInfoForm(initial={'asset_id':new_id})
        if request.method=='POST':
            formasset=PersonAssetInfoForm(request.POST)
            if formasset.is_valid():
                formasset.save()
                return redirect('http://www.dormoni.com/account_panel/asset_table/')
        return render(request,'account_panel/add_personasset.html',{'form':formasset,'person_list':StudentInfoModel.objects.all(),'title':'Yeni Ödeme Planı Kaydı'})
    else: return redirect('http://www.dormoni.com/home/')

def detail_asset(request,asset_no):
    if request.user.has_perm('account_panel.view_personassetinfomodel'):
        if '1701' in asset_no or '1703' in asset_no:
            asset=PersonAssetInfoModel.objects.filter(person_id=asset_no)[0]
        else:
            asset = PersonAssetInfoModel.objects.get(pk=asset_no)
        return render(request,'account_panel/detail_personasset.html',{'asset':asset,'title':'Ödeme Planı Detayı'})
    else: return redirect('http://www.dormoni.com/home/')

def table_asset(request):
    if request.user.has_perm('account_panel.view_personassetinfomodel'):
        asset_list=PersonAssetInfoModel.objects.all()
        return render(request,'account_panel/table_personasset.html',{'asset_list':asset_list,'title':'Ödeme Planı Tablosu'})
    else: return redirect('http://www.dormoni.com/home/')

def edit_asset(request,asset_no):
    if request.user.has_perm('account_panel.change_personassetinfomodel'):
        formasset=PersonAssetInfoForm(instance=PersonAssetInfoModel.objects.get(pk=asset_no))
        if request.method=='POST':
            formasset=PersonAssetInfoForm(request.POST,instance=PersonAssetInfoModel.objects.get(pk=asset_no))
            if formasset.is_valid():
                formasset.save()
                return redirect('http://www.dormoni.com/account_panel/asset_table/')
        return render(request,'account_panel/add_personasset.html',{'form':formasset,'title':'Ödeme Planı Düzenleme','person_list':StudentInfoModel.objects.all()})
    else: return redirect('http://www.dormoni.com/home/')

def delete_asset(request,asset_no):
    if request.user.has_perm('account_panel.delete_personassetinfomodel'):
        PersonAssetInfoModel.objects.get(pk=asset_no).delete()
        return redirect('http://www.dormoni.com/account_panel/asset_table/')
    else: return redirect('http://www.dormoni.com/home/')

def add_account(request):
    if request.user.has_perm('account_panel.add_accountinfomodel'):
        formaccount=AccountInfoForm()
        if request.method=='POST':
            formaccount=AccountInfoForm(request.POST)
            if formaccount.is_valid():
                formaccount.save()
                return redirect('http://www.dormoni.com/account_panel/account_table/')
        return render(request,'account_panel/add_account.html',{'form':formaccount,'title':'Yeni Hesap Kaydı'})
    else: return redirect('http://www.dormoni.com/home/')

def detail_account(request,account_no):
    if request.user.has_perm('account_panel.view_accountinfomodel'):
        account=AccountInfoModel.objects.get(pk=account_no)
        return render(request,'account_panel/detail_account.html',{'account':account,'title':'Hesap Özeti'})
    else: return redirect('http://www.dormoni.com/home/')

def table_account(request):
    if request.user.has_perm('account_panel.view_accountinfomodel'):
        account_list=AccountInfoModel.objects.all()
        return render(request,'account_panel/table_account.html',{'account_list':account_list,'title':'Hesap Tablosu'})
    else: return redirect('http://www.dormoni.com/home/')

def edit_account(request,account_no):
    if request.user.has_perm('account_panel.view_accountinfomodel'):
        formaccount=AccountInfoForm(instance=AccountInfoModel.objects.get(pk=account_no))
        if request.method=='POST':
            formaccount=AccountInfoForm(request.POST,instance=AccountInfoModel.objects.get(pk=account_no))
            if formaccount.is_valid():
                formaccount.save()
                return redirect('http://www.dormoni.com/account_panel/account_table/')
        return render(request,'account_panel/add_account.html',{'form':formaccount,'title':'Hesap Düzenleme'})
    else: return redirect('http://www.dormoni.com/home/')

def delete_account(request,account_no):
    if request.user.has_perm('account_panel.view_accountinfomodel'):
        AccountInfoModel.objects.get(pk=account_no).delete()
        return redirect('http://www.dormoni.com/account_panel/account_table/')
    else: return redirect('http://www.dormoni.com/home/')

def add_bill(request):
    if request.user.has_perm('account_panel.add_billinfomodel'):
        new_id=str(int(BillInfoModel.objects.all().order_by('-id')[0].id)+1)
        formbill=BillInfoForm(initial={'id':new_id})
        if request.method=='POST':
            formbill=BillInfoForm(request.POST)
            if formbill.is_valid():
                bill_transactionsync(formbill)
                formbill.save()
                return redirect('http://www.dormoni.com/account_panel/asset_table/')
        return render(request,'account_panel/add_bill.html',{'form':formbill,'bill_type_list':BillInfoModel.bill_type_list,'title':'Yeni Fatura Kaydı'})
    else: return redirect('http://www.dormoni.com/home/')

def detail_bill(request,bill_no):
    if request.user.has_perm('account_panel.view_billinfomodel'):
        bill=BillInfoModel.objects.get(pk=bill_no)
        return render(request,'account_panel/detail_bill.html',{'bill':bill,'title':'Fatura Detayı'})
    else: return redirect('http://www.dormoni.com/home/')

def table_bill(request):
    if request.user.has_perm('account_panel.view_billinfomodel'):
        bill_list=BillInfoModel.objects.all()
        return render(request,'account_panel/table_bill.html',{'bill_list':bill_list,'title':'Fatura Tablosu'})
    else: return redirect('http://www.dormoni.com/home/')

def edit_bill(request,bill_no):
    if request.user.has_perm('account_panel.change_billinfomodel'):
        formbill=BillInfoForm(instance=BillInfoModel.objects.get(pk=bill_no))
        if request.method=='POST':
            formbill=BillInfoForm(request.POST,instance=BillInfoModel.objects.get(pk=bill_no))
            if formbill.is_valid():
                formbill.save()
                return redirect('http://www.dormoni.com/account_panel/bill_table/')
        return render(request,'account_panel/add_bill.html',{'form':formbill,'bill_type_list':BillInfoModel.bill_type_list,'title':'Fatura Düzenleme'})
    else: return redirect('http://www.dormoni.com/home/')

def delete_bill(request,bill_no):
    if request.user.has_perm('account_panel.delete_bilinfomodel'):
        BillInfoModel.objects.get(pk=bill_no).delete()
        return redirect('http://www.dormoni.com/account_panel/bill_table/')
    else: return redirect('http://www.dormoni.com/home/')

def transaction_accountsync(account_no,amount,transaction_type,transaction_desc):
    if transaction_type=='1' or transaction_type=='7':
        x=1
    elif transaction_type=='8':
        if re.search('1701\w{3}',transaction_desc):
            transaction_to = re.search('1701\w{3}',transaction_desc).group()
            x = 1
            asset = PersonAssetInfoModel.objects.filter(person_id=transaction_to)[0]
            asset.asset_amount = str(float(asset.asset_amount) + x * float(amount))
            asset.asset_debt = str(float(asset.asset_debt) - x * float(amount))
            asset.save()
        else:
            return redirect('http://www.dormoni.com/home/')
    else:
        x=-1
    account_no.account_amount=str(float(account_no.account_amount)+x*float(amount))
    account_no.save()

def bill_transactionsync(formbill):
    account_no=AccountInfoModel.objects.filter(account_name='Nakit')[0]
    amount=formbill.cleaned_data.get('bill_amount')
    description=formbill.cleaned_data.get('bill_desc')
    transaction=TransactionInfoModel(account_no=account_no,transaction_type='6',transaction_amount=amount,transaction_time=datetime.datetime.now(),transaction_desc=description)
    transaction_accountsync(account_no,amount,transaction_type='6',transaction_desc=description)
    transaction.save()

