# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.core.files import File
from .models import StudentLeaveModel,AttendanceInfoModel,VacationInfoModel
from .forms import StudentLeaveForm,AttendanceInfoForm,MailSendForm,VacationInfoForm
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
                return redirect('https://dormoni.com/operation_panel/leave_table/')
        return render(request,'operation_panel/add_leave.html',{'form':leave_form,'title':'Öğrenci'})
    else:
        return redirect('https://dormoni.com/user_panel/login/')

def table_student_leave(request):
    if request.user.has_perm('operation_panel.add_studentleavemodel'):
        leave_list=StudentLeaveModel.objects.filter(company_id=request.user.company_id)
        return render(request,'operation_panel/table_leave.html',{'leave_list':leave_list,'title':'Öğrenci'})
    else:
        return redirect('https://dormoni.com/user_panel/login/')

def add_attendance(request):
    if request.user.has_perm('operation_panel.add_attendanceinfomodel'):
        formattendance=AttendanceInfoForm(user=request.user)
        if request.method=='POST':
            formattendance=AttendanceInfoForm(POST=request.POST,user=request.user)
            if formattendance.is_valid():
                formattendance.save()
                return redirect('https://dormoni.com/operation_panel/attendance_table/')
        return render(request,'operation_panel/add_attendance.html',{'form':formattendance,'title':'Öğrenci'})
    else:
        return redirect('https://dormoni.com/user_panel/login/')

def table_attendance(request):
    if request.user.has_perm('person_panel.delete_studentinfomodel'):
        record_list=AttendanceInfoModel.objects.filter(company_id=request.user.company_id)
        return render(request, 'operation_panel/table_attendance.html', {'record_list':record_list,'title':'Öğrenci'})
    else:
        return redirect('https://dormoni.com/user_panel/login/')

def send_a_mail(request,person_mail):
    if request.user.has_perm('person_panel.add_personalinfomodel'):
        if request.method=='POST':
            formmail=MailSendForm(user=request.user,POST=request.POST)
            if formmail.is_valid():
                formmail.save()
                return redirect('https://dormoni.com/operation_panel/mail_send/')
        if person_mail:
            formmail=MailSendForm(initial={'people_manual':person_mail},user=request.user)
        else:
            formmail=MailSendForm(user=request.user)
        return render(request,'operation_panel/send_mail.html',{'form':formmail,'title':'Öğrenci'})
    else:
        return redirect('https://dormoni.com/user_panel/login/')

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
        return redirect('https://dormoni.com/user_panel/login/')

def change_student_position(request,student_id):# TODO: Turnike sistemleriyle entegreler öğrenilecek
    if request.user.has_perm('person_panel.add_studentinfomodel') and StudentInfoModel.objects.get(pk=student_id).company_id_id==request.user.company_id_id:
        student=StudentInfoModel.objects.get(pk=student_id)
        if student.student_position==True:
            student.student_position=False
        else:
            student.student_position=True
        student.save()
        return redirect('https://dormoni.com/person_panel/student/%s'%student_id)
    else:
        return redirect('https://dormoni.com/user_panel/login/')

def create_egm_xml(request): # TODO: Eminiyet için xml dosyası oluşturulacak
    if request.user.has_perm('person_panel.add_studentinfomodel'):
        if request.method=='POST':
            sstudent_list=request.POST.getlist('sstudent_list')
            if len(sstudent_list)==0:
                sstudent_list=StudentInfoModel.objects.filter(company_id=request.user.company_id_id)

            file2 = open('egm.xml', 'w+')
            file=File(file2)
            file.write('<?xml version="1.0" encoding="utf-8"?><?hash DB1BE508AA9F2D9233C6E9BB06CDFD46?>')
            file.write('<Konaklama TesisKodu="123" Tarih="' + str(datetime.datetime.now()) + '" GonderenProgram="Dormoni.com" >')
            for student in sstudent_list:
                print (student)
                file.write('<Kisi SiraNo="'+student.id+'" TCKimlikNo="'+student.tcn+'" Adi="'+student.name+'" Soyadi="'+student.last_name+'" BabaAdi="'+student.father+'" '
                                                        'AnaAdi="'+student.mother+'" DoğumYeri="'+student.birth_city_name+'" DoğumTarihi="'+student.birth_day+'" Uyrugu="'+student.nation_name+'" KimlikBelgesiTuru="'+student.idcard_type_name+'" '
                                                        'NufasaKayitliOlduğuIl="'+student.register_vilage+'" NufusaKAyitliOlduguIlce="'+student.register_town+'" '
                                                        'NufusaKayitliOlduğuMahalle="'+student.register_distinct+'" Cinsiyet="'+student.gender_name+'" VerilenOdaNo="'+student.room_id_id+'" '
                                                        'NufusCilt="'+student.nufus_cilt+'" NufusAileSira="'+student.nufus_ailesira+'" NufusSiraNo="'+student.nufus_sirano+'" MedeniHali="'+student.medeni_hali_name+'" />')
            file.write('</Konaklama>')
            file.close()
            file2.close()
        student_list=StudentInfoModel.objects.filter(company_id=request.user.company_id_id)
        return render(request,'operation_panel/create_egm_xml.html',{'student_list':student_list,'title':'Öğrenci'})
    else:
        return redirect('https://dormoni.com/user_panel/login/')

def vacation_permission(request):
    pass

def add_vacation(request):
    if request.user.has_perm('operation_panel.add_vacationinfomodel'):
        formvacation = VacationInfoForm(user=request.user)
        if request.method == "POST":
            formvacation = VacationInfoForm(user=request.user,POST=request.POST)
            if formvacation.is_valid():
                formvacation.save()
                return redirect('https://dormoni.com/operation_panel/vacation_table/')
        return render(request, 'operation_panel/add_vacation.html', {'form': formvacation,'title':'Personel'})
    else:
        return redirect('https://dormoni.com/user_panel/login/')

def table_vacation(request):
    if request.user.has_perm('operation_panel.add_vacationinfomodel'):
        vacation_list=VacationInfoModel.objects.filter(company_id=request.user.company_id_id)
        return render(request, 'operation_panel/table_vacation.html', {'vacation_list':vacation_list, 'title':'Personel'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def edit_vacation(request,vacation_id):
    if request.user.has_perm('operation_panel.change_vacationinfomodel') and VacationInfoModel.objects.get(pk=vacation_id).company_id_id==request.user.company_id_id:
        if request.method == "POST":
            formvacation =VacationInfoForm(user=request.user,POST=request.POST,instance=VacationInfoModel.objects.get(pk=vacation_id))
            if formvacation.is_valid():
                formvacation.save()
                return redirect('https://dormoni.com/operation_panel/vacation_table/')
        formvacation = VacationInfoForm(user=request.user,instance=VacationInfoModel.objects.get(pk=vacation_id))
        return render(request, 'operation_panel/add_vacation.html', {'form': formvacation,'title':'Personel'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def delete_vacation(request,vacation_id):
    if request.user.has_perm('operation_panel.delete_vacationinfomodel') and VacationInfoModel.objects.get(pk=vacation_id).company_id_id == request.user.company_id_id:
        VacationInfoModel.objects.get(pk=vacation_id).delete()
        return redirect('https://dormoni.com/operation_panel/vacation_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')