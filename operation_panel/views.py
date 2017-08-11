# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.core.files import File
from .models import StudentLeaveModel,AttendanceInfoModel
from .forms import StudentLeaveForm,AttendanceInfoForm,MailSendForm
from django.core import mail
from person_panel.models import StudentInfoModel
import datetime
import imaplib
import email



def add_student_leave(request):
    if request.user.has_perm('operation_panel.add_studentleavemodel'):
        leave_form=StudentLeaveForm()
        if request.method=='POST':
            leave_form = StudentLeaveForm(request.POST)
            if leave_form.is_valid():
                leave_form.save()
                return redirect('http://www.dormoni.com/operation_panel/leave_table/')
        return render(request,'operation_panel/add_leave.html',{'form':leave_form,'title':'Yeni İzin Kaydı','model_info':StudentLeaveModel})
    else:
        return redirect('http://www.dormoni.com/login/')

def table_student_leave(request):
    if request.user.has_perm('operation_panel.view_studentleavemodel'):
        leave_list=StudentLeaveModel.objects.all()
        return render(request,'operation_panel/table_leave.html',{'leave_list':leave_list,'title':'İzin Tablosu'})
    else:
        return redirect('http://www.dormoni.com/login/')

def add_attendance(request):
    formattendance=AttendanceInfoForm()
    if request.method=='POST':
        formattendance=AttendanceInfoForm(request.POST)
        if formattendance.is_valid():
            formattendance.save()
            return redirect('http://www.dormoni.com/operation_panel/attendance_table/')
    return render(request,'operation_panel/default_form.html',{'form':formattendance,'model_info':'','title':'Yeni Yoklama Kaydı'})

def table_attendance(request):
    record_list=AttendanceInfoModel.objects.all()
    return render(request, 'operation_panel/table_attendance.html', {'record_list':record_list})

def send_a_mail(request,person_mail):
    if request.method=='POST':
        formmail=MailSendForm(request.POST)
        print (formmail)
        if formmail.is_valid():
            subject=request.POST['subject']
            message=request.POST['message']
            selected_people=request.POST.getlist('people_selection')
            written_people=request.POST['people_manual'].split(', ')
            to_ma=selected_people+written_people
            mail.send_mail(subject,message,'tlhclk1312@gmail.com',to_ma)
            return redirect('http://www.dormoni.com/login/')
    if person_mail:
        formmail=MailSendForm(initial={'people_manual':person_mail})
    else:
        formmail=MailSendForm()
    return render(request,'operation_panel/send_mail.html',{'form':formmail,'person_list':StudentInfoModel.objects.all(),'title':'Mail Gönder'})

def mail_inbox():
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

def change_student_position(request,student_id):
    student=StudentInfoModel.objects.get(pk=student_id)
    if student.student_position==True:
        student.student_position=False
    else:
        student.student_position=True
    student.save()
    return redirect('http://www.dormoni.com/person_panel/student/%s'%student_id)

def create_egm_xml(request):
    if request.user.has_perm('person_panel.delete_studentinfomodel'):
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
        student_list=StudentInfoModel.objects.all()
        return render(request,'operation_panel/create_egm_xml.html',{'student_list':student_list})
    else:
        return redirect('http://www.dormoni.com/login/')
