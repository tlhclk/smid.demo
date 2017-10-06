# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.core.files import File
from .models import StudentLeaveModel,AttendanceInfoModel
from .forms import StudentLeaveForm,AttendanceInfoForm,MailSendForm
from person_panel.models import StudentInfoModel
import datetime
import imaplib

def add_student_leave(request):
    if request.user.has_perm('operation_panel.add_studentleavemodel'):
        leave_form=StudentLeaveForm(user=request.user)
        if request.method=='POST':
            leave_form = StudentLeaveForm(POST=request.POST,user=request.user)
            if leave_form.is_valid():
                leave_form.save()
                return redirect('http://127.0.0.1:8000/operation_panel/leave_table/')
        return render(request,'operation_panel/add_leave.html',{'form':leave_form,'title':'Yeni İzin Kaydı'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_student_leave(request):
    if request.user.has_perm('operation_panel.add_studentleavemodel'):
        leave_list=StudentLeaveModel.objects.filter(company_id=request.user.company_id)
        return render(request,'operation_panel/table_leave.html',{'leave_list':leave_list,'title':'İzin Tablosu'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def add_attendance(request):
    if request.user.has_perm('operation_panel.add_attendanceinfomodel'):
        formattendance=AttendanceInfoForm(user=request.user)
        if request.method=='POST':
            formattendance=AttendanceInfoForm(POST=request.POST,user=request.user)
            if formattendance.is_valid():
                formattendance.save()
                return redirect('http://127.0.0.1:8000/operation_panel/attendance_table/')
        return render(request,'operation_panel/default_form.html',{'form':formattendance,'title':'Yeni Yoklama Kaydı'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_attendance(request):
    if request.user.has_perm('person_panel.delete_studentinfomodel'):
        record_list=AttendanceInfoModel.objects.filter(company_id=request.user.company_id)
        return render(request, 'operation_panel/table_attendance.html', {'record_list':record_list,'title':'Attendance Table'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def send_a_mail(request,person_mail):
    if request.user.has_perm('person_panel.add_personalinfomodel'):
        if request.method=='POST':
            formmail=MailSendForm(user=request.user,POST=request.POST)
            if formmail.is_valid():
                formmail.save()
                return redirect('http://127.0.0.1:8000/operation_panel/mail_send/')
        if person_mail:
            formmail=MailSendForm(initial={'people_manual':person_mail},user=request.user)
        else:
            formmail=MailSendForm(user=request.user)
        return render(request,'operation_panel/send_mail.html',{'form':formmail,'title':'Mail Gönder'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def mail_inbox(request):# TODO: mail sistemi kurulacak
    if request.user.has_perm('person_panel.add_studentinfomodel'):
        mail = imaplib.IMAP4_SSL('smtp.gmail.com')
        mail.login('tlhclk1312@gmail.com', 'Tlhclk.12')
        mail.select('inbox')
        print (mail)
        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()
        print (id_list)
        for i in range(int(id_list[-1]),int(id_list[0]),-1):
            result, data = mail.uid('fetch', str(i), '(X-GM-THRID X-GM-MSGID)')
            print (result,data)
            # typ,data=mail.fetch(str(i),'(RFC3501)')
            #
            # for response_part in data:
            #     if isinstance(response_part, tuple):
            #         msg = email.message_from_string(response_part[1])
            #         email_subject = msg['subject']
            #         email_from = msg['from']
            #         print ('From : ' + email_from + '\n')
            #         print ('Subject : ' + email_subject + '\n')
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def change_student_position(request,student_id):# TODO: Turnike sistemleriyle entegreler öğrenilecek

    if request.user.has_perm('person_panel.add_studentinfomodel') and StudentInfoModel.objects.get(pk=student_id).company_id_id==request.user.company_id_id:
        student=StudentInfoModel.objects.get(pk=student_id)
        if student.student_position==True:
            student.student_position=False
        else:
            student.student_position=True
        student.save()
        return redirect('http://127.0.0.1:8000/person_panel/student/%s'%student_id)
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def create_egm_xml(request): # TODO: Eminiyet için xml dosyası oluşturulacak
    if request.user.has_perm('person_panel.add_studentinfomodel'):
        if request.method=='POST':
            sstudent_list=request.POST.getlist('sstudent_list')
            if len(sstudent_list)==0:
                sstudent_list=StudentInfoModel.objects.filter(company_id=request.user.company_id_id)

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
        student_list=StudentInfoModel.objects.all()
        return render(request,'operation_panel/create_egm_xml.html',{'student_list':student_list})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')
