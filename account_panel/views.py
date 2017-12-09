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
                account=formtransaction.cleaned_data.get('account_no')
                amount=formtransaction.cleaned_data.get('amount')
                transaction_type=formtransaction.cleaned_data.get('type')
                transaction_desc=formtransaction.cleaned_data.get('desc')
                time=formtransaction.cleaned_data.get('time')
                transaction_accountsync(account,amount,transaction_type,transaction_desc,time)
                formtransaction.save()
                return redirect('https://dormoni.com/account_panel/transaction_table/')
        if StudentInfoModel.objects.get(pk=filter_no):
            formtransaction = TransactionInfoForm(user=request.user,initial={'desc': filter_no})
        elif filter_no=='':
            formtransaction = TransactionInfoForm(user=request.user, POST=None)
        else:
            formtransaction = TransactionInfoForm(user=request.user,initial={'account_no': AccountInfoModel.objects.get(pk=filter_no)})
        return render(request,'account_panel/add_transaction.html',{'form':formtransaction,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def table_transaction(request,filter_no):
    if request.user.has_perm('account_panel.add_transactioninfomodel'):
        transaction_list=TransactionInfoModel.objects.filter(company_id=request.user.company_id_id)#
        if filter_no!='':
            if filter_no[:4]=='1701':
                transaction_list = transaction_list.filter(desc__contains=filter_no)
                return render(request, 'account_panel/table_transaction.html', {'transaction_list': transaction_list,'title':'%s Kişisine Ait İşlem Geçmişi'%filter_no})
            elif filter_no[:4]=='1713':
                transaction_list = transaction_list.filter(type='6').filter(company_id=request.user.company_id_id)
                return render(request, 'account_panel/table_transaction.html', {'transaction_list': transaction_list,'title':'%s Türüne Ait İşlem Geçmişi'%filter_no})
            else:
                transaction_list=transaction_list.filter(account_no=filter_no)
                return render(request,'account_panel/table_transaction.html',{'transaction_list':transaction_list,'title':'Muhasebe'})
        else:
            return render(request,'account_panel/table_transaction.html',{'transaction_list':transaction_list,'title':'Muhasebe'})

    else: return redirect('https://dormoni.com/user_panel/login/')

def edit_transaction(request,transaction_no):
    if request.user.has_perm('account_panel.change_transactioninfomodel') and TransactionInfoModel.objects.get(pk=transaction_no).company_id_id==request.user.company_id_id:
        formtransaction=TransactionInfoForm(user=request.user,instance=TransactionInfoModel.objects.get(pk=transaction_no))
        if request.method=='POST':
            formtransaction=TransactionInfoForm(user=request.user,POST=request.POST,instance=TransactionInfoModel.objects.get(pk=transaction_no))
            if formtransaction.is_valid():
                formtransaction.save()
                return redirect('https://dormoni.com/account_panel/transaction_table/')
        return render(request,'account_panel/add_transaction.html',{'form':formtransaction,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def delete_transaction(request,transaction_no):
    if request.user.has_perm('account_panel.delete_transactioninfomodel') and TransactionInfoModel.objects.get(pk=transaction_no).company_id_id==request.user.company_id_id:
        tra=TransactionInfoModel.objects.get(pk=transaction_no)
        transaction_accountsync(tra.account_no,-float(tra.amount),tra.type,tra.desc)
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
    if request.user.has_perm('account_panel.add_personassetinfomodel'):
        if len(PersonAssetInfoModel.objects.filter(person=asset_no))!=0:
            asset=PersonAssetInfoModel.objects.filter(person=asset_no)[0]
        else:
            asset = PersonAssetInfoModel.objects.get(pk=asset_no)
        if asset.company_id_id==request.user.company_id_id:
            return render(request,'account_panel/detail_personasset.html',{'asset':asset,'title':'Muhasebe'})
        else: return redirect('https://dormoni.com/account_panel/asset_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')

def table_asset(request):
    if request.user.has_perm('account_panel.add_personassetinfomodel'):
        asset_list=PersonAssetInfoModel.objects.filter(company_id=request.user.company_id_id)
        return render(request,'account_panel/table_personasset.html',{'asset_list':asset_list,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def edit_asset(request,asset_no):
    if request.user.has_perm('account_panel.change_personassetinfomodel') and PersonAssetInfoModel.objects.get(pk=asset_no).company_id_id==request.user.company_id_id:
        formasset=PersonAssetInfoForm(user=request.user,instance=PersonAssetInfoModel.objects.get(pk=asset_no))
        if request.method=='POST':
            formasset=PersonAssetInfoForm(user=request.user,POST=request.POST,instance=PersonAssetInfoModel.objects.get(pk=asset_no))
            if formasset.is_valid():
                formasset.save()
                return redirect('https://dormoni.com/account_panel/asset_table/')
        return render(request,'account_panel/add_personasset.html',{'form':formasset,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def delete_asset(request,asset_no):
    if request.user.has_perm('account_panel.delete_personassetinfomodel')and PersonAssetInfoModel.objects.get(pk=asset_no).company_id_id==request.user.company_id_id:
        PersonAssetInfoModel.objects.get(pk=asset_no).delete()
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
        account=AccountInfoModel.objects.get(pk=account_no)
        if account.company_id_id==request.user.company_id_id:
            return render(request,'account_panel/detail_account.html',{'account':account,'title':'Muhasebe'})
        else: return redirect('https://dormoni.com/account_panel/account_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')

def table_account(request):
    if request.user.has_perm('account_panel.add_accountinfomodel'):
        account_list=AccountInfoModel.objects.filter(company_id=request.user.company_id_id)
        return render(request,'account_panel/table_account.html',{'account_list':account_list,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def edit_account(request,account_no):
    if request.user.has_perm('account_panel.add_accountinfomodel') and AccountInfoModel.objects.get(pk=account_no).company_id_id==request.user.company_id_id:
        formaccount=AccountInfoForm(user=request.user,instance=AccountInfoModel.objects.get(pk=account_no))
        if request.method=='POST':
            formaccount=AccountInfoForm(user=request.user,POST=request.POST,instance=AccountInfoModel.objects.get(pk=account_no))
            if formaccount.is_valid():
                formaccount.save()
                return redirect('https://dormoni.com/account_panel/account_table/')
        return render(request,'account_panel/add_account.html',{'form':formaccount,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def delete_account(request,account_no):
    if request.user.has_perm('account_panel.add_accountinfomodel') and AccountInfoModel.objects.get(pk=account_no).company_id_id==request.user.company_id_id:
        AccountInfoModel.objects.get(pk=account_no).delete()
        return redirect('https://dormoni.com/account_panel/account_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')

def add_bill(request):
    if request.user.has_perm('account_panel.add_billinfomodel'):
        formbill=BillInfoForm(user=request.user)
        if request.method=='POST':
            formbill=BillInfoForm(user=request.user,POST=request.POST)
            if formbill.is_valid():
                bill_transactionsync(formbill,request)
                formbill.save()
                return redirect('https://dormoni.com/account_panel/bill_table/')
        return render(request,'account_panel/add_bill.html',{'form':formbill,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def detail_bill(request,bill_no):
    if request.user.has_perm('account_panel.add_billinfomodel'):
        bill=BillInfoModel.objects.get(pk=bill_no)
        if bill.company_id_id==request.user.company_id_id:
            return render(request,'account_panel/detail_bill.html',{'bill':bill,'title':'Muhasebe'})
        else: return redirect('https://dormoni.com/account_panel/bill_table')
    else: return redirect('https://dormoni.com/user_panel/login/')

def table_bill(request):
    if request.user.has_perm('account_panel.add_billinfomodel'):
        bill_list=BillInfoModel.objects.filter(company_id=request.user.company_id_id)
        return render(request,'account_panel/table_bill.html',{'bill_list':bill_list,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def edit_bill(request,bill_no):
    if request.user.has_perm('account_panel.change_billinfomodel') and BillInfoModel.objects.get(pk=bill_no).company_id_id==request.user.company_id_id:
        formbill=BillInfoForm(user=request.user,instance=BillInfoModel.objects.get(pk=bill_no))
        if request.method=='POST':
            formbill=BillInfoForm(user=request.user,POST=request.POST,instance=BillInfoModel.objects.get(pk=bill_no))
            if formbill.is_valid():
                formbill.save()
                return redirect('https://dormoni.com/account_panel/bill_table/')
        return render(request,'account_panel/add_bill.html',{'form':formbill,'title':'Muhasebe'})
    else: return redirect('https://dormoni.com/user_panel/login/')


def delete_bill(request,bill_no):
    if request.user.has_perm('account_panel.delete_bilinfomodel') and BillInfoModel.objects.get(pk=bill_no).company_id_id==request.user.company_id_id:
        BillInfoModel.objects.get(pk=bill_no).delete()
        return redirect('https://dormoni.com/account_panel/bill_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')

def transaction_accountsync(account_no,amount,type,desc,time=None):# TODO: bu fonk yeniden düzenlenecek
    if type=='1' or type=='7':
        x=1
    elif type=='8':
        if re.search('[0-9]*',desc):
            transaction_to = re.search('[0-9*]',desc).group()
            x = 1
            asset = PersonAssetInfoModel.objects.filter(person_id=transaction_to)[0]
            periodic_pay=PeriodicPaymentModel.objects.get(person_asset=asset)
            for field_name in sorted(list(periodic_pay.__dict__.keys())):
                if field_name[5:] == str(time.month):
                    periodic_pay.__dict__[field_name]=amount
                    periodic_pay.save()

            asset.amount = str(float(asset.amount) + x * float(amount))
            asset.save()
        else:
            return redirect('https://dormoni.com/user_panel/login/')
    else:
        x=-1
    account_no.amount=str(float(account_no.amount)+x*float(amount))
    account_no.save()

def bill_transactionsync(formbill,request):# TODO: bu fonk yeniden düzenlenecen
    if 1==0:
        account_no=AccountInfoModel.objects.filter(type='3',company_id=request.user.company_id_id)[0]
        amount=formbill.cleaned_data.get('amount')
        description=formbill.cleaned_data.get('desc')
        transaction=TransactionInfoModel(account_no=account_no,type='6',amount=amount,time=datetime.datetime.now(),desc=description)
        transaction_accountsync(account_no,amount,type='6',desc=description,time=datetime.datetime.now())
        transaction.save()

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
        for index in PeriodicPaymentModel.objects.filter(company_id=request.user.company_id_id).order_by('person_asset'):
            if int(month)<8:
                form_mount=list(PeriodicPaymentForm(user=request.user,instance=index))[int(month)+6]
            else:
                form_mount=list(PeriodicPaymentForm(user=request.user,instance=index))[int(month)-6]
            all_forms.append(((index,form_mount), PeriodicPaymentForm(user=request.user, instance=index)))

        monthnames = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim','Kasım', 'Aralık']
        return render(request,'account_panel/table_period_payment.html',{'title':'Muhasebe','all_forms':all_forms,'month':monthnames[int(month)]})