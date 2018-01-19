    # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import TransactionInfoModel,PersonAssetInfoModel,AccountInfoModel,BillInfoModel,PeriodicPaymentModel
from .forms import TransactionInfoForm,PersonAssetInfoForm,AccountInfoForm,BillInfoForm,PeriodicPaymentForm
from person_panel.models import StudentInfoModel
from django.shortcuts import render,redirect
from user_panel.models import CompanyInfoModel
import datetime
import re

def add_transaction(request,filter_no):
    if request.user.has_perm('account_panel.add_transactioninfomodel'):
        if request.method=='POST':
            formtransaction=TransactionInfoForm(user=request.user,POST=request.POST)
            if formtransaction.is_valid():
                formtransaction.save()
                formtransaction.add()
                return redirect('https://dormoni.com/account_panel/transaction_table/')
        if StudentInfoModel.objects.get(pk=filter_no):
            formtransaction = TransactionInfoForm(user=request.user,initial={'desc': filter_no})
        else:
            formtransaction = TransactionInfoForm(user=request.user)
        return render(request,'account_panel/add_transaction.html',{'form':formtransaction,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def table_transaction(request):
    if request.user.has_perm('account_panel.change_transactioninfomodel'):
        transaction_list=TransactionInfoModel.objects.filter(company=request.user.company_id)
        return render(request,'account_panel/table_transaction.html',{'transaction_list':transaction_list,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def edit_transaction(request,transaction_no):
    if request.user.has_perm('account_panel.add_transactioninfomodel'):
        formtransaction=TransactionInfoForm(user=request.user,instance=TransactionInfoModel.objects.get(pk=transaction_no,company=request.user.company_id)[0])
        if request.method=='POST':
            formtransaction=TransactionInfoForm(user=request.user,POST=request.POST,instance=TransactionInfoModel.objects.get(pk=transaction_no))
            if formtransaction.is_valid():
                formtransaction.save()# TODO: formlardaki fonksiyonlar gibibir tane eğer miktar değiştirilirse diye
                return redirect('https://dormoni.com/account_panel/transaction_table/')
        return render(request,'account_panel/add_transaction.html',{'form':formtransaction,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def delete_transaction(request,transaction_no):
    if request.user.has_perm('account_panel.add_transactioninfomodel'):
        tra=TransactionInfoModel.objects.get(pk=transaction_no,company=request.user.company_id)[0]
        TransactionInfoForm(user=request.user).remove(transaction_no)
        tra.delete()
        return redirect('https://dormoni.com/account_panel/transaction_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')

def add_asset(request):
    if request.user.has_perm('account_panel.add_personassetinfomodel'):
        formasset=PersonAssetInfoForm(user=request.user)
        if request.method=='POST':
            formasset=PersonAssetInfoForm(user=request.user,POST=request.POST)
            if formasset.is_valid():
                formasset.save()
                return redirect('https://dormoni.com/account_panel/asset_table/')
        return render(request,'account_panel/add_personasset.html',{'form':formasset,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def detail_asset(request,asset_no):
    if request.user.has_perm('account_panel.change_personassetinfomodel'):
        asset = PersonAssetInfoModel.objects.get(pk=asset_no,company=request.user.company_id)
        return render(request,'account_panel/detail_personasset.html',{'asset':asset,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def table_asset(request):
    if request.user.has_perm('account_panel.change_personassetinfomodel'):
        asset_list=PersonAssetInfoModel.objects.filter(company=request.user.company_id)
        return render(request,'account_panel/table_personasset.html',{'asset_list':asset_list,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def edit_asset(request,asset_no):
    if request.user.has_perm('account_panel.add_personassetinfomodel'):
        instance=PersonAssetInfoModel.objects.get(pk=asset_no,company=request.user.company_id)
        formasset=PersonAssetInfoForm(user=request.user,instance=instance)
        if request.method=='POST':
            formasset=PersonAssetInfoForm(user=request.user,POST=request.POST,instance=instance)
            if formasset.is_valid():
                formasset.save()
                return redirect('https://dormoni.com/account_panel/asset_table/')
        return render(request,'account_panel/add_personasset.html',{'form':formasset,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def delete_asset(request,asset_no):
    if request.user.has_perm('account_panel.add_personassetinfomodel'):
        PersonAssetInfoModel.objects.get(pk=asset_no, company=request.user.company_id).delete()
        return redirect('https://dormoni.com/account_panel/asset_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')

def add_account(request):
    if request.user.has_perm('account_panel.add_accountinfomodel'):
        formaccount=AccountInfoForm(user=request.user)
        if request.method=='POST':
            formaccount=AccountInfoForm(user=request.user,POST=request.POST)
            if formaccount.is_valid():
                formaccount.save()
                return redirect('https://dormoni.com/account_panel/account_table/')
        return render(request,'account_panel/add_account.html',{'form':formaccount,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def detail_account(request,account_no):
    if request.user.has_perm('account_panel.add_accountinfomodel'):
        account=AccountInfoModel.objects.get(pk=account_no,company=request.user.company_id)
        return render(request,'account_panel/detail_account.html',{'account':account,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def table_account(request):
    if request.user.has_perm('account_panel.add_accountinfomodel'):
        account_list=AccountInfoModel.objects.filter(company=request.user.company_id)
        return render(request,'account_panel/table_account.html',{'account_list':account_list,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def edit_account(request,account_no):
    if request.user.has_perm('account_panel.add_accountinfomodel'):
        instance=AccountInfoModel.objects.get(pk=account_no,company=request.user.company_id)
        formaccount=AccountInfoForm(user=request.user,instance=instance)
        if request.method=='POST':
            formaccount=AccountInfoForm(user=request.user,POST=request.POST,instance=instance)
            if formaccount.is_valid():
                formaccount.save()
                return redirect('https://dormoni.com/account_panel/account_table/')
        return render(request,'account_panel/add_account.html',{'form':formaccount,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def delete_account(request,account_no):
    if request.user.has_perm('account_panel.add_accountinfomodel'):
        AccountInfoModel.objects.get(pk=account_no,company=request.user.company_id).delete()
        return redirect('https://dormoni.com/account_panel/account_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')

def add_bill(request):
    if request.user.has_perm('account_panel.add_billinfomodel'):
        formbill=BillInfoForm(user=request.user)
        if request.method=='POST':
            formbill=BillInfoForm(user=request.user,POST=request.POST)
            if formbill.is_valid():
                formbill.save()
                formbill.add()
                return redirect('https://dormoni.com/account_panel/bill_table/')
        return render(request,'account_panel/add_bill.html',{'form':formbill,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def detail_bill(request,bill_no):
    if request.user.has_perm('account_panel.change_billinfomodel'):
        bill=BillInfoModel.objects.get(pk=bill_no)
        if bill.company_id==request.user.company_id:
            return render(request,'account_panel/detail_bill.html',{'bill':bill,'title':'Muhasebe'})
        else: return redirect('https://dormoni.com/account_panel/bill_table')
    else: return redirect('https://dormoni.com/user_panel/login/')

def table_bill(request):
    if request.user.has_perm('account_panel.change_billinfomodel'):
        bill_list=BillInfoModel.objects.filter(company=request.user.company_id)
        return render(request,'account_panel/table_bill.html',{'bill_list':bill_list,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def edit_bill(request,bill_no):
    if request.user.has_perm('account_panel.add_billinfomodel'):
        bill=BillInfoModel.objects.get(pk=bill_no,company=request.user.company_id)
        formbill=BillInfoForm(user=request.user,instance=bill)
        if request.method=='POST':
            formbill=BillInfoForm(user=request.user,POST=request.POST,instance=bill)
            if formbill.is_valid():
                formbill.save()#TODO: transaction editle aynı
                return redirect('https://dormoni.com/account_panel/bill_table/')
        return render(request,'account_panel/add_bill.html',{'form':formbill,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def delete_bill(request,bill_no):
    if request.user.has_perm('account_panel.add_bilinfomodel'):
        BillInfoForm(user=request.user).remove(bill_no)
        BillInfoModel.objects.get(pk=bill_no,company=request.user.company_id).delete()
        return redirect('https://dormoni.com/account_panel/bill_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')

def periodic_payment(request,month):
    if month=='':
        return redirect('https://dormoni.com/account_panel/periodic_payment/%d'%(datetime.date.today().month-1))
    if 1==1:
        if request.method == 'POST':
            formpp = PeriodicPaymentForm(user=request.user,POST=request.POST,instance=PeriodicPaymentModel.objects.get(person_asset_id=request.POST['person_asset']))
            if formpp.is_valid():
                formpp.save()
                formpp.cleaned_data.get('person_asset').amount=PeriodicPaymentModel.objects.get(person_asset_id=request.POST['person_asset']).paid()
                return redirect('https://dormoni.com/account_panel/periodic_payment/')
        all_forms = []
        for index in PeriodicPaymentModel.objects.filter(company=request.user.company_id).order_by('person_asset'):
            if int(month)<8:
                form_mount=list(PeriodicPaymentForm(user=request.user,instance=index))[int(month)+6]
            else:
                form_mount=list(PeriodicPaymentForm(user=request.user,instance=index))[int(month)-6]
            all_forms.append(((index,form_mount), PeriodicPaymentForm(user=request.user, instance=index)))

        monthnames = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim','Kasım', 'Aralık']
        return render(request,'account_panel/table_period_payment.html',{'title':'Muhasebe','all_forms':all_forms,'month':monthnames[int(month)]})