# -*- coding: utf-8 -*-
from django import forms
from .models import StudentLeaveModel,AttendanceInfoModel,StudentInfoModel
from django.utils import timezone

class StudentLeaveForm(forms.ModelForm):
    class Meta:
        model=StudentLeaveModel
        fields=(
                'leave_start',
                'leave_end',
                'person_id',
                'leave_reason',
                )

class AttendanceInfoForm(forms.ModelForm):
    in_list=[('1','in'),('2','out')]
    in_or_out= forms.TypedChoiceField(choices=in_list,widget=forms.RadioSelect,coerce=str)
    class Meta:
        model=AttendanceInfoModel
        fields=['person_id',
                'traffic_date',
                'in_or_out']


class MailSendForm(forms.Form):
    people_selection=forms.ModelChoiceField(StudentInfoModel.objects.all(),required=False)
    people_manual=forms.CharField(max_length=200,required=False)
    subject=forms.CharField(max_length=100)
    message=forms.CharField(max_length=500,widget=forms.TextInput)

    class Meta:
        fields=[
                'people_selection',
                'people_manual',
                'subject',
                'message'
                ]
