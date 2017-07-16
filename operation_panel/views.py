# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.core.files import File
from .models import StudentLeaveModel,AttendanceInfoModel
from .forms import StudentLeaveForm,AttendanceInfoForm
from person_panel.views import send_a_email
from person_panel.models import StudentInfoModel
import datetime

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

def send_a_mail(request):
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

def create_egm_xml(request):
    if request.method=='POST':
        sstudent_list=request.POST.getlist('sstudent_list')
        if len(sstudent_list)==0:
            sstudent_list=StudentInfoModel.objects.all()

        file2 = open('deneme.xml', 'w+')
        file=File(file2)
        file.write('<?xml version="1.0" encoding="utf-8"?><?hash DB1BE508AA9F2D9233C6E9BB06CDFD46?>')
        file.write('<Konaklama TesisKodu="123" Tarih="' + str(datetime.datetime.now()) + '" GonderenProgram="SMiD" >')
        for student in sstudent_list:
            print (student)
            # file.write('<Kisi SiraNo="'+student.id+'" TCKimlikNo="'+student.student_tcn+'" Adi="'+student.student_name+'" Soyadi="'+student.student_lastname+'" BabaAdi="'+student.student_father+'" '
            #                                         'AnaAdi="'+student.student_mother+'" DoğumYeri="'+student.birth_place+'" Uyrugu="'+student.student_nation_name+'" KimlikBelgesiTuru="'+student.s_idcard_type_name+'" '
            #                                        'NufasaKayitliOlduğuIl="'+student.s_register_vilage+'" NufusaKAyitliOlduguIlce="'+student.s_register_town+'" '
            #                                         'NufusaKayitliOlduğuMahalle="'+student.s_register_distinct+'" Cinsiyet="'+student.s_gender+'" VerilenOdaNo="'+student.room_no.room_no+'" '
            #                                         'NufusCilt="'+student.s_nufus_cilt+'" NufusAileSira="'+student.s_nufus_ailesira+'" NufusSiraNo="'+student.s_nufus_sirano+'" MedeniHali="'+student.s_medeni_hali+'" />')
        file.write('</Konaklama>')
        file.close()
        file2.close()

        print (sstudent_list)
    student_list=StudentInfoModel.objects.all()
    return render(request,'operation_panel/create_egm_xml.html',{'student_list':student_list})