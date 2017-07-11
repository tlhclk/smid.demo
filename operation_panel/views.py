# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import StudentLeaveModel,AttendanceInfoModel
from .forms import StudentLeaveForm,AttendanceInfoForm
from person_panel.views import send_a_email
from person_panel.models import StudentInfoModel

def option_menu(request):
    return render(request,'operation_panel/option_menu.html')

def add_student_leave(request):
    leave_form=StudentLeaveForm()
    if request.method=='POST':
        leave_form = StudentLeaveForm(request.POST)
        if leave_form.is_valid():
            leave_form.save()
            return redirect('../')
    return render(request,'operation_panel/default_form.html',{'form':leave_form})

def add_attendance(request):
    formattendance=AttendanceInfoForm()
    if request.method=='POST':
        formattendance=AttendanceInfoForm(request.POST)
        if formattendance.is_valid():
            formattendance.save()
            return redirect('../../')
    return render(request,'operation_panel/default_form.html',{'form':formattendance})

def table_attendance(request):
    record_list=AttendanceInfoModel.objects.all()
    return render(request, 'operation_panel/table_attendance.html', {'record_list':record_list})


def send_collective_message(request):
    if request.method=='POST':
        subject=request.POST['message_subject']
        message=request.POST['message_content']
        selected_people=request.POST.getlist('message_people')
        written_people=request.POST['message_people_str'].split(', ')
        to_ma=selected_people+written_people
        send_a_email(to_ma,subject,message)
        return redirect('../../')
    people_list=StudentInfoModel.objects.all()
    return render(request,'operation_panel/sending_mail_sms.html',{'people_list':people_list})


def change_student_position(request,student_id):
    student=StudentInfoModel.objects.get(pk=student_id)
    if student.student_position==True:
        student.student_position=False
    else:
        student.student_position=True
    student.save()
    return redirect('../../student/%s'%student_id)
