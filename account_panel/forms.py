# -*- coding: utf-8 -*-
from django import forms
from .models import TransactionInfoModel,PersonAssetInfoModel,AccountInfoModel,BillInfoModel,PeriodicPaymentModel
from person_panel.models import StudentInfoModel
from user_panel.models import CompanyInfoModel
import re,datetime

class TransactionInfoForm(forms.ModelForm):
    def __init__(self, user,POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(TransactionInfoForm, self).__init__(POST,*args, **kwargs)
        self.user=user
        self.fields['account'].queryset =AccountInfoModel.objects.filter(company=user.company)

    account=forms.ModelChoiceField(AccountInfoModel.objects.all(),label='Hesap Numarası',widget=forms.Select(attrs={"class":"select2"}))
    type=forms.ChoiceField(choices=TransactionInfoModel.transaction_type_list,label='İşlem Türü',widget=forms.Select(attrs={"class":"select2"}))
    amount=forms.CharField(max_length=10,label='İşlem Miktarı')
    time=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"datetime-picker"}),label='İşlem Zamanı')
    desc=forms.CharField(max_length=100,label='İşlem Açıklaması',required=False)
    company=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)

    class Meta:
        model=TransactionInfoModel
        fields=[
            'account',
            'type',
            'amount',
            'time',
            'desc',
            'company',
        ]
    def clean(self):
        amount=self.cleaned_data.get('amount')
        if 0.0<float(amount)<10000.00:
            print (amount)
        else:
            self.add_error('amount','Yanlış Miktar')
        desc=self.cleaned_data.get('desc')
        if self.cleaned_data.get('type')=='7':
            if re.search('[0-9]+',desc):
                asset=PeriodicPaymentModel.objects.filter(person_asset=re.search('[0-9]+',desc).group())[0]
                total=float(asset.debt)+float(asset.amount)
                period=int(asset.period)
                rest=float(amount)%(total/period)
                if rest!=0.0:
                    self.add_error('amount','Lütfen Kişiye Belirlenmiş Taksit Denemini Giriniz!')
            else:
                self.add_error('desc','Öğrenci Numarasını Açıklamayı Yazınız!')

    def clean_company(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id)

    def add(self):
        type=self.cleaned_data.get('type')
        amount=self.cleaned_data.get('amount')
        if type=='7' and type=='1':
            account = self.cleaned_data.get('account')
            account.amount = str(float(account.amount) + float(amount))
            account.save()
            if type=='7':
                time=self.cleaned_data.get('time')
                desc=self.cleaned_data.get('desc')
                ppayment=PeriodicPaymentModel.objects.filter(person_asset=re.search('[0-9]+',desc).group())[0]
                period=time.mounth
                for field in ppayment._meta.fields:
                    if field.name==str(period):
                        old=float(ppayment.__getattribute__(field.name)) or 0.0
                        new=float(amount)
                        ppayment.__setattr__(field.name,str(old+new))
                        ppayment.save()
        else:
            account=self.cleaned_data.get('account')
            account.amount=str(float(account.amount)-float(amount))
            account.save()

    def remove(self,no):
        transaction=TransactionInfoModel.objects.get(pk=no)
        type=transaction.type
        if type=='7' and type=='1':
            account=transaction.account
            account.amount=str(float(account.amount)-float(transaction.amount))
            account.save()
            if type=='7':
                ppayment=PeriodicPaymentModel.objects.filter(person_asset=re.search('[0-9]+',transaction.desc).group())[0]
                period=transaction.time.mounth
                for field in ppayment._meta.fields:
                    if field.name==str(period):
                        old=float(ppayment.__getattribute__(field.name)) or 0.0
                        new=float(transaction.amount)
                        ppayment.__setattr__(field.name,str(old-new))
                        ppayment.save()
        else:
            account=transaction.account
            account.amount=str(float(account.amount)+float(transaction.amount))
            account.save()


class PersonAssetInfoForm(forms.ModelForm):
    def __init__(self, user,POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(PersonAssetInfoForm, self).__init__(POST,*args, **kwargs)
        self.user=user
        self.fields['person'].queryset =StudentInfoModel.objects.filter(company=user.company)

    id=forms.CharField(max_length=10,label='Sözleşme No')
    person=forms.ModelChoiceField(StudentInfoModel.objects.all(),label='Öğrenci No',widget=forms.Select(attrs={"class":"select2"}))
    debt=forms.CharField(max_length=6,label='Ödenecek Miktar')
    period=forms.CharField(max_length=2,label='Taksit Miktarı')
    type=forms.ChoiceField(choices=PersonAssetInfoModel.asset_type_list,label='Ödeme Türü',widget=forms.Select(attrs={"class":"select2"}))
    desc=forms.CharField(max_length=100,label='Ödeme Planı Açıklaması',required=False)
    company=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)
    class Meta:
        model=PersonAssetInfoModel
        fields=[
            'id',
            'person',
            'debt',
            'period',
            'type',
            'desc',
            'company',
        ]
    def clean(self):
        debt=self.cleaned_data.get('debt')
        if 0.0<float(debt)<100000.00:
            print ('total'+debt)
        else:
            self.add_error('debt','Yanlış Miktar')
        period=self.cleaned_data.get('period')
        if 0<int(period)<13:
            print('period'+period)
        else:
            self.add_error('period','Yanlış Dönem')

    def clean_company(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id)


class AccountInfoForm(forms.ModelForm):
    def __init__(self, user,POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(AccountInfoForm, self).__init__(POST,*args, **kwargs)
        self.user=user

    no=forms.CharField(max_length=10,label='Hesap Numarası')
    name=forms.CharField(max_length=20,label='Hesap Adı')
    type=forms.ChoiceField(choices=AccountInfoModel.account_type_list,label='Hesap Türü',widget=forms.Select(attrs={"class":"select2"}))
    amount=forms.CharField(max_length=10,label='Hesap Miktarı')
    desc=forms.CharField(max_length=100,label='Hesap Aciklamasi',required=False)
    bank_code=forms.ChoiceField(choices=AccountInfoModel.bank_code_list,label='Banka Şubesi',widget=forms.Select(attrs={"class":"select2"}))
    company=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)
    class Meta:
        model=AccountInfoModel
        fields=[
            'no',
            'name',
            'type',
            'amount',
            'desc',
            'bank_code',
            'company',
        ]
    def clean(self):
        amount=self.cleaned_data.get('amount')
        if 0.0<float(amount)<100000.00:
            print (amount)
        else:
            self.add_error('amount','Yanlış Miktar')

    def clean_company(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id)


class BillInfoForm(forms.ModelForm):
    def __init__(self, user,POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(BillInfoForm, self).__init__(POST,*args, **kwargs)
        self.user=user

    type=forms.ChoiceField(choices=BillInfoModel.bill_type_list,label='Fatura Türü',widget=forms.Select(attrs={"class":"select2"}))
    code=forms.CharField(max_length=10,label='Fatura Kodu')
    amount=forms.CharField(max_length=10,label='Fatura Miktarı')
    payed=forms.BooleanField(required=False,label='Ödendi')
    last_day=forms.DateField(widget=forms.DateInput(attrs={"class":"date-picker","style":"height: 30px"}),label='Fatura Son Ödeme Tarihi')
    address=forms.CharField(max_length=200,label='Fatura Adresi',required=False)
    desc=forms.CharField(max_length=100,label='Fatura Açıklaması',required=False)
    company=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)
    class Meta:
        model=BillInfoModel
        fields=[
            'type',
            'code',
            'amount',
            'payed',
            'last_day',
            'address',
            'desc',
            'company',
        ]
    def clean(self):
        amount = self.cleaned_data.get('amount')
        if 0.0 < float(amount) < 10000.00:
            print(amount)
        else:
            self.add_error('amount', 'Yanlış Miktar')

    def clean_company(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id)

    def add(self):
        amount=self.cleaned_data.get('amount')
        type1=self.cleaned_data.get('type')
        code=self.cleaned_data.get('code')
        company=self.user.company
        account=AccountInfoModel.objects.filter(company=company)[0]
        new_tra=TransactionInfoModel(account=account,type='6',amount=amount,time=datetime.datetime.now(),desc=type1+' - '+code,company=company)
        new_tra.save()
        account.amount=str(float(account.amount)+float(amount))
        account.save()

    def remove(self,bill_no):
        bill=BillInfoModel.objects.get(pk=bill_no)
        amount=bill.amount
        type1=bill.type
        code=bill.code
        company=self.user.company
        account=AccountInfoModel.objects.filter(company=company)[0]
        new_tra=TransactionInfoModel(account=account,type='6',amount=amount,time=datetime.datetime.now(),desc=type1+' - '+code,company=company)
        new_tra.save()
        account.amount=str(float(account.amount)+float(amount))
        account.save()



class PeriodicPaymentForm(forms.ModelForm):
    def __init__(self, user,POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(PeriodicPaymentForm, self).__init__(POST,*args, **kwargs)
        self.user=user
        self.fields['person_asset'].queryset =PersonAssetInfoModel.objects.filter(company=user.company)

    person_asset=forms.ModelChoiceField(PersonAssetInfoModel.objects.all(),widget=forms.Select(),label='Ödeme Planı')
    deposito=forms.CharField(max_length=6,label='Deposito Miktarı',required=False)
    month1=forms.CharField(max_length=6,label='Eylül',required=False)
    month2=forms.CharField(max_length=6,label='Ekim',required=False)
    month3=forms.CharField(max_length=6,label='Kasım',required=False)
    month4=forms.CharField(max_length=6,label='Aralık',required=False)
    month5=forms.CharField(max_length=6,label='Ocak',required=False)
    month6=forms.CharField(max_length=6,label='Şubat',required=False)
    month7=forms.CharField(max_length=6,label='Mart',required=False)
    month8=forms.CharField(max_length=6,label='Nisan',required=False)
    month9=forms.CharField(max_length=6,label='Mayıs',required=False)
    month10=forms.CharField(max_length=6,label='Haziran',required=False)
    month11=forms.CharField(max_length=6,label='Temmuz',required=False)
    month12=forms.CharField(max_length=6,label='Ağustos',required=False)
    desc=forms.CharField(max_length=200,label='Açıklama',required=False)
    company=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False,label='company')

    class Meta:
        model=PeriodicPaymentModel
        fields=['person_asset',
                'deposito',
                'month1',
                'month2',
                'month3',
                'month4',
                'month5',
                'month6',
                'month7',
                'month8',
                'month9',
                'month10',
                'month11',
                'month12',
                'desc',
                'company'
                ]

    def clean(self):
        month1 = self.cleaned_data.get('month1')
        if month1:
            if 0.0 < float(month1) < 10000.00: pass
            else:self.add_error('month1', 'Yanlış Miktar')
        month2 = self.cleaned_data.get('month2')
        if month2:
            if 0.0 < float(month2) < 10000.00: pass
            else:self.add_error('month2', 'Yanlış Miktar')
        month3 = self.cleaned_data.get('month3')
        if month3:
            if 0.0 < float(month3) < 10000.00: pass
            else:self.add_error('month3', 'Yanlış Miktar')
        month4 = self.cleaned_data.get('month4')
        if month4:
            if 0.0 < float(month4) < 10000.00: pass
            else:self.add_error('month4', 'Yanlış Miktar')
        month5 = self.cleaned_data.get('month5')
        if month5:
            if 0.0 < float(month5) < 10000.00: pass
            else:self.add_error('month5', 'Yanlış Miktar')
        month6 = self.cleaned_data.get('month6')
        if month6:
            if 0.0 < float(month6) < 10000.00: pass
            else:self.add_error('month6', 'Yanlış Miktar')
        month7 = self.cleaned_data.get('month7')
        if month7:
            if 0.0 < float(month7) < 10000.00: pass
            else:self.add_error('month7', 'Yanlış Miktar')
        month8 = self.cleaned_data.get('month8')
        if month8:
            if 0.0 < float(month8) < 10000.00: pass
            else:self.add_error('month8', 'Yanlış Miktar')
        month9 = self.cleaned_data.get('month9')
        if month9:
            if 0.0 < float(month9) < 10000.00: pass
            else:self.add_error('month9', 'Yanlış Miktar')
        month10 = self.cleaned_data.get('month10')
        if month10:
            if 0.0 < float(month10) < 10000.00: pass
            else:self.add_error('month10', 'Yanlış Miktar')
        month11 = self.cleaned_data.get('month11')
        if month11:
            if 0.0 < float(month11) < 10000.00: pass
            else:self.add_error('month11', 'Yanlış Miktar')
        month12 = self.cleaned_data.get('month12')
        if month12:
            if 0.0 < float(month12) < 10000.00: pass
            else:self.add_error('month12', 'Yanlış Miktar')
        deposito = self.cleaned_data.get('deposito')
        if deposito:
            if 0.0 < float(deposito) < 10000.00: pass
            else:self.add_error('deposito', 'Yanlış Miktar')

    def clean_company(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id)