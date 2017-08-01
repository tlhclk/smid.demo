# -*- coding: utf-8 -*-
from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core import mail
from .forms import StudentInfoForm,ParentInfoForm,PersonalInfoForm,PersonIDInfoForm
from .models import StudentInfoModel,ParentInfoModel,PersonalInfoModel,PersonIDInfoModel


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
                email = formstudent.cleaned_data.get('e_mail')
                new_user_add(first_name, last_name, email,id,group_id='1')
                room_no=formstudent.cleaned_data.get('room_no')
                room_no.room_people=str(int(room_no.room_people)+1)
                room_no.save()
                formstudent.save()
                profile_pic_config(StudentInfoModel.objects.get(pk=id))
            return redirect('http://127.0.0.1:8000/account_panel/asset_add/')
        return render(request, 'person_panel/add_student.html', {'form': formstudent,'model_info':StudentInfoModel,'title':'Yeni Öğrenci Kaydı'})
    else:
        return redirect('http://127.0.0.1:8000/home/')

def detail_student(request,student_id):
    if request.user.has_perm('person_panel.view_studentinfomodel'):
        student = StudentInfoModel.objects.get(pk=student_id)
        parent = ParentInfoModel.objects.filter(student_id=student_id)
        return render(request, 'person_panel/detail_student.html', {'student': student,'parent':parent,'title':'Öğrenci Detayı'})
    else: return redirect('http://127.0.0.1:8000/home/')

def table_student(request):
    if request.user.has_perm('person_panel.view_studentinfomodel'):
        student_list=StudentInfoModel.objects.all()
        return  render(request, 'person_panel/table_student.html',{'student_list':student_list, 'title': 'Öğrenci Tablosu'})
    else: return redirect('http://127.0.0.1:8000/home/')

def edit_student(request,student_id):
    if request.user.has_perm('person_panel.change_studentinfomodel'):
        if request.method=='POST':
            formstudent=StudentInfoForm(request.POST,instance=StudentInfoModel.objects.get(pk=student_id))
            if formstudent.is_valid():
                formstudent.save()
                return redirect('http://127.0.0.1:8000/person_panel/student_table/')
        formstudent=StudentInfoForm(instance=StudentInfoModel.objects.get(pk=student_id))
        return render(request,'person_panel/add_student.html',{'form':formstudent,'model_info':StudentInfoModel,'title':'Öğrenci Ekleme'})
    else: return redirect('http://127.0.0.1:8000/home/')

def delete_student(request,student_id):
    if request.user.has_perm('person_panel.delete_studentinfomodel'):
        student=StudentInfoModel.objects.get(pk=student_id)
        parent=ParentInfoModel.objects.filter(student_id=student_id)
        if len(parent)!=0:
            parent[0].delete()
        student.delete()
        if len(User.objects.filter(username=student.e_mail))!=0:
            user = User.objects.filter(username=student.e_mail)[0]
            user.delete()
        return redirect('http://127.0.0.1:8000/person_panel/student_table/')
    else: return redirect('http://127.0.0.1:8000/home/')

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
            return redirect('http://127.0.0.1:8000/person_panel/parent_table/')
        return render(request, 'person_panel/add_parent.html', {'form':formparent,'model_info':StudentInfoModel.objects.all(), 'title':'Yeni Veli Kaydı'})
    else: return redirect('http://127.0.0.1:8000/home/')

def detail_parent(request,parent_id):
    if request.user.has_perm('person_panel.view_parentinfomodel'):
        if parent_id[:4]=='1701':
            parent_list=ParentInfoModel.objects.filter(student_id=parent_id)
            if len(parent_list)!=0:
                parent=parent_list[0]
                return render(request, 'person_panel/detail_parent.html', {'parent': parent,'title':'Veli Detayı'})
            return redirect('http://127.0.0.1:8000/person_panel/parent_table')
        else:
            parent = ParentInfoModel.objects.get( pk=parent_id)
            return render(request, 'person_panel/detail_parent.html', {'parent': parent,'title':'Veli Detayı'})
    else: return redirect('http://127.0.0.1:8000/home/')

def table_parent(request):
    if request.user.has_perm('person_panel.view_parentinfomodel'):
        parent_list=ParentInfoModel.objects.all()
        return render(request, 'person_panel/table_parent.html', {'parent_list':parent_list, 'title':'Veli Tablosu'})
    else: return redirect('http://127.0.0.1:8000/home/')

def edit_parent(request,parent_id):
    if request.user.has_perm('person_panel.change_parentinfomodel'):
        formparent=ParentInfoForm(instance=ParentInfoModel.objects.get(pk=parent_id))
        if request.method=='POST':
            formparent=ParentInfoForm(request.POST,instance=ParentInfoModel.objects.get(pk=parent_id))
            if formparent.is_valid():
                formparent.save()
                return redirect('http://127.0.0.1:8000/person_panel/parent_table/')
        return render(request,'person_panel/add_parent.html',{'form':formparent, 'title':'Veli Düzenleme'})
    else: return redirect('http://127.0.0.1:8000/home/')

def delete_parent(request,parent_id):
    if request.user.has_perm('person_panel.delete_parentinfomodel'):
        parent=ParentInfoModel.objects.get(pk=parent_id)
        parent.delete()
        return redirect('http://127.0.0.1:8000/person_panel/parent_table/')
    else: return redirect('http://127.0.0.1:8000/home/')

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
                email = formpersonal.cleaned_data.get('e_mail')
                new_user_add(first_name, last_name, email,id,group_id=3)
                formpersonal.save()
                profile_pic_config(PersonalInfoModel.objects.get(pk=id))
                return redirect('http://127.0.0.1:8000/person_panel/personal_table/')
        return render(request, 'person_panel/add_personal.html', {'form': formpersonal,'model_info':PersonIDInfoModel.objects.all(),'city_list':PersonIDInfoModel.city_list,'blood_type_list':StudentInfoModel.blood_type_list,'title':'Yeni Personel Kaydı'})
    else:
        return redirect('http://127.0.0.1:8000/home/')

def detail_personal(request,personal_id):
    if request.user.has_perm('person_panel.view_personalinfomodel'):
        personal = PersonalInfoModel.objects.get( pk=personal_id)
        return render(request, 'person_panel/detail_personal.html', {'personal': personal, 'title':'Personel Detayı'})
    else: return redirect('http://127.0.0.1:8000/home/')

def table_personal(request):
    if request.user.has_perm('person_panel.view_personalinfomodel'):
        personal_list=PersonalInfoModel.objects.all()
        return render(request, 'person_panel/table_personal.html', {'personal_list':personal_list, 'title':'Personel Tablosu'})
    else: return redirect('http://127.0.0.1:8000/home/')

def edit_personal(request,personal_id):
    if request.user.has_perm('person_panel.change_personalinfomodel'):
        if request.method == "POST":
            formpersonal =PersonalInfoForm(request.POST,instance=PersonalInfoModel.objects.get(pk=personal_id))
            if formpersonal.is_valid():
                formpersonal.save()
                return redirect('http://127.0.0.1:8000/person_panel/personal_table/')
        formpersonal = PersonalInfoForm(instance=PersonalInfoModel.objects.get(pk=personal_id))
        return render(request,'person_panel/add_personal.html',{'form':formpersonal,'model_info':PersonIDInfoModel.objects.all(),'city_list':PersonIDInfoModel.city_list,'blood_type_list':StudentInfoModel.blood_type_list,'title':'Personel Ekleme'})
    else: return redirect('http://127.0.0.1:8000/home/')

def delete_personal(request,personal_id):
    if request.user.has_perm('person_panel.delete_personalinfomodel'):
        PersonalInfoModel.objects.get(pk=personal_id).delete()
        return redirect('http://127.0.0.1:8000/person_panel/personal_table/')
    else: return redirect('http://127.0.0.1:8000/home/')

def add_person_id(request):
    if request.user.has_perm('person_panel.add_personidinfomodel'):
        formstudent = PersonIDInfoForm()
        if request.method == "POST":
            formstudent = PersonIDInfoForm(request.POST, request.FILES)
            if formstudent.is_valid():
                formstudent.save()
            return redirect('http://127.0.0.1:8000/person_panel/student_add/')
        return render(request, 'person_panel/add_person_id.html', {'form': formstudent,'model_info':PersonIDInfoModel,'title':'Yeni Kimlik Kaydı'})
    else:
        return redirect('http://127.0.0.1:8000/home/')

def detail_person_id(request,person_id):
    if request.user.has_perm('person_panel.view_personidinfomodel'):
        print (request.user)
        person=PersonIDInfoModel.objects.get(pk=person_id)
        person_info=(StudentInfoModel.objects.filter(student_tcn=person_id) or PersonalInfoModel.objects.filter(personal_tcn=person_id))
        return render(request,'person_panel/detail_person_id.html',{'person':person,'person_info':person_info[0],'title':'Kimlik Detayı'})
    else: return redirect('http://127.0.0.1:8000/home/')

def table_person_id(request):
    if request.user.has_perm('person_panel.view_personidinfomodel'):
        person_id_list=PersonIDInfoModel.objects.all()
        return render(request, 'person_panel/table_person_id.html', {'person_id_list':person_id_list,'title':'Kimlik Tablosu'})
    else: return redirect('http://127.0.0.1:8000/home/')

def edit_person_id(request,person_id):
    if request.user.has_perm('person_panel.change_personidinfomodel'):
        if request.method == "POST":
            formperson_id =PersonIDInfoForm(request.POST,instance=PersonIDInfoModel.objects.get(pk=person_id))
            print (formperson_id)
            if formperson_id.is_valid():
                formperson_id.save()
                return redirect('http://127.0.0.1:8000/person_panel/person_id_table/')
        formperson_id = PersonIDInfoForm(instance=PersonIDInfoModel.objects.get(pk=person_id))
        return render(request,'person_panel/add_person_id.html',{'form':formperson_id,'model_info':PersonIDInfoModel,'title':'Kimlik Düzenleme'})
    else: return redirect('http://127.0.0.1:8000/home/')

def delete_person_id(request,person_id):
    if request.user.has_perm('person_panel.delete_personidinfomodel'):
        PersonIDInfoModel.objects.get(pk=person_id).delete()
        User.objects.get(pk=person_id).delete()
        return redirect('http://127.0.0.1:8000/person_panel/person_id_table/')
    else: return redirect('http://127.0.0.1:8000/home/')

def show_profile(request,person_id):
    if person_id[:4]=='1701':
        return redirect('http://127.0.0.1:8000/person_panel/student/'+person_id)
    elif person_id[:4]=='1703':
        return redirect('http://127.0.0.1:8000/person_panel/personal/' + person_id)
    elif person_id[:4]=='1704':
        return redirect('http://127.0.0.1:8000/person_panel/parent/' + person_id)
    else:
        if len(StudentInfoModel.objects.filter(student_tcn=person_id))!=0:
            student = StudentInfoModel.objects.filter(student_tcn=person_id)[0]
            return redirect('http://127.0.0.1:8000/person_panel/student/' + student.id)
        elif len(PersonalInfoModel.objects.filter(personal_tcn=person_id))!=0:
            personal = PersonalInfoModel.objects.filter(personal_tcn=person_id)[0]
            return redirect('http://127.0.0.1:8000/person_panel/personal/' + personal.id)
        else:
            return ('Aranan Kayıt Bulunamadı')

def profile_pic_config(user):
    try:
        email=user.e_mail
        import os
        os.rename(user.image_field.path,os.path.join(os.path.split(user.image_field.path)[0],str(email)+'.jpg'))
        user.image_field.name='profile_pic/'+str(email)+'.jpg'
        user.save()
    except FileNotFoundError:
        pass