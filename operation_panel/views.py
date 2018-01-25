# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.core.files import File
from .models import StudentLeaveModel,AttendanceInfoModel,VacationInfoModel,NotificationInfoModel
from .forms import StudentLeaveForm,AttendanceInfoForm,MailSendForm,VacationInfoForm
from person_panel.models import StudentInfoModel
from user_panel.models import CompanyInfoModel
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
        return render(request,'operation_panel/add_leave.html',{'form':leave_form,'title':'Öğrenci'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_student_leave(request,student_id):
    if request.user.has_perm('operation_panel.change_studentleavemodel'):
        leave_list=StudentLeaveModel.objects.filter(company=request.user.company)
        if student_id: leave_list=leave_list.filter(person=student_id)
        return render(request,'operation_panel/table_leave.html',{'leave_list':leave_list,'title':'Öğrenci'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_student_leave(request,sleave_id):
    if request.user.has_perm('sleave_info.add_studentleavemodel'):
        sleave=StudentInfoModel.objects.get(pk=sleave_id,company=request.user.company_id)
        if request.method=='POST':
            formleave=StudentLeaveForm(POST=request.POST,user=request.user,instance=sleave)
            if formleave.is_valid():
                formleave.save()
                return redirect('http://127.0.0.1:8000/operation_panel/leave_table/')
        formleave=StudentLeaveForm(POST=request.POST,user=request.user,instance=sleave)
        return render(request, 'operation_panel/add_leave.html', {'form': formleave,'title':'Öğrenci'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_student_leave(request,sleave_id):
    if request.user.has_perm('operation_panel.add_studentleavemodel'):
        StudentLeaveModel.objects.get(pk=sleave_id,company=request.user.company_id).delete()
        return redirect('http://127.0.0.1:8000/operation_panel/leave_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')


def add_vacation(request):
    if request.user.has_perm('operation_panel.add_vacationinfomodel'):
        formvacation = VacationInfoForm(user=request.user)
        if request.method == "POST":
            formvacation = VacationInfoForm(user=request.user,POST=request.POST)
            if formvacation.is_valid():
                formvacation.save()
                return redirect('http://127.0.0.1:8000/operation_panel/vacation_table/')
        return render(request, 'operation_panel/add_vacation.html', {'form': formvacation,'title':'Personel'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_vacation(request,personal_id):
    if request.user.has_perm('operation_panel.change_vacationinfomodel'):
        vacation_list=VacationInfoModel.objects.filter(company=request.user.company_id)
        if personal_id: vacation_list=vacation_list.filter(person=personal_id)
        return render(request, 'operation_panel/table_vacation.html', {'vacation_list':vacation_list, 'title':'Personel'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_vacation(request,vacation_id):
    if request.user.has_perm('operation_panel.add_vacationinfomodel'):
        vacation=VacationInfoModel.objects.get(pk=vacation_id,company=request.user.company_id)
        if request.method == "POST":
            formvacation =VacationInfoForm(user=request.user,POST=request.POST,instance=vacation)
            if formvacation.is_valid():
                formvacation.save()
                return redirect('http://127.0.0.1:8000/operation_panel/vacation_table/')
        formvacation = VacationInfoForm(user=request.user,instance=vacation)
        return render(request, 'operation_panel/add_vacation.html', {'form': formvacation,'title':'Personel'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_vacation(request,vacation_id):
    if request.user.has_perm('operation_panel.add_vacationinfomodel'):
        VacationInfoModel.objects.get(pk=vacation_id,company=request.user.company_id).delete()
        return redirect('http://127.0.0.1:8000/operation_panel/vacation_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')


def add_attendance(request):
    if request.user.has_perm('operation_panel.add_attendanceinfomodel'):
        formattendance=AttendanceInfoForm(user=request.user)
        if request.method=='POST':
            formattendance=AttendanceInfoForm(POST=request.POST,user=request.user)
            if formattendance.is_valid():
                formattendance.save()
                return redirect('http://127.0.0.1:8000/operation_panel/attendance_table/')
        return render(request,'operation_panel/add_attendance.html',{'form':formattendance,'title':'Öğrenci'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_attendance(request):
    if request.user.has_perm('person_panel.change_studentinfomodel'):
        record_list=AttendanceInfoModel.objects.filter(company=request.user.company)
        return render(request, 'operation_panel/table_attendance.html', {'record_list':record_list,'title':'Öğrenci'})
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
        return render(request,'operation_panel/send_mail.html',{'form':formmail,'title':'Öğrenci'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def mail_inbox(request):# TODO: mail sistemi kurulacak
    if request.user.has_perm('person_panel.add_personidinfomodel'):
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
    if request.user.has_perm('person_panel.add_studentinfomodel') and StudentInfoModel.objects.get(pk=student_id).company_id==request.user.company_id:
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
                sstudent_list=StudentInfoModel.objects.filter(company=request.user.company_id)
            print(sstudent_list)
            file2 = open('egm.xml', 'w+')
            file=File(file2)
            file.write('<?xml version="1.0" encoding="utf-8"?><?hash DB1BE508AA9F2D9233C6E9BB06CDFD46?>')
            file.write('<Konaklama TesisKodu="123" Tarih="' + str(datetime.datetime.now()) + '" GonderenProgram="Dormoni.com" >')
            for student_id in sstudent_list:
                student=StudentInfoModel.objects.get(pk=student_id)
                file.write('<Kisi SiraNo="'+student.id+'" TCKimlikNo="'+student.tcn_id+'" Adi="'+student.tcn.name+'" Soyadi="'+student.tcn.last_name+'" BabaAdi="'+student.tcn.father+'" '
                                                        #'AnaAdi="'+str(student.tcn.mother)+'" DoğumYeri="'+str(student.tcn.birth_city_name)+'" DoğumTarihi="'+str(student.tcn.birth_day)+'" Uyrugu="'+str(student.tcn.nation_name)+'" KimlikBelgesiTuru="'+str(student.tcn.idcard_type_name)+'" '
                                                        'NufasaKayitliOlduğuIl="'+student.tcn.register_vilage+'" NufusaKAyitliOlduguIlce="'+student.tcn.register_town+'" '
                                                        'NufusaKayitliOlduğuMahalle="'+student.tcn.register_distinct+'" Cinsiyet="'+student.tcn.gender_name+'" VerilenOdaNo="'+student.room_id_id+'" '
                                                        'NufusCilt="'+student.tcn.nufus_cilt+'" NufusAileSira="'+student.tcn.nufus_ailesira+'" NufusSiraNo="'+student.tcn.nufus_sirano+'" MedeniHali="'+student.tcn.medeni_hali_name+'" />')
            file.write('</Konaklama>')
            file.close()
            file2.close()
        student_list=StudentInfoModel.objects.filter(company=request.user.company_id)
        return render(request,'operation_panel/create_egm_xml.html',{'student_list':student_list,'title':'Öğrenci'})
    else:
        return redirect('http://127.0.0.1:8000/user_panel/login/')

def notification(request=None,company=None):#TODO: mantığı unuttum bi ara yapıcam
    if request.user.has_perm('user_panel.add_user'):
        late_payment=('','')
        stu_absence=('','')
        end_of_month=('','')
        event=('','')
        last_day_bill=('','')
        all_results=[late_payment,stu_absence,end_of_month,event,last_day_bill]
        for item in all_results:
            if request:
                if item not in NotificationInfoModel.objects.values_list('title','text').filter(company=request.user.company):
                    new_notification=NotificationInfoModel(title=item[0],text=item[1],company=request.user.company,day=datetime.date.today())
                    new_notification.save()
            elif company:
                if item not in NotificationInfoModel.objects.values_list('title', 'text').filter(company=company):
                    new_notification=NotificationInfoModel(title=item[0],text=item[1],company=company,day=datetime.date.today())
                    new_notification.save()
    else: redirect('http://127.0.0.1:8000/user_panel/login/')
