# -*- coding: utf-8 -*-
from django import forms
from .models import StudentLeaveModel,AttendanceInfoModel,StudentInfoModel
from django.core.validators import validate_email
from django.core import mail
from user_panel.models import CompanyInfoModel

class StudentLeaveForm(forms.ModelForm):
    def __init__(self, user,POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(StudentLeaveForm, self).__init__(POST,*args, **kwargs)
        self.user=user
        self.fields['person'].queryset =StudentInfoModel.objects.filter(company_id=user.company_id)

    start=forms.DateField(label='İzin Başlangıç Tarihi',widget=forms.DateInput(attrs={'class':'date-picker'}))
    end=forms.DateField(label='İzin Bitiş Tarihi',widget=forms.DateInput(attrs={'class':'date-picker'}))
    person=forms.ModelChoiceField(StudentInfoModel.objects.all(),label='Öğrenci Numarası',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    reason=forms.CharField(max_length=50,label='İzin Sebebi')
    company_id=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)
    class Meta:
        model=StudentLeaveModel
        fields=('start',
                'end',
                'person',
                'reason',
                'company_id',
                )
    def clean(self):
        startd=self.cleaned_data.get('start')
        endd=self.cleaned_data.get('end')
        if startd and endd:
            if endd<startd:
                self.add_error('end','Lütfen Geçerli Bir Tarih Giriniz')
            for row in StudentLeaveModel.objects.all():
                if row.start and row.end:
                    if startd<=row.start<=endd:
                        self.add_error('start','Girdiğiniz Tarih Aralığında Öğrenci İzinli Gözüküyor')
                    if startd<=row.end<=endd:
                        self.add_error('end','GirdiğinizTarih Aralığında Öğrenci İzinli Gözüküyor')
    def clean_company_id(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id_id)


class AttendanceInfoForm(forms.ModelForm):
    def __init__(self, user, POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(AttendanceInfoForm, self).__init__(POST,*args, **kwargs)
        self.fields['people_selection'].queryset = StudentInfoModel.objects.filter(company_id=user.company_id)

    person=forms.ModelChoiceField(StudentInfoModel.objects.all(),label='Öğrenci Numarası',widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    in_list=[('1','in'),('2','out')]
    in_or_out= forms.TypedChoiceField(choices=in_list,widget=forms.RadioSelect,coerce=str)
    time=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"pickTime": False,"startDate": "2007","class":"datetime-picker","style":"height: 30px"}),label='İşlem Zamanı')
    class Meta:
        model=AttendanceInfoModel
        fields=['person',
                'time',
                'in_or_out']
    def clean(self):
        #kontrol edilmedi
        pos=self.cleaned_data.get('in_or_out')
        per=self.cleaned_data.get('person')
        if pos and per:
            last = AttendanceInfoModel.objects.filter(person=per).last().in_or_out
            if pos==last:
                self.add_error('in_or_out','Geçiş Reddedildi')
    def clean_company_id(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id_id)


class MailSendForm(forms.Form):
    def __init__(self, user, POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(MailSendForm, self).__init__(POST,*args, **kwargs)
        self.fields['people_selection'].queryset = StudentInfoModel.objects.filter(company_id=user.company_id)

    people_selection=forms.ModelChoiceField(StudentInfoModel.objects.all(),required=False,widget=forms.Select(attrs={"style":"height: 50px","class":"select2"}))
    people_manual=forms.CharField(max_length=200,required=False)
    subject=forms.CharField(max_length=100)
    message=forms.CharField(max_length=500,widget=forms.Textarea())

    class Meta:
        fields=[
                'people_selection',
                'people_manual',
                'subject',
                'message'
                ]

    def clean(self):
        selected=self.cleaned_data.get('people_selection')
        manual=self.cleaned_data.get('people_manual')
        if selected==None and manual==None:
            self.add_error('people_selection','Lütfen Bir Kişi Seçiniz ya da E-Posta Adresi Yazınız.')
    def save (self):
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        selected_people = self.cleaned_data['people_selection']
        written_people = self.cleaned_data['people_manual'].split(', ')
        print (subject,message)
        print (selected_people,written_people)
        if selected_people and not written_people:
            to_ma=selected_people
        elif written_people and not selected_people:
            to_ma=written_people
        else:
            to_ma = selected_people + written_people
        mail.send_mail(subject, message, self.user.email, to_ma)

    def clean_company_id(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id_id)

