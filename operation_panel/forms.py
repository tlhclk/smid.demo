# -*- coding: utf-8 -*-
from django import forms
from .models import StudentLeaveModel,AttendanceInfoModel

class StudentLeaveForm(forms.ModelForm):
    class Meta:
        model=StudentLeaveModel
        fields=(#'leave_id',
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

