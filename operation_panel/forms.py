# -*- coding: utf-8 -*-
from django import forms
from .models import StudentLeaveModel,AttendanceInfoModel,VacationInfoModel
from person_panel.models import StudentInfoModel,PersonalInfoModel
from django.core import mail
from user_panel.models import CompanyInfoModel

class StudentLeaveForm(forms.ModelForm):
    def __init__(self, user,POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(StudentLeaveForm, self).__init__(POST,*args, **kwargs)
        self.user=user
        self.fields['person'].queryset =StudentInfoModel.objects.filter(company=user.company)

    start=forms.DateField(label='İzin Başlangıç Tarihi',widget=forms.DateInput(attrs={'class':'date-picker'}))
    end=forms.DateField(label='İzin Bitiş Tarihi',widget=forms.DateInput(attrs={'class':'date-picker'}))
    person=forms.ModelChoiceField(StudentInfoModel.objects.all(),label='Öğrenci Numarası',widget=forms.Select(attrs={"class":"select2"}))
    reason=forms.CharField(max_length=50,label='İzin Sebebi')
    company=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)
    class Meta:
        model=StudentLeaveModel
        fields=('start',
                'end',
                'person',
                'reason',
                'company',
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

    def clean_company(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id)


class AttendanceInfoForm(forms.ModelForm):# TODO: Turnike Sistemleriyle uyumlu hale getirilecek
    def __init__(self, user, POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(AttendanceInfoForm, self).__init__(POST,*args, **kwargs)
        self.user=user
        self.fields['person'].queryset = StudentInfoModel.objects.filter(company=user.company)

    person=forms.ModelChoiceField(StudentInfoModel.objects.all(),label='Öğrenci Numarası',widget=forms.Select(attrs={"class":"select2"}))
    in_list=(('1','İçeri Girdi'),('0','Dışarı Çıktı'))
    in_or_out= forms.TypedChoiceField(choices=in_list,widget=forms.RadioSelect,coerce=str)
    time=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"datetime-picker"}),label='İşlem Zamanı')
    company=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)

    class Meta:
        model=AttendanceInfoModel
        fields=['person',
                'time',
                'in_or_out',
                'company']

    def clean(self):
        pos=self.cleaned_data.get('in_or_out')
        per=self.cleaned_data.get('person')
        if pos and per:
            if len(AttendanceInfoModel.objects.filter(person=per))!=0:
                last = AttendanceInfoModel.objects.filter(person=per).last().in_or_out
                if pos==last:
                    self.add_error('in_or_out','Geçiş Reddedildi')

    def clean_company(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id)


class MailSendForm(forms.Form):
    def __init__(self, user, POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(MailSendForm, self).__init__(POST,*args, **kwargs)
        self.fields['people_selection'].queryset = StudentInfoModel.objects.filter(company=user.company)

    people_selection = forms.ModelMultipleChoiceField(StudentInfoModel.objects.all(), required=False,widget=forms.CheckboxSelectMultiple(attrs={'class':'select2','multiple':'multiple'}))# TODO: html hazıtrlanırken select2 multiple özelliği kurukacak
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
        written_people = self.cleaned_data['people_manual'].strip().split(',')
        if selected_people and not written_people:
            to_ma=selected_people
        elif written_people and not selected_people:
            to_ma=written_people
        else:
            to_ma = [selected_people.email] + written_people
        from_ma='admin@dormoni.com'
        from_pass='Deneme1234'
        mail.send_mail(subject, message,from_ma,to_ma,auth_user=from_ma,auth_password=from_pass)


class VacationInfoForm(forms.ModelForm):
    def __init__(self, user,POST=None,*args, **kwargs):
        # user is a required parameter for this form.
        super(VacationInfoForm, self).__init__(POST,*args, **kwargs)
        self.user=user
        self.fields['person'].queryset =PersonalInfoModel.objects.filter(company=user.company)

    start_day=forms.DateField(label='İzin Başlangıç Tarihi',widget=forms.DateInput(attrs={'class':'date-picker'}))
    end_day=forms.DateField(label='İzin Bitiş Tarihi',widget=forms.DateInput(attrs={'class':'date-picker'}))
    person=forms.ModelChoiceField(PersonalInfoModel.objects.all(),label='Personel Numarası',widget=forms.Select(attrs={"class":"select2"}))
    reason=forms.CharField(max_length=50,label='İzin Sebebi')
    company=forms.ModelChoiceField(CompanyInfoModel.objects.all(),widget=forms.HiddenInput(),required=False)

    class Meta:
        model=VacationInfoModel
        fields=['person','start_day','end_day','reason','company']

    def clean(self):
        startd = self.cleaned_data.get('start_day')
        endd = self.cleaned_data.get('end_day')
        if startd and endd:
            if endd < startd:
                self.add_error('end', 'Lütfen Geçerli Bir Tarih Giriniz')
            for row in StudentLeaveModel.objects.all():
                if row.start and row.end:
                    if startd <= row.start <= endd:
                        self.add_error('start', 'Girdiğiniz Tarih Aralığında Öğrenci İzinli Gözüküyor')
                    if startd <= row.end <= endd:
                        self.add_error('end', 'GirdiğinizTarih Aralığında Öğrenci İzinli Gözüküyor')

    def clean_company(self):
        return CompanyInfoModel.objects.get(pk=self.user.company_id)