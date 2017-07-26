# -*- coding: utf-8 -*-
from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import mail
from .forms import StudentInfoForm,ParentInfoForm,PersonalInfoForm,PersonIDInfoForm
from .models import StudentInfoModel,ParentInfoModel,PersonalInfoModel,PersonIDInfoModel
from stock_panel.models import RoomInfoModel
from operation_panel.models import StudentLeaveModel
import datetime


def options_menu(request):
    return render(request,'person_panel/option_menu.html')

def add_student(request):
    if request.user.has_perm('person_panel.add_studentinfomodel'):
        new_id=str(int(StudentInfoModel.objects.all().order_by('-id')[0].id)+1)
        formstudent = StudentInfoForm(initial={'id':new_id})
        if request.method == "POST":
            formstudent = StudentInfoForm(request.POST, request.FILES)
            if formstudent.is_valid():
                id=formstudent.cleaned_data.get('id')
                student_tcn = formstudent.cleaned_data.get('student_tcn')
                first_name= student_tcn.s_name
                last_name = student_tcn.s_lastname
                email = formstudent.cleaned_data.get('student_email')
                new_user_add(first_name, last_name, email,id,group_id='1')
                room_no=formstudent.cleaned_data.get('room_no')
                room_no.room_people=str(int(room_no.room_people)+1)
                room_no.save()
                formstudent.save()
            return redirect('http://127.0.0.1:8000/account_panel/asset_add/')
        #student_new_id = int(StudentInfoModel.objects.all().order_by('-id')[0].id)+1
        return render(request, 'person_panel/add_student.html', {'form': formstudent,'model_info':StudentInfoModel})
    else:
        return HttpResponse('You has no authorization to add a student')

def detail_student(request,student_id):
    if request.user.has_perm('person_panel.view_studentinfomodel'):
        student = StudentInfoModel.objects.get( pk=student_id)
        user = User.objects.get(username=student.student_email)
        parent = ParentInfoModel.objects.filter(person_id=student_id)
        leave_boolean=True
        return render(request, 'person_panel/detail_student.html', {'student': student, 'user':user,'parent':parent,'show':True,'leave_boolean':leave_boolean})

    elif request.user.has_perm('person_panel.view_profile'):
        student = StudentInfoModel.objects.get( pk=student_id)
        user = User.objects.get(username=student.student_email)
        leave_boolean=None
        if len(StudentLeaveModel.objects.filter(student_id=student_id))!=0:
            for permi in StudentLeaveModel.objects.filter(student_id=student_id):
                if datetime.datetime.strptime(str(permi.leave_start),"%Y-%m-%d")<=datetime.datetime.strptime(str(datetime.date.today()),'%Y-%m-%d')<=datetime.datetime.strptime(str(permi.leave_end),"%Y-%m-%d"):
                    leave_boolean=permi.leave_start,permi.leave_end
        return render(request, 'person_panel/detail_student.html', {'student': student, 'user': user,'leave_boolean':leave_boolean})

    else: return HttpResponse('You has no authorization to view student profile <a href="../"> Go back</a>')

def table_student(request):
    if request.user.has_perm('person_panel.view_studentinfomodel'):
        student_list=StudentInfoModel.objects.all()
        all_in,all_all=(len(StudentInfoModel.objects.filter(student_position=True)),len(StudentInfoModel.objects.all()))
        #return render(request, 'person_panel/table_student.html', {'student_list':student_list,'all_in':all_in,'all_all':all_all})
        return  render(request, 'person_panel/table_student.html',{'student_list':student_list})
    else: return HttpResponse('You has no authorization to view student info list')

def edit_student(request,student_id):
    if request.user.has_perm('person_panel.change_studentinfomodel'):
        if request.method=='POST':
            formstudent=StudentInfoForm(request.POST,instance=StudentInfoModel.objects.get(pk=student_id))
            if formstudent.is_valid():
                formstudent.save()
                return redirect('../')
        formstudent=StudentInfoForm(instance=StudentInfoModel.objects.get(pk=student_id))
        return render(request,'person_panel/add_student.html',{'form':formstudent,'model_info':StudentInfoModel})
    else: return HttpResponse('You has no authorization to change student info')

def delete_student(request,student_id):
    if request.user.has_perm('person_panel.delete_studentinfomodel'):
        student=StudentInfoModel.objects.get(pk=student_id)
        parent=ParentInfoModel.objects.filter(student_id=student_id)
        if len(parent)!=0:
            parent[0].delete()
        student.delete()
        if len(User.objects.filter(username=student.student_email))!=0:
            user = User.objects.get(username=student.student_email)
            user.delete()
        return redirect('../student_table/')
    else: return HttpResponse('You has no authorization to delete a student')

# user add and sending mail
def new_user_add(first_name,last_name,email,id,group_id):
    new_pass = User.objects.make_random_password(10)
    new_user=User(id=id,username=email,first_name=first_name,last_name=last_name,email=email)
    new_user.set_password(new_pass)
    new_user.save()
    new_user.groups.add(group_id)
    subj = 'New Password'
    mesg = 'Thanks for joining our system. \nUsername/E-mail = %s \nYour first password is: %s' % (email, new_pass)
    send_a_email([email],subj,mesg)

def send_a_email(email_list,subject,message,from_ma='tlhclk1312@gmail.com'):
    to_ma = ['tlhclk1312@windowslive.com']
    for email in email_list:
        if'std.sehir.edu.tr' in email or 'windowslive' in email or 'mail' in email:
            to_ma.append(email)
    mail.send_mail(subject, message, from_ma, to_ma)

def add_parent(request):
    if request.user.has_perm('person_panel.add_parentinfomodel'):
        new_id=str(int(ParentInfoModel.objects.all().order_by('-id')[0].id)+1)
        formparent= ParentInfoForm(initial={'id':new_id})
        if request.method == "POST":
            formparent = ParentInfoForm(request.POST)
            if formparent.is_valid():
                formparent.save()
            return redirect('http://127.0.0.1:8000/person_panel/parent_table')
        return render(request, 'person_panel/add_parent.html', {'form':formparent,'model_info':StudentInfoModel.objects.all()})
    else: return HttpResponse('You has no authorization to add a parent')

def detail_parent(request,parent_id):
    if request.user.has_perm('person_panel.view_parentinfomodel'):
        if parent_id[:4]=='1701':
            parent_list=ParentInfoModel.objects.filter(student_id=parent_id)
            if len(parent_list)!=0:
                parent=parent_list[0]
                return render(request, 'person_panel/detail_parent.html', {'parent': parent})
            return redirect('http://127.0.0.1:8000/person_panel/parent_table')
        else:
            parent = ParentInfoModel.objects.get( pk=parent_id)
            return render(request, 'person_panel/detail_parent.html', {'parent': parent})
    else: return HttpResponse('You has no authorization to view parent profile <a href="../"> Go back</a>')

def table_parent(request):
    if request.user.has_perm('person_panel.view_parentinfomodel'):
        parent_list=ParentInfoModel.objects.all()
        return render(request, 'person_panel/table_parent.html', {'parent_list':parent_list})
    else: return HttpResponse('You has no authorization to view parent info list')

def edit_parent(request,parent_id):
    if request.user.has_perm('person_panel.change_parentinfomodel'):
        formparent=ParentInfoForm(instance=ParentInfoModel.objects.get(pk=parent_id))
        if request.method=='POST':
            formparent=ParentInfoForm(request.POST,instance=ParentInfoModel.objects.get(pk=parent_id))
            if formparent.is_valid():
                formparent.save()
                return redirect('../')
        return render(request,'person_panel/add_parent.html',{'form':formparent})
        #return render(request,'person_panel/edit_parent.html',{'parent':parent})
    else: return HttpResponse('You has no authorization to change parent info')

def delete_parent(request,parent_id):
    if request.user.has_perm('person_panel.delete_parentinfomodel'):
        parent=ParentInfoModel.objects.get(pk=parent_id)
        parent.delete()
        return redirect('../parent_table/')
    else: return HttpResponse('You has no authorization to delete a parent')

def add_personal(request):
    if request.user.has_perm('person_panel.add_personalinfomodel'):
        new_id=str(int(PersonalInfoModel.objects.all().order_by('-id')[0].id)+1)
        formpersonal = PersonalInfoForm(initial={'id':new_id})
        if request.method == "POST":
            formpersonal = PersonalInfoForm(request.POST, request.FILES)
            print (formpersonal)
            if formpersonal.is_valid():
                id=formpersonal.cleaned_data.get('id')
                personal_tcn= formpersonal.cleaned_data.get('personal_tcn')
                first_name = personal_tcn.s_name
                last_name = personal_tcn.s_lastname
                email = formpersonal.cleaned_data.get('personal_email')
                new_user_add(first_name, last_name, email,id,group_id=3)
                formpersonal.save()
                return redirect('http://127.0.0.1:8000/person_panel/personal_table')
        return render(request, 'person_panel/add_personal.html', {'form': formpersonal,'model_info':PersonIDInfoModel.objects.all(),'city_list':PersonIDInfoModel.city_list,'blood_type_list':StudentInfoModel.blood_type_list})
    else:
        return HttpResponse('You has no authorization to add a personal')

def detail_personal(request,personal_id):
    if request.user.has_perm('person_panel.view_personalinfomodel'):
        personal = PersonalInfoModel.objects.get( pk=personal_id)
        user = User.objects.get(pk=personal_id)
        return render(request, 'person_panel/detail_personal.html', {'personal': personal, 'user': user})

    else: return HttpResponse('You has no authorization to view personal profile <a href="../"> Go back</a>')

def table_personal(request):
    if request.user.has_perm('person_panel.view_personalinfomodel'):
        personal_list=PersonalInfoModel.objects.all()
        return render(request, 'person_panel/table_personal.html', {'personal_list':personal_list})
    else: return HttpResponse('You has no authorization to view personal info list')

def edit_personal(request,personal_id):
    if request.user.has_perm('person_panel.change_personalinfomodel'):
        if request.method == "POST":
            formpersonal =PersonalInfoForm(request.POST,instance=PersonalInfoModel.objects.get(pk=personal_id))
            if formpersonal.is_valid():
                formpersonal.save()
                return redirect('../personal_table/')
        formpersonal = PersonalInfoForm(instance=PersonalInfoModel.objects.get(pk=personal_id))
        return render(request,'person_panel/add_personal.html',{'form':formpersonal})
    else: return HttpResponse('You has no authorization to change personal info')

def delete_personal(request,personal_id):
    if request.user.has_perm('person_panel.delete_personalinfomodel'):
        PersonalInfoModel.objects.get(pk=personal_id).delete()
        User.objects.get(pk=personal_id).delete()
        return redirect('../')
    else: return HttpResponse('You has no authorization to delete a personal')


def multiple_add(request):
    if request.method=='POST':
        form1=StudentInfoForm(request.POST,prefix='std')
        form2=PersonIDInfoForm(request.POST,prefix='prsn')
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('../')
    else:
        form1=StudentInfoForm(prefix='std')
        form2=PersonIDInfoForm(request.POST,prefix='prsn')
        return render(request,'person_panel/default_form.html',{'form1':form1,'form2':form2})

def add_person_id(request):
    if request.user.has_perm('person_panel.add_studentinfomodel'):
        formstudent = PersonIDInfoForm()
        if request.method == "POST":
            formstudent = PersonIDInfoForm(request.POST, request.FILES)
            if formstudent.is_valid():
                formstudent.save()
            return redirect('http://127.0.0.1:8000/person_panel/student_add/')
        #student_new_id = int(StudentInfoModel.objects.all().order_by('-id')[0].id)+1
        return render(request, 'person_panel/add_person_id.html', {'form': formstudent,'model_info':PersonIDInfoModel})
    else:
        return HttpResponse('You has no authorization to add a student')

def table_person_id(request):
    if request.user.has_perm('person_panel.view_personidinfomodel'):
        person_id_list=PersonIDInfoModel.objects.all()
        return render(request, 'person_panel/table_person_id.html', {'person_id_list':person_id_list})
    else: return HttpResponse('You has no authorization to view person_id info list')

def edit_person_id(request,person_id):
    if request.user.has_perm('person_panel.change_personidinfomodel'):
        if request.method == "POST":
            formperson_id =PersonIDInfoForm(request.POST,instance=PersonIDInfoModel.objects.get(pk=person_id))
            if formperson_id.is_valid():
                formperson_id.save()
                return redirect('http://127.0.0.1:8000/person_panel/person_id_table')
        formperson_id = PersonIDInfoForm(instance=PersonIDInfoModel.objects.get(pk=person_id))
        return render(request,'person_panel/add_person_id.html',{'form':formperson_id,'model_info':PersonIDInfoModel})
    else: return HttpResponse('You has no authorization to change person_id info')

def delete_person_id(request,person_id):
    if request.user.has_perm('person_panel.delete_personidinfomodel'):
        PersonIDInfoModel.objects.get(pk=person_id).delete()
        User.objects.get(pk=person_id).delete()
        return redirect('http://127.0.0.1:8000/person_panel/person_id_table')
    else: return HttpResponse('You has no authorization to delete a person_id')

def show_profile(request,person_id):
    if person_id[:4]=='1701':
        if request.user.has_perm('person_panel.view_studentinfomodel'):
            student=StudentInfoModel.objects.get(pk=person_id)
            user=User.objects.get(pk=person_id)
            person_id=PersonIDInfoModel.objects.get(pk=student.student_tcn.id)
            return render(request,'person_panel/detail_student.html',{'student':student,'user':user,'person_id':person_id})
    elif person_id[:4]=='1703':
        if request.user.has_perm('person_panel.view_personalinfomodel'):
            personal=PersonalInfoModel.objects.get(pk=person_id)
            user=User.objects.get(pk=person_id)
            return render(request,'person_panel/detail_personal.html',{'personal':personal,'user':user})
    elif person_id[:4]=='1704':
        if request.user.has_perm('person_panel.view_parentinfomodel'):
            parent=ParentInfoModel.objects.get(pk=person_id)
            student=StudentInfoModel.objects.get(pk=parent.person_id.id)
            return render(request,'person_panel/detail_parent.html',{'student':student,'parent':parent})
    else: return HttpResponse('Aranan Kayıt Bulunanamadı')